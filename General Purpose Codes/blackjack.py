# Blackjack

'''
The deck contains all cards from 2 to 10 inclusive, which are counted according to their value,
also Kings, Queens and Jacks which cost 10 points each and also Aces, which could be counted as 
1 or 11 points, whatever is better.


Each test-case consists of several cards expressed with symbols:
2, 3, 4, 5, 6, 7, 8, 9,
T, J, Q, K - for 10, Jack, Queen, King,
A - for Ace.
'''


# File Parsing

with open('blackjack.txt') as f:
    c = f.readlines()

d = []
for i in c:
    d.append(i.split( ))


for i in d:
    
    count = 0
    for j in i:
        if j in ['2','3','4','5','6','7','8','9']:
            count += int(j)
        elif j == 'T' or j == 'J' or j == 'Q' or j == 'K':
            count += 10
        elif j == 'A':
            if count + 11 <= 21:
                count += 11    # For Ace
            else:
                count += 1
            
    if count <= 21:
        print(count)
    else:
        print('Bust')