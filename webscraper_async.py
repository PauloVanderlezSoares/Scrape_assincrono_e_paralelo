import aiohttp
import asyncio
from bs4 import BeautifulSoup
from requests import get
from time import time
from multiprocessing import Pool


async def get_pagina(session, url):
    async with session.get(url) as page:
        return await page.text()


async def scraper(session, urls_list):
    tasks = []
    for url in urls_list:
        task = asyncio.create_task(get_pagina(session, url))
        tasks.append(task)

    resultado = await asyncio.gather(*tasks)
    return resultado


async def main(urls_list):
    async with aiohttp.ClientSession() as session:
        dados_site = await scraper(session, urls_list)

        return dados_site


def wiki_spyder():
    resposta = get('https://pt.wikipedia.org/wiki/Python')
    tags = BeautifulSoup(resposta.text, 'html5lib')
    allLinks = tags.find("html").find_all("a")
    lista_links = []
    for link in allLinks:
        x = str(link).split(" ")
        for y in x:
            if 'href' and '/wiki/' in y:
                lista_links.append(y)

    lista_wiki = []
    for link in lista_links:
        link = link.split('"')
        for link_valido in link:
            if "/wiki/" in link_valido:
                lista_wiki.append(link_valido)

    lista_links.clear()
    for link in lista_wiki:
        if "https" in link:
            lista_links.append(link)
        else:
            link_completo = "https://pt.wikipedia.org" + link
            lista_links.append(link_completo)

    return lista_links


def title(html):
    soup = BeautifulSoup(html, 'html5lib')
    print(soup.title.text)


if __name__ == '__main__':
    urls = wiki_spyder()
    inicio = time()
    resultado = asyncio.run(main(urls))
    print(f"Total de páginas visitadas: {len(resultado)}")
    print(f"Tempo total: {time() - inicio} segundos\n")

    p = Pool(2)
    p.map(title, resultado)
    p.terminate()
    p.join()
