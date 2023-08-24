from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092', 'localhost:9093'])
for _ in range(10):
    msg = f"some byte message {_}"
    future = producer.send('make', msg.encode())
    result = future.get(timeout=60)
    print(result)
