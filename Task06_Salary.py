numbers_of_tab = int(input())
salary = float(input())

for i in range(1, numbers_of_tab + 1):
    next_tab = input()
    if next_tab == "Facebook":
        salary -= 150
    elif next_tab == "Instagram":
        salary -= 100
    elif next_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(int(salary))
