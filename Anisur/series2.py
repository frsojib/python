# 2+4+6+.....+n

n = int(input('Enter your last Number: '))
sum = 0

for x in range(2,n+1,2):
    sum = sum + x

print(sum)