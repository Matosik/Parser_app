import os


def make_folder(name, path=os.getcwd()):
    if(os.path.exists(f"{path}/{name}")):
        print("папка есть")
    else:
        os.mkdir(f"{path}/{name}")
        print(f"cоздаем папку с именем {name}")
    return f"{path}\{name}"

