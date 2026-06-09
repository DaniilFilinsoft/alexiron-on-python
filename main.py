#--------------------------------------#
#                                      #
# Александр Железкин 2.0 Python-версия #
#                       от OwlPrograms #
#                                      #
#--------------------------------------#
# цепь маркова для генерации текста    #
# версия 2.0.1                         #
#--------------------------------------#
# изменение: подкрутил менюшку и доба- #
# вил копирование текста               #
#--------------------------------------#

### ПЕРЕМЕННЫЕ

global chain
global gen1

### ИМПОРТ БИБЛИОТЕК

import random as rm
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
try:
    import pyperclip
except:
    messagebox.showerror("Александр Железкин", "Не удаётся использовать библиотеку pyperclip. Докачай её с помощью pip install pyperclip в папке где у тебя установлен питон/Scripts")

### НАСТРОЙКА ОКНА

root = Tk()
root.title("Александр Железкин")

window_width = 550
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('./ailogo.ico')

### ФУНКЦИИ

def choice(inputs): # Делает выбор между вероятностями
    
    inputs.pop(0) # убираем первый элемент
    
    choice = rm.randint(1,100) # случайное число
    choice_builder = choice
    
    addit1 = 0 # для цикла
    for d in range(len(inputs)):
        if int(choice_builder) < int(inputs[d]) + int(addit1): # если число в диапазоне
            return d+1
        else: addit1 += inputs[d]
    return choice(inputs) # рекурсия

def find(lst, item, n): # найти n-нное появление элемента в списке
    
    count = 0
    for index, value in enumerate(lst): # интересно как это работает
        if value == item:
            count += 1
            if count == n:
                return index
            
    return -1 # на случай если элемент в списке отсутствует

def say(input_list, length): # Сгенерировать текст по данной цепи
    
    wordn = rm.randint(0,len(list(input_list))-1) # выбирается слово, с которого начинается построение текста
    answer = [input_list[wordn].get("_word")] # добавление его в ответ
    
    for a in range(length): # цикл генерации
        
        wordnlist = input_list[wordn] # данные слова
        w2 = input_list[wordn] # что это зачем
        nextword = choice(list(wordnlist.values())) 
        nextword_str = w2.get("_word") # выбранное слово
        
        for b in range(len(input_list)): # цикл для поиска выбранного слова чтоб от него выбирать другие
            if input_list[b].get("_word") == list(wordnlist.keys())[nextword]:
                wordn = b
                break
        answer.append(input_list[wordn].get("_word")) # добавление 
        
    return answer

def waw(wordS, listS): # Я забыл что это
    countW = listS.count(wordS)
    answer = []
    for e in range(countW):
        if find(listS,wordS,e+1)+1 < len(listS):
            answer.append(listS[find(listS,wordS,e+1)+1])
    return answer

def calcprob(listP): # Вычислить частоту появления слов
    blockWords = [] # слова уже прощитанные
    answer = []
    for f in range(len(listP)): # поиск
        if not listP[f] in blockWords:
            timesApp = listP.count(listP[f])
            answer.append({listP[f]:round((100/len(listP))*timesApp)}) # формула появления слов
    return answer

def gen(inp_str): # Генерация цепей / Главная тареллка спаггети или как это слово пишется ёперный театр
    wb = []
    chain = []
    for g in range(len(inp_str.split(" "))): # для всех слов:
        if not inp_str.split(" ")[g] in wb: # если слово не было обработанно:
            chainpart = [{"_word":inp_str.split(" ")[g]}] # слава тебе господи оно всё работает (через раз но сути не меняет)
            for h in range(len(calcprob(waw(inp_str.split(" ")[g],inp_str.split(" "))))):
                chainpart.append(calcprob(waw(inp_str.split(" ")[g],inp_str.split(" ")))[h-1])
            chainpart1 = {}
            for i in range(len(chainpart)):
                chainpart1 = chainpart1|chainpart[i]
            chain.append(chainpart1)
            wb.append(inp_str.split(" ")[g])
    return chain

def norm(inp_list): # Нормализатор списков в текст

    answer = "" 
    
    for a in range(len(inp_list)):

        if inp_list[a] != "'" and inp_list[a] != "[" and inp_list[a] != "]" and inp_list[a] != ",":
            
            answer = answer+inp_list[a]

    return answer

### ФУНКЦИОНАЛ

chain = gen("привет всем вы на канале анука давайка и всем привет вы соверма сво сво вы привет")

answerr = tk.Label(root, text="Здесь появится результат генерации текста", fg="green", bg="yellow")
answerr.pack()

def action3():
    pyperclip.copy(gen1)

buttonc = tk.Button( 
   text="Скопировать генерацию",
   command=action3
)
buttonc.pack()

new_chain = ""

def action(): # Генерация текста

    global gen1
    gen1 = norm(str(say(chain,rm.randint(5,10))))
    answerr.config(text=gen1)

button = tk.Button( 
   text="Сгенерировать!",
   command=action
)
button.pack()

changer = tk.Entry(root,textvariable = new_chain,width=80)
changer.pack()

def action2():
    global chain
    new_chain = changer.get()
    chain = gen(new_chain)

change = tk.Button( 
   text="Поменять текст с которого генерации",
   command=action2
)
change.pack()

#print(say([{"_word":"privet","vsem":50,"dane":50},{"_word":"vsem","privet":100},{"_word":"dane","vsem":100}],8))

#print(chain)
#print(say(chain,8))

message = tk.Label(root, text="Александр Железкин 2.0 Python от OwlPrograms (2.0.1)", bg="blue", fg="white")
message.pack(side="bottom")

root.mainloop() # Запуск приложения
