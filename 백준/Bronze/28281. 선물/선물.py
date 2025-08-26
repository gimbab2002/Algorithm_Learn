import sys
n, x = map(int, input().rstrip().split())
price = list(map(int, input().rstrip().split()))
pay_price = []

for i in range(len(price)-1):
    pay_price.append(price[i]*x + price[i+1]*x)
print(min(pay_price))
