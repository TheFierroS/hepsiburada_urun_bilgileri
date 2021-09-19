import requests
from bs4 import BeautifulSoup

#header kısmına kendi user agentinizi girmeniz gerek yoksa siteden veri çekilmiyor.
header = {"User-Agent":""} #kendi user agentinizi giriniz
link = input("Ürünün Linkini Giriniz -> ")
r = requests.get(link, headers=header)
soup = BeautifulSoup(r.content ,"lxml")
urunad = soup.find("header", {"class":"title-wrapper"}).find("span").text
indirim_yüzdesi = soup.find("div", {"class":"active"}).find("span").text.strip().strip("indirim").strip()
şuanki_fiyat = soup.find("div", {"class":"extra-discount-price"}).text.strip()
ozellikler = soup.find("div", {"id":"productTechSpecContainer"}).find_all("tr")
print("------------------")
print("Ürün Adı -> ",urunad)
print("------------------")
print("Şuanki Fiyatı -> ",şuanki_fiyat)
print("------------------")
print("↓ Ürün Özellikleri ↓")
print("------------------")

for detay in ozellikler:
    etiket = detay.find("th").text
    deger = detay.find("td").text
    print(etiket," = ",deger)
