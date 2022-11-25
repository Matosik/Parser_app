import requests
from bs4 import BeautifulSoup as bs
import os
from time import sleep
import create_dataset as cd

headers = {"Accept": "*/*","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

def parser(page, query,path_folder ,amount=100):
    counter_img=0
    while(counter_img<amount):
        sleep(0.46)
        counter_locale=0
        i=0
        url=f"https://yandex.ru/images/search?p=10&text={query}={page}&rpt=image"
        r=requests.get(url,headers)
        page+=10
        soup=bs(r.text,"lxml")
        img_url=soup.findAll("img", class_="serp-item__thumb justifier__thumb")
        lena=len(img_url)
        while(counter_img<amount)and(counter_locale<lena):
            if(i>=len(img_url)):
                break
            sleep(0.54)
            img="https:"+ img_url[i].get("src")
            with open(f"{path_folder}/{counter_img}.jpg","wb") as file:
                file.write(requests.get(img).content)
                print(f"====Download file {counter_img} ==== ")
                counter_img+=1
                counter_locale+=1
            i+=1




if (__name__== "__main__"):
    page=10
    request=input("введите какие картинки хотите найти: ")
    amount=int(input("Введите количество картинок: "))
    name_folder=input("Введите название папки: ")

    #path=input("Введите путь для папки")
    path="C:/Users/79093/Desktop"

    pf=cd.make_folder(name_folder,path)
    parser(page,request,pf,amount)



