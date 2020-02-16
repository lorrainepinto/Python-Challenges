coins = {10: 0, 5: 0, 2: 0, 1: 0}
money = int(input("Enter the amount: "))
print("The min coins required are: ")
for i in coins:
    if money:
        n = money // i
        coins[i] = n
        money = money % i
for key, value in coins.items():
    if(value):
        print(value," ",key,"'s",sep='')
