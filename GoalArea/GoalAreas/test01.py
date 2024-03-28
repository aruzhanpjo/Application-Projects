import pandas

data = pandas.read_csv('GoalArea/GoalAreas/goalAreas.csv')

while True:
    findVal = int(input("How many goal areas do you want to cover? Out of 4.(You can include W and L as well)\n"))
    if findVal <= 3:
        break
    print("Invalid input. Please try again.")

# Get goal areas from user
goalArea = set()
for i in range(findVal):
    val = (input(f"Enter goal area {i + 1}: "))
    goalArea.add(val)

check = data.copy()
for area in goalArea:
    check = check[check['area'].str.contains(area)]
#print(check)

filtered_data = check[['short_name', 'name', 'credits']]

print(filtered_data)
