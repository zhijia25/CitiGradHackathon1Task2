import time
import urllib3

import EmailSender as es


def send():
    pass


def check_availability(check_list):
    http = urllib3.PoolManager()
    for address in check_list:
        try:
            r = http.request('GET', address)
            if r.status == 500:
                es.send_notification(address)
                print("server is down, sending notification")
        except urllib3.exceptions.MaxRetryError:
            es.send_notification(address)
            print("server is down, sending notification")


def timer_start(interval=3, timeout=10, check_list=[]):
    """every 3s checking, 10s"""
    n = 1
    start_time = None
    if start_time is None:
        start_time = time.time()
    while True:
        if time.time() > start_time + timeout:
            print("end play at {}".format(time.asctime(time.localtime(time.time()))))
            break
        elif (time.time() - start_time) % interval == 0:
            print("checking at {}".format(time.asctime(time.localtime(time.time()))))
            check_availability(check_list)
            n += 1


if __name__ == '__main__':
    # fill target websites here
    address_list = ['172.20.10.7:8080/hello_world']
    print("web listener is running!")
    timer_start(check_list=address_list)
