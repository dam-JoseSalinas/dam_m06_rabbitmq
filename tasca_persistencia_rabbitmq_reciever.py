import pika

class Tasca_persistencia_rabbitmq_reciever:
    def __init__(self, host, queue, routing_key, exchange=''):
        self._host = host
        self._queue = queue
        self._routing_key = routing_key
        self._exchange = exchange

    def recieve_desa(self):
        def desa_callback(ch, method, properties, body):
            print(f"{body}")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._host))
        channel = connection.channel()
        channel.queue_declare(queue=self._queue)
        channel.basic_consume(queue=self._queue, on_message_callback=desa_callback, auto_ack=True)
        channel.start_consuming()
if __name__ == "__main__":
    receiver = Tasca_persistencia_rabbitmq_reciever('localhost', 'desa', 'desa')
    receiver.recieve_desa()