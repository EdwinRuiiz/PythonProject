import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the iris dataset from Sheet1 of iris.xlsx
def load_and_prep_data(file_path):
    """"
    Loads the Excel file and strips the whitespace from species names.
    Helps avoid errors caused by accidental spaces in species column
    """
    df = pd.read_excel(file_path, sheet_name="Sheet1")
    df['Species'] = df['Species'].str.strip()
    return df

# Train Logistic regression model with the given data
def train_logistic_regression(x, y, test_size=.25):
    """""
    Split the dataset into training and testing sets, then fit a logistic regression model.
    Returns:
        Trained logistic regression model
        Test features
        Test Target
        Predicted species
    """
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    # Training a classifier
    lr = LogisticRegression(max_iter=100)
    lr.fit(x_train, y_train)

    # Make a prediction on the test set
    y_prediction = lr.predict(x_test)

    return lr, x_test, y_test, y_prediction

# Display results along with R-squared score
def display_results(y_test, y_prediction, r_squared):
    """
        Display the actual and predicted species side by side.
        Also displays the final R-squared score.
        """
    print('\n{: <5} {: <15} {: <15}'.format('', 'y_test', 'y_prediction'))
    print('-' * 40)
    # Print each test sample's actual vs predicted species
    for i, (actual, predicted) in enumerate(zip(y_test, y_prediction)):
        print(f"{i:<5} {actual:<15} {predicted:<15}")

    # Display R-squared score (model accuracy on test set)
    print(f'\nR-squared: {r_squared:.4f}')
# Print key Logistic Regression configuration details
def print_logistic_regression_header(lr):
    """
      Print key parameters from the trained logistic regression model.
      This helps document how the model was configured.
      """
    print("\nLogistic Regression Model Configuration:")
    print(f"  Solver:          {lr.solver}")
    print(f"  Max Iterations:  {lr.max_iter}")
    print(f"  Penalty:         {lr.penalty}")
    print(f"  Multi-Class:     {lr.multi_class}")
    print(f"  C (Regularization): {lr.C}")
    print(f"  Tolerance:       {lr.tol}\n")

# Main to load data, train model, display results
def main():
    file_path = "iris.xlsx"

    # Load data
    df = load_and_prep_data(file_path)

    # Defines features and target columns
    feature_columns = df.columns[1:3]
    target_column = 'Species'

    # Display dataset information
    print(f"\nLength(rows) of dataset: {len(df)}")
    print(f"Columns used as features (explanatory variables): 0 - 3\n")

    # Prepare features and labels (X and y)
    x = np.array(df[feature_columns])
    y = np.array(df[target_column])

    # randomly splitting the data into training set and test set
    lr, x_test, y_test, y_predictions = train_logistic_regression(x, y)

    print(f"Target (label) column: 4 - The \"{target_column}\"")

    # Display logistic regression model configuration
    print_logistic_regression_header(lr)

    # Compute R-squared score
    r_squared = lr.score(x_test, y_test)

    # Display actual vs predicted and R-squared score
    display_results(y_test, y_predictions, r_squared)

# Run the main function
main()




