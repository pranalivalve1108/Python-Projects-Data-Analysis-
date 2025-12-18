import csv
import numpy as np

values = [120, 150, 180, 200, 160]

# Create and write to CSV file
with open("numbers.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["values"])

    # Write multiple rows (single column)
    for value in values:
        writer.writerow([value])

# Read CSV file
with open("F:\\Python_Practice\\Python_Practice_Project\\numbers.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        values.append(int(row["values"]))

# Convert to NumPy array
values_np = np.array(values)

# Analysis using NumPy
print("Values:", values_np)
print("Total:", np.sum(values_np))
print("Average:", np.mean(values_np))
print("Maximum:", np.max(values_np))
print("Minimum:", np.min(values_np))

