import csv

# Sample data to write to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Jane', 25, 'Los Angeles'],
    ['Doe', 35, 'Chicago']
]

# File path to save the CSV file
csv_file = 'output_file.csv'

# Write data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

print("CSV file generated successfully!")
