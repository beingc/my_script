import os
import requests

# 下载hosts文件，来自 https://github.com/521xueweihan/GitHub520
url = "https://raw.hellogithub.com/hosts"
response = requests.get(url)
hosts_content = response.text

# 写入本地hosts文件
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
with open(hosts_path, 'w') as file:
    file.write(hosts_content)

# 刷新DNS缓存
os.system("ipconfig /flushdns")
