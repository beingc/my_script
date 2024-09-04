import requests
from bs4 import BeautifulSoup
import time


class WebCrawler:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers if headers else {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_title(self, soup):
        try:
            title_tag = soup.select_one('div.cont h1 span b')
            return title_tag.get_text(strip=True) + "\n" if title_tag else "No Title Found\n"
        except Exception as e:
            print(f"Error extracting title: {e}")
            return "Error extracting title\n"

    def extract_text(self, soup):
        try:
            content_div = soup.select_one('div.contson')
            paragraphs = content_div.find_all('p') if content_div else []
            return "\n".join([p.get_text(strip=True) for p in paragraphs]) + "\n"
        except Exception as e:
            print(f"Error extracting text: {e}")
            return "Error extracting text\n"

    def save_to_file(self, content, file_name):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(content)

    def run(self, start_url, save_file):
        url = start_url
        while url:
            time.sleep(1)
            html_content = self.fetch_page(url)
            if html_content:
                soup = BeautifulSoup(html_content, 'html.parser')
                # 提取标题
                title_content = self.extract_title(soup)
                print(f"Start processing {title_content.strip()}")
                self.save_to_file(title_content, save_file)
                # 提取正文内容
                text_content = self.extract_text(soup)
                self.save_to_file(text_content, save_file)
                # 获取下一章连接
                next_link = soup.find('a', string='下一章')
                if next_link and 'href' in next_link.attrs:
                    url = next_link['href']
                    if not url.startswith('http'):
                        url = self.base_url + url
                else:
                    url = None


if __name__ == "__main__":
    base_url = "https://www.gushiwen.cn"
    start_url = "https://www.gushiwen.cn/guwen/bookv_c6af930a3d19.aspx"
    save_file = "output.txt"
    crawler = WebCrawler(base_url)
    crawler.run(start_url, save_file)
    print("Complete")
