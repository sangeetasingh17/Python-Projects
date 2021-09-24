import random


def win(comp, user):

    if comp == user:  # tie
        return None

    elif comp == 'r':
        if user == 'p':
            return False
        else:
            return True

    elif comp == 'p':
        if user == 's':
            return False
        else:
            return True

    else:
        if user == 'r':
            return False
        else:
            return True


num = random.randint(1, 3)
if num == 1:
    comp = 'r'
elif num == 2:
    comp = 's'
else:
    comp = 's'

user = input("Rock(r) Paper(p) Scissors(s) -> ")
result = win(comp, user)

print("Computer chose", comp)
print("You chose", user)

if result == None:
    print("The game is a tie!")
elif result:
    print("You Won!")
else:
    print("You Lost!")
