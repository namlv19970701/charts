from confluent_kafka.avro import AvroProducer
import requests
import json
from tqdm.auto import tqdm
from datetime import datetime
from confluent_kafka import avro

schema_str=open("tiki-store.avsc",'r').read()

value_schema = avro.loads(schema_str)

producer = AvroProducer({'bootstrap.servers': 'localhost:9092','schema.registry.url':'http://localhost:8081'},
                        default_value_schema=value_schema)

session = requests.Session()

seller_id=1
res=session.get(f"{tiki_store_url}{str(i)}",headers=tiki_store_headers)
seller=res.json()['data']['seller']
seller['crawled_at']=datetime.now().timestamp()

producer.produce(topic="e-commerce-tiki-store-data-source",value=seller)
producer.flush()
