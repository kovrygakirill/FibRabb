import os
import sys
import logging
from time import sleep
from rabbitmq import RabbitMQ

from conf_logging import setup_logging

setup_logging()
logger = logging.getLogger('__name__')

"""Публикует 3 сообщения с интервалом 3 секунда в обменник for_fibonacci"""


def main():
    publisher = RabbitMQ("rabbitmq")
    routing_key = 'ABC'
    messages = ['10', '100', '56']
    logger.info("Start Publisher")
    for message in messages:
        publisher.publish_message_to_exchange(exchange="for_fibonacci", message=message,
                                              routing_key=routing_key)
        logger.info(f"Send message - {message}")
        sleep(2)
    publisher.close_connection()
    logger.info("Stop Publisher")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.warning('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
