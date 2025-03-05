import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


file_path = 'iris.xlsx'
excel_file = pd.ExcelFile(file_path)

sheet_num = int(input("Enter the sheet number 1-4 of the dataset to be analyzed:"))
if sheet_num < 1 or sheet_num > 4:
    print("Invalid sheet number. Select from 1 -4")
    exit()

sheet_name = f'Sheet{sheet_num}'
df = pd.read_excel(file_path, sheet_name=sheet_name)

if len(df.columns) < 4:
    print(f"Sheet {sheet_name} does not have enough columns")
    exit()

print(f"\nlength(rows) of dataset: {len(df)}")

print("Columns used in training dataset (explanatory variables): 0 - 3")
print('Target estimation (response variable) data in column: 3 - The "Petal width"')

x = np.array(df[df.columns[1:2]])

y = np.array(df[df.columns[3]])

X_train, X_test, y_train, y_test = train_test_split(x, y , test_size=0.25)

model = LinearRegression()
model.fit(X_train, y_train)

y_predictions = model.predict(X_test)

print("\n\t y_test \t\t y_prediction")
for i in range(0, len(y_predictions), 1):
    print(i, '\t', f'{y_test[i]:.2f}', '\t\t', f'{y_predictions[i]:.2f}')

r2 = r2_score(y_test, y_predictions)

print(f"\nR-squared: {r2:.4f}")

