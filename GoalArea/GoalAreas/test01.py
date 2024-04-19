import pandas

data = pandas.read_csv('GoalArea/GoalAreas/goalAreas.csv')

while True:
    findVal = int(input("How many goal areas do you want to cover? Out of 3.(You can include W and L as well)\n"))
    if findVal <= 3:
        break
    print("Invalid input. Please try again.")

# Get goal areas from user
goalArea = set()
for i in range(findVal):
    val = (input(f"Enter goal area {i + 1}: "))
    goalArea.add(val)

#filter the data and find goal areas that match the user input
check = data.copy()
for area in goalArea:
    check = check[check['area'].str.contains(area)]
#print(check)

filtered_data = check[['short_name', 'name', 'credits', 'area']]

if filtered_data.empty == False:
    print(filtered_data)
else:
    print("No classes found. Try different goal areas.")
