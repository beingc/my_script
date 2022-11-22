#!/usr/bin/env python3
# coding=utf-8
# Date: 2021/2/20 23:03
# Desc: Get bing today wallpaper and save at current directory.

import os
import requests
import logging

# Log function
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)

logger.addHandler(console)


# Get html text
def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        logger.error("Get html text failed.", exc_info=True)
        exit()


# Get the pics url
def get_pics_url(html):
    import xml.dom.minidom
    domtree = xml.dom.minidom.parseString(html)
    url = domtree.getElementsByTagName('url')[0]
    url = 'https://cn.bing.com' + url.childNodes[0].data
    logger.info(url)
    return url


def save_pics(url):
    root = os.path.dirname(os.path.realpath(__file__))
    path = root + '/' + url.split('&')[0].split('OHR.')[1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                logger.info("File save success.")
        else:
            logger.info("File already exists.")
    except Exception:
        logger.error("File save failed.", exc_info=True)


def main():
    # Bing pics API, idx=0(开始日期,0:今天,1:昨天)n=1(数量)
    url = "http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"

    html = get_html_text(url)
    url = get_pics_url(html)
    save_pics(url)


if __name__ == '__main__':
    main()
