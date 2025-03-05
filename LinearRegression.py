import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# File path to the dataset
file_path = 'iris.xlsx'
excel_file = pd.ExcelFile(file_path)

# Ask user for which sheet to analyze
sheet_num = int(input("Enter the sheet number 1-4 of the dataset to be analyzed:"))
if sheet_num < 1 or sheet_num > 4:
    print("Invalid sheet number. Select from 1 -4")
    exit()

# Translate user input into actual sheet name
sheet_name = f'Sheet{sheet_num}'

# Load the selected sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Check if the sheet has enough columns for the regression at least 4
if len(df.columns) < 4:
    print(f"Sheet {sheet_name} does not have enough columns")
    exit()

# Report number of rows in the dataset
print(f"\nlength(rows) of dataset: {len(df)}")

# Prints what the columns are used
print("Columns used in training dataset (explanatory variables): 2 - 3")
print('Target estimation (response variable) data in column: 3 - The "Petal width"')

# Extract explanatory variable
x = np.array(df[df.columns[0:3]])

# Extract response variable (y) - Column 3 (Petal Width)
y = np.array(df[df.columns[3]])

# Split data into training and test sets1
X_train, X_test, y_train, y_test = train_test_split(x, y , test_size=0.25)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Model to predict y values for the test set
y_predictions = model.predict(X_test)

# Display y_test and corresponding predictions side-by-side
print("\n\t y_test \t\t y_prediction")

for i in range(0, len(y_predictions), 1):
    print(i, '\t', f'{y_test[i]:.2f}', '\t\t', f'{y_predictions[i]:.2f}')
# Compute and display R-squared (coefficient of determination)
r2 = r2_score(y_test, y_predictions)

print(f"\nR-squared: {r2:.4f}")

