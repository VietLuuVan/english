import random
import time
import os

def create_section(word_list):
    section = input('create section: ')
    path = 'C:\\Users\\VTO\\Documents\\english\\section_'+'section'+'.txt'
    f = open(path, "w", encoding='utf_8')
    for i in word_list.keys():
        f.write(i.lower() + ": " + word_list.get(i) + "\n")
    f.close()

from functools import cmp_to_key   
def get_available_section():
    list_file = os.listdir('C:\\Users\\VTO\\Documents\\english')
    print('All available section: ')
    list_section = []
    
    for i in list_file:
        if '.txt' in i:
            list_section.append(i)
    
    list_section.sort(key = cmp_to_key(compare_section))
    for i in list_section:
        print(i[0:-4])
    return list_section

def compare_section(x, y):
    x = int(x[8:-4])
    y = int(y[8:-4])
    if x > y:
        return 1
    elif x < y:
        return -1
    return 0
    
def get_list(section):
    path = 'C:\\Users\\VTO\\Documents\\english\\section_' + str(section) + '.txt'
    words = {}
    try:
        f = open(path, "r", encoding='utf_8')
    except:
        print(f'section {section} has not been created yet')
        return
    for line in f:
        word = line.strip().split(': ')
        words[word[0]] = word[1]
    return words
         
def learn(words):
    list_words = list(words.keys())
    maximum = len(list_words)
    n = int(input(f'Choose number of words you want to test (max:{maximum}): '))
    test = random.sample(list_words,k = n)
    mark = 0
    wrong_answer = []
    for i in range(n):
        answer = input(str(i+1)+'. '+words.get(test[i])+': ')
        if (answer == test[i].lower()):
            print('Correct!')
            mark += 1
        else:
            print('Incorrect! The correct word is:',test[i])
            wrong_answer.append(test[i])
    print('\nprocessing...\n') 
    time.sleep(1)   
    print(f'Your mark is {mark}/{n}')
    if (mark != n):
        print('You should learn these words carefully:')
        for i in range(len(wrong_answer)):
            print(str(i+1)+'. '+wrong_answer[i]+': '+words.get(wrong_answer[i]))
            
f = open('C:\\Users\\VTO\\Documents\\english\\section_11.txt', "r", encoding='utf_8')

def learn_all():
    list_section = get_available_section()
    words ={}
    for i in list_section:
        j = int(i[8:-4])
        words.update(get_list(j))
    learn(words)
    
def learn_section(n):
    words = get_list(int(n))
    learn(words)     
       
def main(): 
    get_available_section()
    while (1):
        n = input('Choose section you want to learn or all if you want to test all sections: ')
        if n == 'all':
            learn_all()
        else:
           learn_section(n)
        print('---------------------------------------------------')
        choice = input('Choose C to continue or Q to quit: ')
        if choice == 'Q':
            break
        print('---------------------------------------------------')
        
        
if __name__ == "__main__":
    main()