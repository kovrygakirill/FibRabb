import os
import sys
import logging
from rabbitmq import RabbitMQ

from fibonacci import fib
from conf_logging import setup_logging

setup_logging()
logger = logging.getLogger('__name__')

"""Консьюмер получает сообщения из обменника for_fibonacci"""


def main():
    routing_key = 'ABC'
    logger.info("Start Consumer")
    consumer.queue_listener(exchange="for_fibonacci", queue="number_for_fib", routing_key=routing_key,
                            callback=callback)


def callback(ch, method, properties, body):
    """ Функция вызывается консьюмером при получении сообщения из очереди и выводит fibonacci по этому числу"""
    number = int(body.decode())
    result = str(fib(number)).encode()
    logger.info(f"Get message - {number}, Fibonacci = {result.decode()}")
    consumer.publish_message_to_exchange(exchange="result_fib", message=result, routing_key="A")


if __name__ == '__main__':
    try:
        global consumer
        consumer = RabbitMQ("rabbitmq")
        main()
    except KeyboardInterrupt:
        logger.warning('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
