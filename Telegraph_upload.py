from telegraph import Telegraph
import requests
import os

telegraph = Telegraph()
telegraph.create_account(short_name='1337')
dir_name = "KuukoW - Nahida selfies 1"
files = os.listdir(dir_name)
images = []

for img in files:
    with open(f"{dir_name}/{img}", 'rb') as f:
        images.append(requests.post('https://telegra.ph/upload', files={'file': ('file', f, 'image/jpeg')}).json()[0]['src'])
        print(images)


content = [f"<img src='{i}'/>" for i in images]

response = telegraph.create_page(dir_name, html_content="<p>My test page</p>" + "".join(content),)

print('http://telegra.ph/{}'.format(response['path']))