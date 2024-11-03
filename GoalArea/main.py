import os
import mysql.connector
import pandas as pd

# Get environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Establish connection to MySQL database
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# Create a cursor to execute SQL queries
cursor = connection.cursor(dictionary=True)

while True:
    findVal = int(input("How many goal areas do you want to cover? Out of 3. (You can include W and L as well)\n"))
    if findVal <= 3:
        break
    print("Invalid input. Please try again.")

# Get goal areas from user
goalArea = set()
for i in range(findVal):
    val = input(f"Enter goal area {i + 1}: ")
    goalArea.add(val)

# Initialize conditions for SQL query
goalArea_conditions = []
contains_w_condition = ""

# Check if 'W' is in the goal areas
if 'W' in goalArea:
    contains_w_condition = "contains_W = 1"

# Build the SQL query conditions
for area in goalArea:
    if area != 'W':  # Exclude 'W' from area conditions
        goalArea_conditions.append(f"area LIKE '%{area}%'")

# Combine conditions
if contains_w_condition:
    # If 'W' is included, ensure that the area condition also applies
    query_conditions = " AND ".join(goalArea_conditions + [contains_w_condition])
else:
    # If 'W' is not included, just use the area conditions
    query_conditions = " OR ".join(goalArea_conditions)

# Prepare the final query
if query_conditions:
    query = f"""
    SELECT short_name, name, credits, area
    FROM goalAreasDataBase
    WHERE {query_conditions};
    """
else:
    query = "SELECT short_name, name, credits, area FROM goalAreasDataBase;"

# Execute the SQL query
cursor.execute(query)

# Fetch the results
filtered_data = cursor.fetchall()

# Convert results to a DataFrame
df = pd.DataFrame(filtered_data)

# Check if results are found and print in a table-like manner
if not df.empty:
    print(df)  # This prints the DataFrame in a table format
else:
    print("No classes found. Try different goal areas.")

# Close the connection
cursor.close()
connection.close()