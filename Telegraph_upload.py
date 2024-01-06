from telegraph import Telegraph
import requests
import os

def uplload_folder(dir_name:str):
    telegraph = Telegraph()
    telegraph.create_account(short_name='1337')
    
    files = os.listdir(dir_name)
    temp = []
    for img in files:
        with open(f"{dir_name}/{img}", 'rb') as f:
            temp.append(requests.post('https://telegra.ph/upload', files={'file': ('file', f, 'image/jpeg')}).json()[0]['src'])
    content = [f"<img src='{i}'/>" for i in temp]
    
    response = telegraph.create_page(dir_name, html_content="<p>My test page</p>" + "".join(content),)
    return 'http://telegra.ph/{}'.format(response['path'])

if __name__ == "__main__":
    dir_name = "KuukoW - Nahida selfies 1"
    link = uplload_folder(dir_name)
    print(link)