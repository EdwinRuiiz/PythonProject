import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read in the ‘iris.xlsx’ dataset
file_path = "iris.xlsx"
sheet_one = "Sheet1"
df = pd.read_excel(file_path, sheet_name=sheet_one)  # Read the first sheet

# Display specific rows, columns, and cells
def display_data():
    print("\nDisplaying the first 5 rows of the dataset:\n", df.head().to_string(index=False))

display_data()

# Step 2.1: Search the data content by row and column numbers
def search_by_index():
    try:
        row_index = int(input("\nEnter the row (0-149) of the dataset: "))
        column_index = int(input("\nEnter the column (0) of the dataset: "))

        # Validate row and column numbers
        if 0 <= row_index < len(df) and 0 <= column_index < len(df.columns):
            print(f"\nValue at row {row_index}, column {column_index}: {df.iloc[row_index, column_index]}")
        else:
            print("\nError: Row or column number is out of range.")
    except ValueError:
        print("\nError: Please enter valid integer values.")

 # Call function to allow user input
search_by_index()

# Step 2.2: Search for a specific value and replace it
try:
    search_value = float(input("\nEnter a value to search for (0.0-10.0): "))

    if not (0.0 <= search_value <= 10.0):
        print("\nError: The number must be between 0.0 and 10.0.")
        exit()

    numeric_df = df.select_dtypes(include=['number'])
    matches = numeric_df == search_value
    count_occurrences = matches.sum().sum()

    if count_occurrences > 0:
        rand = random.randint(100,999)
        replace_value = rand
        occurrences = list(zip(*np.where(matches.values)))

        for row, col in occurrences:
            df.iloc[row, df.columns.get_loc(numeric_df.columns[col])] = replace_value

        print("\nReplacements made:")
        for i, (row, col) in enumerate(occurrences, start=1):
            print(
                f"{i}. Found {search_value} at (Row {row}, Column '{numeric_df.columns[col]}') → Replaced with {replace_value}")

        print(f"\nTotal occurrences replaced: {count_occurrences}")

    else:
        print(f"\nThe value '{search_value}' was not found in the dataset.")

except ValueError:
    print("\nError: Please enter a valid number.")


# Step 2.3: Output the modified dataset to a new Excel file
output_file = "modified_iris.xlsx"
df = df.applymap(lambda x: pd.to_numeric(x, errors="ignore"))

writer = pd.ExcelWriter(output_file, engine="openpyxl")

df.to_excel(writer,sheet_name="Sheet1",index=False)

writer.close()
print(f"\nModified dataset saved as '{output_file}.'")
# Step 3.1: Compute basic statistical parameters
excel_file =pd.ExcelFile(file_path)

sheets = excel_file.sheet_names

while True:
    try:
        sheet_num = int(input("\nEnter the sheet number (range 1 - 4) of the dataset to be analyzed: "))
        if 1 <= sheet_num <= len(sheets):
            sheet_name = sheets[sheet_num - 1]  # Convert user input (1-based) to 0-based index
            break
        else:
            print("\nError: Please enter a number between 1 and 4.")
    except ValueError:
        print("\nError: Please enter a valid numeric sheet number.")
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Filter numeric columns
numeric_df = df.select_dtypes(include=['number'])

print(f"\nThe length (rows) of dataset in {sheet_name}: {len(df)}\n")

mean_values = numeric_df.mean()
median_values = numeric_df.median()
std_values = numeric_df.std()
var_values = numeric_df.var()
corr_values = numeric_df.corr()

# Print formatted results
print("The means are:   ", "  ".join(f"{v:.2f}" for v in mean_values))
print("The medians are: ", "  ".join(f"{v:.2f}" for v in median_values))
print("The standard deviations are: ", "  ".join(f"{v:.2f}" for v in std_values))
print("The variances are: ", "  ".join(f"{v:.2f}" for v in var_values))

# Print correlation matrix
print("\nThe correlation coefficients are:\n")
print(corr_values.to_string())


# Step 3.2: Find 5 minimum and 5 maximum values for each attribute
while True:
    try:
        sheet_num = int(input("\nEnter the sheet number (range 1 - 4) of the dataset to be analyzed: "))
        if 1 <= sheet_num <= len(sheets):
            sheet_name = sheets[sheet_num - 1]  # Convert user input (1-based) to 0-based index
            break
        else:
            print("\nError: Please enter a number between 1 and 4.")
    except ValueError:
        print("\nError: Please enter a valid numeric sheet number.")

# Step 3: Load the selected sheet
df_selected= pd.read_excel(file_path, sheet_name=sheet_name)

# Filter numeric columns
numeric_df = df.select_dtypes(include=['number'])
print(f"\nThe length (rows) of dataset in {sheet_name}: {len(df_selected)}\n")
for col_index, col_name in enumerate(numeric_df.columns):
    min_values = df_selected.nsmallest(5, col_name)[col_name].tolist()
    max_values = df_selected.nlargest(5, col_name)[col_name].tolist()

    print(f"\nFor the column {col_index} - {col_name} of {sheet_name}")
    print("The minima are:", "  ".join(f"{v:.1f}" for v in min_values))
    print("The maxima are:", "  ".join(f"{v:.1f}" for v in max_values))

print("\nProcess finished with exit code 0.")
# Step 4: Scatter plots for attribute pairs

numeric_df = df.select_dtypes(include=['number']).iloc[:, :4]
columns = numeric_df.columns

color_map = {"Iris-setosa": "y", "Iris-versicolor": "r", "Iris-virginica": "g"}
marker_map = {"Iris-setosa": ".", "Iris-versicolor": ".", "Iris-virginica": "."}

pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
plt.figure(figsize=(12, 10))

for i, (col1, col2) in enumerate(pairs, 1):
    plt.subplot(3, 2, i)
    for species in df["Species"].unique():
        subset = df[df["Species"] == species]
        plt.scatter(subset.iloc[:, col1], subset.iloc[:, col2],
                    label=species, color=color_map[species],
                    marker=marker_map[species], alpha=0.7)

    plt.xlabel(columns[col1])
    plt.ylabel(columns[col2])
    plt.title(f"{columns[col1]} vs {columns[col2]}")
    plt.legend()

plt.tight_layout()
plt.show()