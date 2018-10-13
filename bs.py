import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

gs_url = 'https://www.guitarcenter.com/Semi-Hollow-and-Hollow-Body-Electric-Guitars.gc#pageName=subcategory-page&N=18147+1076&Nao=0&recsPerPage=30&postalCode=97420&radius=100&profileCountryCode=US&profileCurrencyCode=USD'
sw_url = "https://www.sweetwater.com/c591--6-string_Hollowbody_Guitars"
rv_url = "https://reverb.com/marketplace/electric-guitars/hollow-body?on_sale=true"
uClient = uReq(gs_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
prod_list = page_soup.findAll("div", {"class": "product"})

for container in prod_list:
    details_container = container.findAll("div", {"class": "productDetails"})
    title = container.findAll("div", {"class": "productTitle"})
    price = container.findAll("div", {"class":"priceContainer mainPrice"})
    print(title[0].text.strip() + price[0].text.strip() + "\n")
uClient = uReq(rv_url)
page_html = uClient.read()
uClient.close()

page_soup2 = soup(page_html, "html.parser")
prod_list2 = page_soup2.findAll("div", {"class": "product"})
print(prod_list2)
