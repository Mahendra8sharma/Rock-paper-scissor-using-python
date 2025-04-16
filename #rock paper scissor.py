import random

emojis = {'r':'🪨','s':'✂️','p':'📜'}
choices = ('r','p','s')

while True:
    user_choice = input('Rock,paper or scissors? (r/p/s): ').lower()
if user_choice not in choices:
    print('Invalid choice!')
    continue

computer_choice = random.choice(choices)

print(f'you chose {emojis(user_choice)}')
print(f' computer chose {emojis(computer_choice)}') 

if user_choice==computer_choice:
    print('Tie!')
    




