from multiprocessing import Pool
from requests import get
from bs4 import BeautifulSoup


def wiki_spyder():
    resposta = get('https://pt.wikipedia.org/wiki/Dragonball')
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


def scrape_title(link):
    response = get(link)
    titulo = BeautifulSoup(response.text, 'html5lib').title.text
    print(titulo)


links = wiki_spyder()

if __name__ == "__main__":
    pool = Pool(8)
    pool.map(scrape_title, links)
    pool.terminate()
    pool.join()
