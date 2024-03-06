import pandas

data = pandas.read_csv('gen_eds.csv')

while True:
    findVal = int(input("How many goal areas do you want to cover? Out of 3\n"))
    if findVal <= 3:
        break
    print("Invalid input. Please try again.")

# Get goal areas from user
goalArea = []
for i in range(findVal):
    val = (input(f"Enter goal area {i + 1}: "))
    goalArea.append(val)
    
    
def check_goal_areas(row):
    areas = row['area'].split(', ')
    return all(area in areas for area in goalArea)

mask = data.apply(check_goal_areas, axis=1)

# Apply the mask to filter the data
filtered_data = data[mask]

# Select only the 'name' and 'credits' columns
filtered_data = filtered_data[['short_name', 'name', 'credits']]

# Print the filtered data
print("Filtered Classes:")
for index, row in filtered_data.iterrows():
    print(f"({row['short_name']}){row['name']}: {row['credits']} credits")