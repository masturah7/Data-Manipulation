import numpy as np

# Open the CSV file and assign the result to a variable
file = open("loan_data.csv")

# Load the data into a NumPy array using comma as the delimiter
data = np.genfromtxt(file, delimiter=",", skip_header=1)

# Be sure to close the file after reading
file.close()

# Column 4 (0-based) holds the total price / loan amount
loan_amounts = data[:, 4]

# Basic statistical analysis of the loan amounts
print("Mean of loan amounts:", np.mean(loan_amounts))
print("Median of loan amounts:", np.median(loan_amounts))
print("Standard deviation of loan amounts:", np.std(loan_amounts))

