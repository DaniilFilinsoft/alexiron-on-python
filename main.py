print("Запуск Железка 2.0 Python...")

import random as rm
from tkinter import *
import tkinter as tk
import time

root = Tk()
root.title("Александр Железкин")

window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('./ailogo.ico')

def choice(inputs):
    inputs.pop(0)
    print(inputs)
    choice = rm.randint(1,100)
    choice_builder = choice
    addit1 = 0
    for d in range(len(inputs)):
        if int(choice_builder) < int(inputs[d]) + int(addit1):
            return d+1
        else: addit1 += inputs[d]
    return choice(inputs)

def find(lst, item, n):
    count = 0
    for index, value in enumerate(lst):
        if value == item:
            count += 1
            if count == n:
                return index
    return -1

def say(input_list, length):
    print(input_list,"input list 2 say")
    wordn = rm.randint(0,len(list(input_list))-1)
    print(input_list[wordn],"wordn")
    answer = [input_list[wordn].get("_word")]
    for a in range(length):
        wordnlist = input_list[wordn]
        w2 = input_list[wordn]
        nextword = choice(list(wordnlist.values()))
        print(nextword)
        nextword_str = w2.get("_word")
        print(nextword_str)
        for b in range(len(input_list)):
            print(input_list[b].get("_word"),"ybub")
            print(list(wordnlist.keys())[nextword],"nextword")
            if input_list[b].get("_word") == list(wordnlist.keys())[nextword]:
                wordn = b
                print(b,"b")
                break
        answer.append(input_list[wordn].get("_word"))
    return answer

def waw(wordS, listS):
    countW = listS.count(wordS)
    answer = []
    for e in range(countW):
        print(listS)
        if find(listS,wordS,e+1)+1 < len(listS):
            print(find(listS,wordS,e+1)+1)
            answer.append(listS[find(listS,wordS,e+1)+1])
    return answer

def calcprob(listP):
    blockWords = []
    answer = []
    for f in range(len(listP)):
        if not listP[f] in blockWords:
            timesApp = listP.count(listP[f])
            answer.append({listP[f]:round((100/len(listP))*timesApp)})
    return answer

def gen(inp_str):
    wb = []
    chain = []
    for g in range(len(inp_str.split(" "))):
        if not inp_str.split(" ")[g] in wb:
            print(inp_str.split(" "),"inp str split")
            print(inp_str.split(" ")[g],"inp str split symbol")
            print(1,"")
            print(waw(inp_str.split(" ")[g] , list(inp_str.split(" "))),"слова после слова",inp_str.split(" ")[g])
            chainpart = [{"_word":inp_str.split(" ")[g]}]
            for h in range(len(calcprob(waw(inp_str.split(" ")[g],inp_str.split(" "))))):
                chainpart.append(calcprob(waw(inp_str.split(" ")[g],inp_str.split(" ")))[h-1])
            chainpart1 = {}
            for i in range(len(chainpart)):
                chainpart1 = chainpart1|chainpart[i]
            chain.append(chainpart1)
            print(chain,"chain")
            wb.append(inp_str.split(" ")[g])
    return chain

print("СЕЙЧАС БУДЕТ ЗАГРУЗКА! ТАК И ДОЛЖНО БЫТЬ!")
time.sleep(3)
chain = gen("привет всем вы на канале анука давайка и всем привет вы соверма сво сво вы привет")

answerr = tk.Label(root, text="Тут появится результат генерации")
answerr.pack()

def action():
    print("генерируем...")
    answerr.config(text=str(say(chain,8)))
    
button = tk.Button( 
   text="Сгенерировать",
   command=action
)
button.pack()

#print(say([{"_word":"privet","vsem":50,"dane":50},{"_word":"vsem","privet":100},{"_word":"dane","vsem":100}],8))

#print(chain)
#print(say(chain,8))

message = tk.Label(root, text="Александр Железкин 2.0 Python от OwlProgramms")
message.pack()

root.mainloop()
