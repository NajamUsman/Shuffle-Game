example = ['','O','']

print('Welcome to the Shuffle Game!')
print()
print('A list will be generated and then it will be shuffled')
print()
print("Your job is to guess where the item is in the list by guessing an index, the item you're tyring to find is 'O' ")
print()
print('This is the list before shuffling: ', example)
print()


from random import shuffle


def shuffle_list(myList):
    shuffle(myList)
    return myList

result = shuffle_list(example)


def player_guess():
    
    guess = ''
    while guess not in ['0','1','2']:
        guess = int(input("Pick a position 0,1 or 2: "))
    
        if result[guess] == 'O':
            print('correct')
            print(result)
            break
        
        else:
            print('Wrong!')
            print(result)
            break
        
        
player_guess()