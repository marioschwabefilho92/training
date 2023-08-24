from kafka import KafkaConsumer

consumer = KafkaConsumer('make', group_id='group1', bootstrap_servers=[
                         'localhost:9092', 'localhost:9093'], consumer_timeout_ms=10000)
for msg in consumer:
    print(msg)
