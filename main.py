n = int(input())
count = 0
num = 101
while count < n:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        if count == n - 1:
            print(num, end="")
        else:
            print(num, end=",")
        count = count + 1
    num = num + 1
