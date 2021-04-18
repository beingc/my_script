# coding=utf8
# date: 2021-04-07
# desc: get github ip with ipaddress.com

import requests
import re
import time


def get_html_text(url):
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    r = requests.get(url, headers=hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def bs_parse_ip2(html):
    url = re.findall(r'ipv4/[\d\.]+', html)
    ip = str(url[0]).split('/')[1]
    return ip


def main():
    search_url = 'https://www.ipaddress.com/search/'
    site_list = ['github.com', 'assets-cdn.github.com', 'github.global.ssl.fastly.net']
    for site in site_list:
        url = search_url + site
        html = get_html_text(url)
        ip = bs_parse_ip2(html)
        print('{} {}'.format(ip, site))


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print("## Used {:.2f} seconds".format(end_time - start_time))
    # todo: improve the script to save time
