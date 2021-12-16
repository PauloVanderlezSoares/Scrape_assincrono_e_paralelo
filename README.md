# Scrape_assincrono_e_paralelo
Projeto possui dois arquivos:
- webscreper_async.py:
    Faz o scrape de dados de maneira assíncrona utilizando bibliotecas como asyncio e aiohttp

- webscreper_paralelo.py:
    Faz o scrape de dados utlizando paralelismo, para isso é utilizado a biblioteca multiprocessing

## Como funciona

Em ambos códigos é feito um crawler em páginas do Wikipédia, gerando uma grande quantidade de links para ser acessados e retornando o título de cada página acessada utilizando o BeautifulSoup.

No código webscreper_async.py o scrape das páginas são realizadas utilizando as bibliotecas asyncio e aiohttp, fazendo uso do método de concorrência para otimizar as requests, e os títulos das páginas são retornados usando o método de paralelismo com multiprocessing.

Já no código webscreper_paralelo, o scrape das páginas são realizadas utilizando paralelismo com a biblioteca multiprocessing.
