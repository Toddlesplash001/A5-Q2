n = int(input("Enter the given number " ))
r = int(input("Enter the range "))
divisors = []
for i in range(1,r):
    if n % i == 0:
        divisors.append(i)
print(divisors)
