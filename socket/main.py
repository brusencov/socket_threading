import threading
import time
import requests
from threading import Thread


class GetResponseFromServer(Thread):
    def __init__(self, url, name):
        Thread.__init__(self)
        self.url = url
        self.name = name

    def run(self):
        print(f'Поток #{self.name} начал работу')
        response = requests.get(url=self.url)
        print(f'Поток #{self.name} закончил работу [{response}]')


def run_threads(urls):
    for i, url in enumerate(urls):
        thread = GetResponseFromServer(url, str(i))
        thread.start()


def run_threads_2(urls):
    for i, url in enumerate(urls):
        print(f'Поток #{i} начал работу')
        response = requests.get(url=url)
        print(f'Поток #{i} закончил работу [{response}]')


if __name__ == '__main__':
    urls = [
        'https://logbook.itstep.org/',
        'https://www.google.com/',
        'https://logbook.itstep.org/',
        'https://www.google.com/',
        'https://logbook.itstep.org/',
        'https://www.google.com/',
        'https://logbook.itstep.org/',
        'https://www.google.com/',
        'https://logbook.itstep.org/',
        'https://www.google.com/',
        'https://logbook.itstep.org/',
        'https://www.google.com/',
    ]
    start_time = time.time()
    run_threads(urls)
    print(f'end {time.time() - start_time}')
    for thread in threading.enumerate():
        print(thread.getName())
    print(f'В настоящее время работает {threading.active_count()} потоков')
