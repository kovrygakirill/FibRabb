import os
import sys
from time import sleep

from rabbitmq import RabbitMQ

"""Публикует 3 сообщения с интервалом 3 секунда в обменник for_fibonacci"""


def main():
    publisher = RabbitMQ("rabbitmq")
    routing_key = 'ABC'
    messages = ['10', '100', '56']
    print("Start Publisher")
    for message in messages:
        publisher.publish_message_to_exchange(exchange="for_fibonacci", message=message,
                                              routing_key=routing_key)
        sleep(2)
    publisher.close_connection()
    print("Stop Publisher")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
