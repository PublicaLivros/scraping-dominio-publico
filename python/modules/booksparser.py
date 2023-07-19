
# Substitui espaços dos arquivos por "_" e coloca todos os caracteres em letra minúscula.
def fileNameNormalize(inputString):
    # TODO: Substituir posteriormente por regex.
    bookNormalizeText = inputString.replace(" ", "_")
    bookNormalizeText = bookNormalizeText.lower()

    return bookNormalizeText

# Substitui o link do livro para o link de download do arquivo.
def replaceLinkToDownload(url, download_again):
    if (not download_again):
        url = url.replace("DetalheObraForm.do", "DetalheObraDownload.do", 1)
        return url
    
    url = url.replace("http://www.dominiopublico.gov.br/download/texto/", "http://bibliotecacomum.com.br/bc-texto/obras/")
    return url

