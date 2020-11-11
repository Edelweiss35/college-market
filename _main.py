import os


def start():
    os.system(  '/usr/bin/python3.6 /root/scraper_0.py &'
                '/usr/bin/python3.6 /root/scraper_1.py &'
                '/usr/bin/python3.6 /root/scraper_2.py &'
                '/usr/bin/python3.6 /root/scraper_3.py &'
                '/usr/bin/python3.6 /root/scraper_4.py &'
                '/usr/bin/python3.6 /root/scraper_5.py &'
                '/usr/bin/python3.6 /root/scraper_6.py &'
                '/usr/bin/python3.6 /root/scraper_7.py &'
                '/usr/bin/python3.6 /root/scraper_8.py')

start()