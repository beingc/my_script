# coding=utf8
# date: 2023-03-23
# desc: get the rank of cnblogs

import datetime
import requests
from bs4 import BeautifulSoup


def get_rank(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    score_tag = soup.find('li', {'class': 'liScore'})
    rank_tag = soup.find('li', {'class': 'liRank'})
    score = score_tag.text.strip().split("-")[-1].strip()
    rank = rank_tag.text.strip().split("-")[-1].strip()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "{},{},{}\n".format(current_time, rank, score)


if __name__ == '__main__':
    username = "your user name"
    url = f"https://www.cnblogs.com/{username}/ajax/sidecolumn.aspx"
    with open("rank.csv", 'a') as f:
        f.writelines(get_rank(url))
