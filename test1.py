import sqlite3
import random
import time
from threading import Thread

conn = sqlite3.connect('Data/Knowleage.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Know(Name TEXT,Ans TEXT)')

def Insert(name,number):
    c.execute('INSERT INTO Know(Name,Ans) VALUES(?,?)',(name,number))
    conn.commit()

def Show_Backbone():
    Datas = c.execute('SELECT * FROM Know')
    contents = []
    for data in Datas:
        contents.append(data)
    return contents

def Show():
    for i in Show_Backbone():
        print(i)

def Test():
    datas = Show_Backbone()
    datas = random.sample(datas,len(datas))
    for i in datas:
        print("ID: {}".format(i[0]))
        ans = None
        def check():
            time.sleep(2)
            if ans != None:
                return
            print('Too Slow')
        Thread(target= check).start()
        ans = input('Your Ans: ')
        if ans in ('q','quit','exit'):
            break
        elif ans == i[1]:
            print(f'Your Ans: {ans} Is Correct.')
        else:
            print(f'Your Ans: {ans} Is Wrong.\nCorrect Ans: {i[1]}')

def Present(value):
    datas = Show_Backbone()
    for i in datas:
        if i[1] == value:
            return True
            
def Main():
    while True:
        print('Action: \n1.SHOW\n2.INSERT\n3.TEST')
        command = input('PUT YOUR COMMAND: ')

        if command.lower() in ('q','quit','exit'):
            break
        elif command == '1':
            Show()
        elif command == '2':
            name = input('PUT NAME: ')
            number = input("PUT NUMBER: ")
            if Present(number) == True:
                print('Entry Already Exists.')
            else:
                Insert(name,number)
        elif command == '3':
            Test()



Main()