from bs4 import BeautifulSoup

soup = BeautifulSoup(open("./Data/DATA/HTML/MyActivity.html"),"html.parser")

print soup.find("p","mdl-typography--title")

print soup.find("div","header-cell mdl-cell mdlcell--12-cd")

##check if the each data set is same: by the time