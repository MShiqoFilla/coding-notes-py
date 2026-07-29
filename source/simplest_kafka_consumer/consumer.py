from kafka import KafkaConsumer
from dotenv import load_dotenv
import json
import os

load_dotenv()

class RunConsumer:
    def consumer(self):
        consumer = KafkaConsumer(
            *["malut-comments-classifier"], #topic name
            bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
            auto_offset_reset="earliest",
            group_id="test",
            enable_auto_commit=False,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            max_poll_records=400
        )

        while True:
            records = []
            message_batch = consumer.poll(timeout_ms=50000, max_records=100)
            for tp, messages in message_batch.items():
                records.extend([msg.value for msg in messages])

            for record in records:
                print(record)
            
            # consumer.commit() #if enable_auto_commit is false

if __name__ == "__main__":
    RunConsumer().consumer()