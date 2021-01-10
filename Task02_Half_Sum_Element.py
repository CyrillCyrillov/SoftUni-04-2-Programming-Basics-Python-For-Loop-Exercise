import sys
n = int(input())
sum = 0
max_number = -sys.maxsize

for i in range(1, n+1):
    next =int(input())
    sum += next
    if next >= max_number:
        max_number = next

if sum - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (sum - max_number))}")
