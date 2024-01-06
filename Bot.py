from pyrogram import Client, filters
from pyrogram.types import Message
from cosplay_downloader import download_cosplay
from Telegraph_upload import uplload_folder
import time

api_id = 26262506
api_hash = "591d4da0c263183c34b6352b119188bf"
client = Client("Testy", api_id, api_hash)

def upload_by_link(client: Client, message: Message, link:str, chat_id:str):
    folder = download_cosplay(link)
    # folder = "KuukoW - Nahida selfies 1"
    ph = uplload_folder(folder)
    print(ph)
    client.send_message(chat_id , text=f"[{folder}]({ph})")
    client.send_message(chat_id , text=f"{folder} downloaded.")


@client.on_message(filters=filters.text)
def fff(client: Client, message: Message):
    chat_id = message.from_user.id
    client.send_message(chat_id , text="checking links")
    time.sleep(1)
    links = []
    for link in message.text.split():
        if link[:8] == "https://":
            links.append(link)
    
    client.send_message(chat_id , text=f"{len(links)} packs will be downloaded")
    time.sleep(1)
    for i in range(len(links)):
        client.send_message(chat_id , text=f"Progress: {i}/{len(links)} downloaded.\n[Now downloading]({link})")
        time.sleep(1)
        upload_by_link(client, message, link, chat_id)



client.run()