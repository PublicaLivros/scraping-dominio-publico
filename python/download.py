import requests
import json
import os
from modules.booksparser import *

json_file_absolute_path = os.path.realpath("json/raw_data.json")

with open(json_file_absolute_path, encoding="utf8") as dataRaw:
    data = json.load(dataRaw)

def verifyDirsExist():
    if not os.path.exists('booklibrary'): os.makedirs('booklibrary')

def requestPdf(url, name, id, download_again):
    response = requests.get(url)
    name = fileNameNormalize(name)

    if (response.status_code == 200):
        try:
            with open(f'./booklibrary/{name}_{id}.pdf', 'wb') as f:
                f.write(response.content)
                print(f'\033[1;32mBook saved:\033[1;m {name}. \33[1;32mID:\33[1;m {id}')            
        except:
            print(f'\033[1;31mUnable to save book:\033[1;m {name}, ID: {id}')

        return 

    if (response.status_code == 404 and download_again == False):
        requestPdf(replaceLinkToDownload(response.url, True), name, id, True)
        return
    
    print(f"\033[1;31mArquivo não encontrado no servidor.\033[1;m - Livro: {name}")

def tryDownload(index):
    try:
        requestPdf(replaceLinkToDownload(data[index]["link"] + "&co_midia=2", False), data[index]["titulo"], index, False)
    except:
        print(f'Unable do download book: {data[index]["titulo"]}')

def init():
    verifyDirsExist()
    for i in range(0, len(data)): tryDownload(i)

init()