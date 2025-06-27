import requests, bs4

res = requests.get("https://books.toscrape.com/")

soup = bs4.BeautifulSoup(res.text, "html.parser")
type(soup)

soup.title.string #carrega o título da página

titulos_livros = [] # lista para armazenar os titulos dos livros

# Itera sobre cada livro encontrado

for livro in soup.select(".product_pod"):
    h3 = livro.find("h3")
    # verifica se o h3 não possui atriubutos "class"
    if not h3.has_attr("class"):
        título = h3.a["title"]
        titulos_livros.append(título)

print(soup.title.string) #carrega o título da página
print(titulos_livros) #exibe todos os títulos dos livros   