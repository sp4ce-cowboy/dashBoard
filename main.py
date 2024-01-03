#!/usr/bin/env python3

import os
from time import sleep
import csv
import pandas as pd
import datetime
import shutil
import calendar
screen_col = shutil.get_terminal_size().columns

def start():
    df = pd.read_csv('directives.csv')
    points_e = 0
    weight_e = 0
    directives_e = 0

    for i in range(1, len(df)):
        if df.iat[i,7] == 'Y':
            points_e += df.iat[i,5]
            weight_e += df.iat[i,6]
            directives_e += 1
    
    index_e = round(((points_e/weight_e)*100), 3)
    

    pd.options.display.max_rows = 100
    global screen_col
    screen_col = shutil.get_terminal_size().columns
    
    os.system('clear')
    e = datetime.datetime.now()
 

    print('\n\n','Welcome to Dashboard!'.center(screen_col))
    print(('Day ' + str(e.strftime("%j"))).center(screen_col))
    print(e.strftime("%d %B, %Y").center(screen_col))
    print(e.strftime("%A, %I:%M:%S %p").center(screen_col))
    print(('Critical Index = ' + str(index_e,)).center(screen_col))
    print('\n')

    #print(calendar.month(int(e.strftime("%Y")),int(e.strftime("%m"))))
    
    with open('taskpad.txt', 'r+') as t:
        print('Tasks for today:')
        print(t.read())

    print('  Choose option below:')
    print('    |  ')
    print('    |–– 1: View all Directives')
    print('    |–– 2: View selected Directives')
    print('    |–– 3: View incomplete Directives')
    print('    | ')
    print('    |–– 4: View completed Directives')
    print('    |–– 5: View Statistics')
    print('    |–– 6: Execute Directives')
    print('    | ')
    print('    |–– 7: Reset all Directives')
    print('    |–– 8: Reset daily Directives')
    print('    | ')
    print('    |–– 9: Write to Notepad')
    print('    |–– 10: Read from Notepad')
    print('    | ')
    print('    |–– 11: Update Tasks')
    print('    | ')
    print('    |–– 12: Exit\n')

    
    options_dict = {
        1: viewAll,
        2: viewTime,
        3: inComp,
        4: comp,
        5: Stats,
        6: Execute,
        7: Reset,
        8: partReset,
        9: notePad,
        10: readPad,
        11: taskPad,
        12: exit}
    
    inpu = input()
    option = int(inpu) if inpu.isnumeric() == True else start()
   
    return options_dict[option]() if option in options_dict else start()

def continual():
    print('\n','PRESS ENTER TO CONTINUE'.center(screen_col),'\n')
    option = input().upper()
    if option == '' :
        os.system('clear')
        return start()
    exit()

def viewAll():
    os.system('clear')
    pd.options.display.max_rows = 100
    df = pd.read_csv('directives.csv')
    total = 0
    for i in range(len(df)):
            total += df.iat[i,6]
    print('\nALL DIRECTIVES')

    print(df)
    print('\nTotal weight =',total,'points\n')
    
    return continual()

def viewTime():
    os.system('clear')
    pd.options.display.max_rows = 100
    df = pd.read_csv('directives.csv')

    print('Which directives would you like to see?\n')
    print('M: Morning')
    print('A: All-day')
    print('E: Evening')
    print('R: Repeat')
    print('L: All time-based\n')

    print('N: Entropy')
    print('Q: Quotidian')
    print('T: All type-based\n')

    print('C: CRITICAL\n')

    print('Enter: Return')

    option = input().upper()

    def options(arg):
        
        def optionsContinual():
            print('\nWould you like to see more directives Y/N?\n')
    
            option = input().upper()
            if option == 'Y':
                return viewTime()
            return continual()
        
        dic1 = {
            'M':'Morning',
            'A':'All-Day',
            'E':'Evening',
            'R':'Repeat',
            }
        dic2 = {
            'N':'Entropic',
            'Q':'Quotidian'
        }

        
        if arg in dic1:
            time = dic1[arg]
            df2 = df.query("Time == @time")
        elif arg in dic2:
            time = dic2[arg]
            df2 = df.query("Entropy == @time")
        elif arg == 'X':
            return start()
        elif arg == 'L':
            for i in dic1:
                print('\n{}\n'.format(str(dic1[i]).upper()))
                time = dic1[i]
                df2 = df.query("Time == @time")
                print(df2)
            return optionsContinual()
        elif arg == 'T':
            for i in dic2:
                print('\n{}\n'.format(str(dic2[i]).upper()))
                time = dic2[i]
                df2 = df.query("Entropy == @time")
                print(df2)
            return optionsContinual()
        elif arg == 'C':
            print('CRITICAL')
            df2 = df.query("Crit == 'Y'")
            time = 'CRITICAL'
            
        elif arg == '':
            return start() 
        else:
            return viewTime()
        
        total = sum([df2.iat[i,6] for i in range(len(df2))])
        
        print('\n{} DIRECTIVES\n'.format(time.upper()))
        print('Total Weight =', total, 'points\n' )
        print(df2)

        return optionsContinual()


    return options(str(option))

def inComp():
    df = pd.read_csv('directives.csv')
    total = 0
    df2 = df.query("Points == 0")
    for i in range(len(df2)):
        total += df2.iat[i,6]
    
    print('\nINCOMPLETE DIRECTIVES\n')
    print('Total Weight =', total, 'points\n' )
    
    print(df2)

    return continual()

def comp():
    df = pd.read_csv('directives.csv')
    total = 0
    df2 = df.query("Points != 0")
    for i in range(len(df2)):
        total += df2.iat[i,6]
    
    print('\nCOMPLETED DIRECTIVES\n')
    print('Total Weight =', total, 'points\n' )
    
    print(df2)

    return continual()

