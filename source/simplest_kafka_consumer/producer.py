from kafka import KafkaProducer
from dotenv import load_dotenv
import json
import os

load_dotenv()

producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    value_serializer=lambda v:json.dumps(v).encode("utf-8")
)

def send_message(topic:str, message:dict):
    producer.send(topic=topic, value=message)

#producer.flush() #flushing messages, do after sending some is better