const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const savedirpath = path.resolve(__dirname, '../json/');

const url = "http://www.dominiopublico.gov.br/pesquisa/ResultadoPesquisaObraForm.do?first=3000&skip=0&ds_titulo=&co_autor=&no_autor=&co_categoria=2&pagina=1&select_action=Submit&co_midia=2&co_obra=&co_idioma=1&colunaOrdenar=NU_PAGE_HITS&ordem=asc";
let globalData;

(async () => {

      const browser = await puppeteer.launch({
        headless: true,
        });

      const page = await browser.newPage();

      await page.goto(url);
      const result = await page.evaluate(() => {
        const table = document.querySelector("table#res").childNodes[3];
        const tablelength = table.childElementCount;
        const data  = [];

        for(let line = 0; line < tablelength; line++) {
    
          let actualLine = table.children[line];
          
          let bookTitle = actualLine?.childNodes[5]?.innerText ?? "";
                    
          let bookLink = actualLine?.childNodes[5]?.children[0]?.href ?? "";
          
          let authorName = actualLine?.childNodes[7]?.innerText ?? "";
      
          let bookFont = actualLine?.childNodes[9]?.innerText ?? "";
      
          let fileType = actualLine?.childNodes[11]?.innerText ?? "";
      
          let fileSize = actualLine?.childNodes[13]?.innerText ?? "";

          let verifyProps = [bookTitle, bookLink, bookFont, authorName, fileSize, fileType];

          if (verifyProps.every(value => { return value != ""; })) {
            data.push(
              {
                "link": bookLink,
                "titulo": bookTitle,
                "autor": authorName,
                "categoria": "literatura",
                "fonte": bookFont,
                "tipo_de_arquivo": fileType,
                "tamanho_do_arquivo": fileSize,
              });
          };
         
        };
        return data;
      });
    globalData = result;

    let json = JSON.stringify(globalData, null, 1);

    if (!fs.existsSync(savedirpath)) { fs.mkdirSync(savedirpath); }

    fs.writeFile(`${savedirpath}/raw_data.json`, json, (err) => {
      if(err) throw err;
      console.log(`saved: ${savedirpath}raw_data.json`);
    });
    
    await browser.close();

  })();
