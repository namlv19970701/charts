from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
import requests
import json
from airflow.models import Variable
import uuid

tiki_store_variable=Variable.get("tiki_store_api",deserialize_json=True)
job_variable=Variable.get("crawl_tiki",deserialize_json=True)

@task
def extract_stores_from_snowflake(sql):
    snowflake_hook=SnowflakeHook(snowflake_conn_id="snowflake")#,database=database,schema=schema)

    records = snowflake_hook.get_records(sql=sql)
    
    return records

@task
def run_store_api(ids):
    s3_hook=S3Hook(aws_conn_id="aws")
    today=datetime.today()
    date_string = today.strftime('%Y-%m-%d')
    steps=len(ids)//job_variable['batch_size']+1
    for _ in range(steps):
        crawled_data=[]
        for id in ids:
            res=requests.get(f"{tiki_store_variable['api']}{str(id[0])}",headers=tiki_store_variable['headers'])
            if res.status_code==200:
                data=res.json()
                crawled_data.append(data)
        s3_hook.load_string(
            string_data=json.dumps(crawled_data),
            bucket_name=job_variable['bucket'],
            key=f"{job_variable['prefix']}/{date_string}/{str(uuid.uuid4())}.json",
            replace=True 
        )
                        
                
@dag(schedule_interval='@daily', start_date=datetime(2024, 1, 1), catchup=False)
def crawl_product():

    run_store_api(extract_stores_from_snowflake(sql=job_variable['sql']))

crawl_product()
