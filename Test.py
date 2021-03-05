import sqlite3
import random

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
    print(Show_Backbone())

def Test():
    datas = Show_Backbone()
    datas = random.sample(datas,len(datas))
    for i in datas:
        print("ID: {}".format(i[0]))
        ans = input("Ans: ")
        if ans in ('q','quit','exit'):
            break
        elif ans == i[1]:
            print(f'Your Ans: {ans} Is Correct.')
        else:
            print(f'Your Ans: {ans} Is Wrong.\nCorrect Ans: {i[1]}')

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
            Insert(name,number)
        elif command == '3':
            Test()



Main()