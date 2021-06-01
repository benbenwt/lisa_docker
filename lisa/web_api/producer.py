from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json

def produce(topic,value):
    producer = KafkaProducer(
        bootstrap_servers=['172.18.65.187:9092'],
        key_serializer=lambda k: json.dumps(k).encode(),
        value_serializer=lambda v: json.dumps(v).encode())
    # 发送三条消息
    future = producer.send(
        topic,
        key="",
        value=value)
    try:
        future.get(timeout=10)  # 监控是否发送成功
    except kafka_errors:  # 发送失败抛出kafka_errors
        traceback.format_exc()

if __name__=='__main__':
    produce("lisa",r"C:\Users\guo\Desktop\input1")