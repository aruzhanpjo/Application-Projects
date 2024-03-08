import pandas

data = pandas.read_csv('GoalArea/GoalAreas/gen_eds.csv')

while True:
    findVal = int(input("How many goal areas do you want to cover? Out of 3\n"))
    if findVal <= 3:
        break
    print("Invalid input. Please try again.")

# Get goal areas from user
goalArea = set()
for i in range(findVal):
    val = (input(f"Enter goal area {i + 1}: "))
    goalArea.add(val)
    
    
def check_goal_areas(row):
    areas = set(row['area'].split(', '))
    return goalArea.issubset(areas)

filtered_data = []

for index, row in data.iterrows():
    if check_goal_areas(row):
        filtered_data.append(row)
        
filtered_data = pandas.DataFrame(filtered_data)

try:  
    filtered_data = filtered_data[['short_name', 'name', 'credits']]
except:
    print("There are no classes that satisfy those goal areas. Try different combinations")
    exit()

# Print the filtered data
print("Filtered Classes:")
for index, row in filtered_data.iterrows():
    print(f"({row['short_name']}){row['name']}: {row['credits']} credits")