from bs4 import BeautifulSoup
import requests
import shutil
import re
import os

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'uk,en-US;q=0.9,en;q=0.8,ru;q=0.7',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

def download(url: str, folder: str, name = "img"):
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        if not os.path.exists(f"downloads/{folder}"):
            os.makedirs(f"downloads/{folder}")

        with open(f"downloads/{folder}/{name}", 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        print(f"File {name} downladed")
        return 1
    else: 
        print(f"Error {response.status_code}")
        return 0


def findlink(cosplay:str):
    response = requests.get(cosplay, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    title = str(soup.title)[7:].replace("Story Viewer", "").replace("- Hentai Cosplay</title>", "")
    item = soup.find('meta', property = "og:image")
    temp  = re.search(r'(https?://\S+)', str(item)).group(0)
    temp = temp[:-1]
    if temp[:7] == "http://" and temp[-4] == ".":
        pattern = temp[:temp.find('/', -7) + 1] + "{number}" + temp[-4:]
        return title, pattern
    else:
        return 0


def download_cosplay(cosplay_link:str):
    name, pattern = findlink(cosplay_link.replace("image", "story"))
    print(name, pattern, sep="\n")
    folder_name = name.strip().replace("-", "").replace("–", "").replace("*", "").replace("|", "").replace("\\", "").replace("/", "").replace("?", "").replace(":", "").replace("<", "").replace(">", "").replace("  ", " ")#<>:"/\|?*
    i = 1
    while 1:
        if download(pattern.format(number = i), folder_name, f"{i}{pattern[-4:]}"):
            i+=1
        else:
            break
    
    return folder_name

if __name__ == "__main__":
    cosplay = 'https://ru.hentai-cosplays.com/image/kuukow-nahida-selfies-1'
    download_cosplay(cosplay)
    # pattern = "http://static13.hentai-cosplays.com/upload/20231206/360/367889/{number}.jpg"
    