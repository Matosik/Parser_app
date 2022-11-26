import requests
from bs4 import BeautifulSoup as bs
import os
from time import sleep
import create_dataset as cd #создание папки
import Parserapp as mainParser #главное окно приложения
import sys


headers = {"Accept": "*/*","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

def parser(page:str, query,path_folder ,amount=10):
    print("НАЧАЛИ ПАРСИТЬ")
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
    return None

def push_request():
    global request
    global check_request
    if(len(ui.name_reqeust.text())==0):
        msg = mainParser.QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("Запрос не может быть пустым!")
        msg.setIcon(mainParser.QMessageBox.Warning)
        msg.exec_()
        check_request=False
    else:
        request=ui.name_reqeust.text()
        check_request=True
        print("УРА")

def push_path():
    global path
    global check_path
    if(os.path.exists(ui.full_path.text())==False):
        msg = mainParser.QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("Неверный путь!")
        msg.setIcon(mainParser.QMessageBox.Warning)
        msg.exec_()
        check_path=False
    else:
        path=ui.full_path.text()
        check_path=True
        print("УРА")

def push_folder():
    global folder
    global check_folder
    if(len(ui.name_folder.text())==0):
        msg = mainParser.QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("Папку нужно как то назвать!")
        msg.setIcon(mainParser.QMessageBox.Warning)
        msg.exec_()
        check_folder=False
    else:
        check_folder=True
        folder=ui.name_folder.text()
        print("УРА")


def start():
    if(check_folder==False):
        msg = mainParser.QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("Сперва нужно как то назвать папку!")
        msg.setIcon(mainParser.QMessageBox.Warning)
        msg.exec_()
    elif(check_request==False):
        msg = mainParser.QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("Нужно написать запрос!")
        msg.setIcon(mainParser.QMessageBox.Warning)
        msg.exec_()
    else:
        if(check_path==False):
            page=10
            pf=cd.make_folder(folder)
            parser(page,request,pf)
        else:
            page=10
            pf=cd.make_folder(folder,path)
            parser(page,request,pf)


if (__name__== "__main__"):
    global check_path
    global check_folder
    global check_request
    check_request=False
    check_path=False
    check_folder=False
    #==================================================#
    app = mainParser.QtWidgets.QApplication(sys.argv)  #
    Application = mainParser.QtWidgets.QMainWindow()   #
    ui = mainParser.Ui_parser()                        #
    ui.setupUi(Application)   
    #ui.setWindowsTitle("Парсер картинок")
    ui.name_reqeust.setPlaceholderText("запрос")
    ui.full_path.setPlaceholderText(os.getcwd())
    ui.name_folder.setPlaceholderText("имя для папки")                         #
    Application.show()                                 #
    #==================================================#
    ui.take_request.clicked.connect(push_request)
    ui.take_the_path.clicked.connect(push_path)
    ui.take_folder.clicked.connect(push_folder)
    ui.start_parsing.clicked.connect(start)

    sys.exit(app.exec_())   
    



