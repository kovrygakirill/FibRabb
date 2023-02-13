import pika
from pika.exchange_type import ExchangeType


class RabbitMQ:
    """Класс для работы с RabbitMQ"""
    def __init__(self, host):
        parameters = pika.ConnectionParameters(host=host)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def _exchange_declare(self, name):
        """Создаёт обменник"""
        return self.channel.exchange_declare(exchange=name, exchange_type=ExchangeType.direct, durable=True)

    def _queue_declare(self, name):
        """Создаёт очередь"""
        return self.channel.queue_declare(queue=name, durable=True)

    def close_connection(self):
        """Завершает соединение"""
        self.connection.close()

    def _publish_to_exchange(self, exchange, routing_key, message):
        """Публикует сообщение в указанный обменник"""
        self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)

    def _bind_queue(self, queue, exchange, routing_key):
        """Привязывает очередь к обменнику"""
        self.channel.queue_bind(queue=queue, exchange=exchange, routing_key=routing_key)

    def _queue_listener(self, queue, callback):
        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def queue_listener(self, exchange, queue, routing_key, callback):
        """Создает обменник, очередь, связывает их и начинает получение сообщений из очереди"""
        self._exchange_declare(name=exchange)
        self._queue_declare(name=queue)
        self._bind_queue(queue=queue, exchange=exchange, routing_key=routing_key)
        self._queue_listener(queue=queue, callback=callback)

    def publish_message_to_exchange(self, exchange, message, routing_key):
        """Создает обменник и отправляет в него сообщение"""
        self._exchange_declare(name=exchange)
        self._publish_to_exchange(exchange=exchange, routing_key=routing_key, message=message)
