# Scraping Dominio Publico (Gov Brasil)

Tools for scraping data and files from the [Public Domain (gov BR)](http://www.dominiopublico.gov.br/).

![badge-js] ![badge-python] ![badge-shellscript] 

[badge-python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[badge-js]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[badge-shellscript]: https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white

## Dependencies:

- Python 3.11+
- NodeJS 19+
- A Linux bash environment (if you want to use the script).


## How to use

Run the file **"run.sh"** in a bash terminal and choose an option. Alternatively, if you want to execute it directly, include the option number as an argument.

Run the script with the menu to choose an option:

```sh
./run.sh
```

Run the script with the option already included:

```sh
# In this case, the option "1" from the menu
./run.sh 1
```

The scraping data is stored in the "json" directory with the name "raw_data.json", and the downloaded book files are saved in the "booklibrary" directory. It is necessary to perform the scraping of the data first before running the script to download them.
