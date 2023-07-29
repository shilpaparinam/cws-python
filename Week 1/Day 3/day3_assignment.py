"""num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = num1 + num2
print(f"Sum is : {num3}")


km = int(input("Enter value in km: "))
mil = 0.6214 * km
print(f"Miles= {mil}")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
avg = (num1 + num2 + num3) / 3
print(avg)

rup = int(input("Enter rupees: "))
paise = rup * 100
print(paise)

side = int(input("Enter side: "))
area = side**2
print(area)"""


tot_games = int(input("Enter no of games: "))
games_won = int(input("No of games won: "))
games_loss = int(input("No of games loss: "))
games_tie = tot_games - (games_won + games_loss)
points = (games_won * 4) + (games_tie * 2)
print(f"Total matches Tie is: {games_tie}")
print(f"Total points: {points}")
