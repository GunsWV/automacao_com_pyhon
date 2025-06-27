import bs4

exampleFile = open("index3.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")

elems = exampleSoup.select('#autor') #identificador author
sl = exampleSoup.select(".slogan") #classe slogan

print(elems[0]) #imprime o valor de id autor
print(sl) #imrpime o valor da classe slogan 