def Stats():
    os.system('clear')
    df = pd.read_csv('directives.csv')
    points = 0
    weight = 0
    directives = 0
    
    points_ent = 0
    weight_ent = 0
    directives_ent = 0

    points_q = 0
    weight_q = 0
    directives_q = 0

    points_e = 0
    weight_e = 0
    directives_e = 0

    for i in range(1, len(df)):
        directives +=1
        points += df.iat[i,5]
        weight += df.iat[i,6]

        if df.iat[i,7] == 'Y':
            points_e += df.iat[i,5]
            weight_e += df.iat[i,6]
            directives_e += 1


        if df.iat[i,3] == 'Entropic':
            points_ent += df.iat[i,5]
            weight_ent += df.iat[i,6]
            directives_ent += 1

        elif df.iat[i,3] == 'Quotidian':
            points_q += df.iat[i,5]
            weight_q += df.iat[i,6]
            directives_q += 1
    
    index = round(((points/weight)*100), 3) 
    index_ent = round(((points_ent/weight_ent)*100), 3)
    index_e = round(((points_e/weight_e)*100), 3)
    index_q = round(((points_q/weight_q)*100), 3)

    print('\n\n\n')
    print('\n','     OVERALL INDEX\n')
    print('       Active directives =', directives)
    print('       Current fulfilment =', points)
    print('       Total requirement =', weight)
    print('       Fulfilment ratio =', index,'\n')

    print('\n','     DAILY PERFORMANCE INDEX\n')
    print('       Active directives =', directives_q)
    print('       Current fulfilment =', points_q)
    print('       Total requirement =', weight_q)
    print('       Fulfilment ratio =', index_q,'\n')

    print('\n','     ENTROPY INDEX\n')
    print('       Active directives =', directives_ent)
    print('       Current fulfilment =', points_ent)
    print('       Total requirement =', weight_ent)
    print('       Fulfilment ratio =', index_ent,'\n')

    print('\n','     CRITICAL INDEX\n')
    print('       Active directives =', directives_e)
    print('       Current fulfilment =', points_e)
    print('       Total requirement =', weight_e)
    print('       Fulfilment ratio =', index_e,'\n')

    return continual()
    
def Reset():
    os.system('clear')
    df = pd.read_csv('directives.csv')
    directives = 0
    for i in range(len(df)):
        directives += 1
        df.iat[i,5] = 0
    df.to_csv('directives.csv', index = False)


    print(directives,'directives reset to 0')
    
    return continual()

def partReset():
    os.system('clear')
    df = pd.read_csv('directives.csv')
    directives = 0
    for i in range(len(df)):
        if df.iat[i,3] == 'Quotidian':
            directives += 1
            df.iat[i,5] = 0
    df.to_csv('directives.csv', index = False)

    print(directives,'directives reset to 0')

    return continual()
            
def Execute():
    os.system('clear')
    df = pd.read_csv('directives.csv') 

    print(df, '\n')
    while True:
        try:
            print('Enter DX-ID of directive, Ctrl^D to exit, DO NOT PRESS ENTER:')
            option = str(input())

            if option == '\n':
                continue

            for i in range(len(df)):
                if option in df.iat[i,0]:
                    df.iat[i,5] = df.iat[i,6]
                    print(df.iat[i,0], 'executed')

            df.to_csv('directives.csv', index = False)

        
        except EOFError:
            break

    return continual()

def notePad():
    os.system('clear')
    #enter = '>>>>>>>>>>>>>>>>> Write text below. Ctrl^D to close. <<<<<<<<<<<<<<<<<)
    print('\n',('>>>>>>>>>>>>>>>>> Write text below. Ctrl^D to close. <<<<<<<<<<<<<<<<<').center(screen_col))
    print('------------------------------------------------------------------')
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    #text = input()
    e = datetime.datetime.now()
    timestamp = str(e.strftime("%d %b %y: ")) + str(e.strftime("%a, %I:%M %p"))
    with open ('notepad.txt', 'a') as h:
        h.write('\n\n')
        h.write('>>>>>>>>>>>>>>>>>>>>>> ' + str(timestamp) + ' <<<<<<<<<<<<<<<<<<<<<<')
        h.write('\n')
        for i in contents:
            h.write(i)
            h.write('\n')

    return continual()

def readPad():
    os.system('clear')
    with open ('notepad.txt', 'r') as h:
        print(h.read().center(screen_col))
    
    return continual()

def taskPad():
    os.system('clear')

    def overwrite(contents):
        with open ('taskpad.txt', 'w') as h:
            for i in contents:
                h.write(i)
                h.write('\n')
        return start()

    def append(contents):
        with open ('taskpad.txt', 'a') as h:
            for i in contents:
                h.write(i)
                h.write('\n')
        return start()

    print('Overwrite tasks Y/N?\n')
    option = input().upper()

    print('Write tasks below. Ctrl^D to close.\n')
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    
    if option == 'Y':
        return overwrite(contents)
    else:
        return append(contents)

def status():
    os.system('clear')

    def overwrite(contents):
        with open ('status.txt', 'w') as h:
            for i in contents:
                h.write(i)
                h.write('\n')
        return start()

    def append(contents):
        with open ('status.txt', 'a') as h:
            for i in contents:
                h.write(i)
                h.write('\n')
        return start()

    print('Overwrite STATUS Y/N?\n')
    option = input().upper()

    print('Update STATUS below. Ctrl^D to close.\n')
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    
    if option == 'Y':
        return overwrite(contents)
    else:
        return append(contents)

start()
