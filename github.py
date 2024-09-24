from colorama import Fore
import select
import os
import csv
import sys

input("Введите ник")

if select == "User":
    print("Успешно!")
input("Введите пароль")

if select == "Pass":
    print("Пароль подошел запускаю софт!")

#Код был написан наполовину вручную наполовину с гптшкой
Red = Fore.RED
Yellow = Fore.YELLOW
Blue = Fore.BLUE
Green = Fore.GREEN
Reset = Fore.RESET

def display_banner():
    banner_text = '''

 ____    ______  __  __   __  __  ________   __  __  __  __  ______     
/\  _`\ /\  _  \/\ \/\ \ /\ \/\ \/\_____  \ /\ \/\ \/\ \/\ \/\  _  \    
\ \,\L\_\ \ \L\ \ \ \/'/'\ \ \ \ \/____//'/'\ \ \ \ \ \ `\\ \ \ \L\ \   
 \/_\__ \\ \  __ \ \ , <  \ \ \ \ \   //'/'  \ \ \ \ \ \ , ` \ \  __ \  
   /\ \L\ \ \ \/\ \ \ \\`\ \ \ \_\ \ //'/'___ \ \ \_\ \ \ \`\ \ \ \/\ \ 
   \ `\____\ \_\ \_\ \_\ \_\\ \_____\/\_______\\ \_____\ \_\ \_\ \_\ \_\
    \/_____/\/_/\/_/\/_/\/_/ \/_____/\/_______/ \/_____/\/_/\/_/\/_/\/_/
    
  ╔════════════════════════════════════════════════════════════════════╗
  ║ Софт был написан во временна древних Римляней так что не осуждайте ║                                                            
  ╚════════════════════════════════════════════════════════════════════╝     
  ╔════════════════════════════════════════════════════════════════════╗
  ║                         <Введите ваш запрос>                       ║
  ╚════════════════════════════════════════════════════════════════════╝
'''
                                                
                                                
print(f"{Red}{banner_text}{Reset}")

#Аргументы
def get_argument():
    parser = argparse.ArgumentParser(description=dispaly_banner())
    
input(f"{Yellow}Введите запрос{Reset}")

def search_files(query):
    # Путь к папке "data" вы можете поменять название папке просто поменяв нащвание папки в 51-ой строке
    data_dir = os.path.join(os.getcwd(), 'data')

    # Посик по базам в папке "data"
    for filename in os.listdir(data_dir):
        # Проверка формата файлов
        if filename.endswith(('.txt', '.csv', '.xlsx')):
            # Чтение баз
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r') as file:
                for line_num, line in enumerate(file, start=1):
                    # Найдено/Не найдено
                    if query in line:
                        # Есл найдено то
                        print(f"File: {filename}, Line {line_num}: {line.strip()}")

# Пример:
query = '7999999999'
search_files(query)