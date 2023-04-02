import requests
import json
from random import randint

with open("../json/raw_data.json") as dataRaw:
    data = json.load(dataRaw)

def requestPdf(url, name, id):
    url = f'{url}&co_midia=2'
    response = requests.get(url)
    with open(f'./dist/{name}_{id}.pdf', 'wb') as f:
        f.write(response.content)

def tryDownload(index, id):
    try:
        requestPdf(data[index]["link"].replace("DetalheObraForm.do", "DetalheObraDownload.do", 1), data[index]["titulo"], id)
    except:
        print("Lascou")

def init():
    for i in range(0, len(data)):
        tryDownload(i, randint(1, 500))
init()

"""
 def request_pdf():
 url = 'http://www.dominiopublico.gov.br/pesquisa/DetalheObraDownload.do?select_action=&co_obra=19314&co_midia=2'
 response = requests.get(url)
 with open('file.pdf', 'wb') as f:
     f.write(response.content)
"""


