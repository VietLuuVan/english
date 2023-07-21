import random
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
            
    print(f'Your mark is {mark}/{n}')
    if (mark != n):
        print('You should learn these words carefully:')
        for i in range(len(wrong_answer)):
            print(str(i+1)+'. '+wrong_answer[i]+': '+words.get(wrong_answer[i]))
            
f = open('C:\\Users\\VTO\\Documents\\english\\section_11.txt', "r", encoding='utf_8')

def get_list(section):
    path = 'C:\\Users\\VTO\\Documents\\english\\section_' + str(section) + '.txt'
    words = {}
    f = open(path, "r", encoding='utf_8')
    for line in f:
        word = line.strip().split(': ')
        words[word[0]] = word[1]
    return words
    
while (1):
    try:
        n = int(input('Choose section you want to learn: '))
    except:
        break
    words = get_list(n)
    learn(words)
    
