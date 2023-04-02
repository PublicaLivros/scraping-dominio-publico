import requests
import json
from random import randint
with open("../json/raw_data.json") as dataRaw:
    data = json.load(dataRaw)

def parseTrueBook(books, index, id):
    book = books[index]
    bdata = {
    "cct_status":book["cct_status"],
    "titulo": book["titulo"],
    "id": id,
    "autor": book["autor"],
    "fonte": book["fonte"],
    "tipo_de_arquivo": book["tipo_de_arquivo"],
    "tamanho_do_arquivo": book["tamanho_do_arquivo"],
    "capa": book["capa"]
   }
    return bdata

def parseTrueJSON():
    print(parseTrueBook(data, 0, randint(1, 5000)))

parseTrueJSON()

"""
 def request_pdf():
 url = 'http://www.dominiopublico.gov.br/pesquisa/DetalheObraDownload.do?select_action=&co_obra=19314&co_midia=2'
 response = requests.get(url)
 with open('file.pdf', 'wb') as f:
     f.write(response.content)
"""


