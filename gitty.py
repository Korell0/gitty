def introduce():
    gitty_name=input("What is my name?  ")
    print('Hello, my name is '+gitty_name)

def add(a,b):
    return a+b

def joke():
    print('\nA husband and wife were dining at a 5-star restaurant. ' +
        'When their food arrived, the husband said:')
    print('- “Our food has arrived! Let’s eat!”')
    print('His wife reminded him:')
    print('- “Honey, you always say your prayers at home before your dinner!”')
    print('Her husband replied:')

    input('\nPress any key to continue\n')

    print('“That’s at home, my dear. Here the chef knows how to cook…”')

def shout():
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')

introduce()
joke()
print(add(5,5))