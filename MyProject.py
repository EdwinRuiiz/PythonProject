import math


def get_positive_real(prompt):

    while True:
        try:
            value =float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Enter a positive real number")
        except ValueError:
            print("Invalid input. Enter a numeric value.")

def get_positive_integer(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer(x):")
        except ValueError:
            print("Error:Invalid input. Please enter an integer(y)")

x = get_positive_real("Enter a positive real number (x):")
y = get_positive_integer("Enter a positive integer(y):")

z = x**y

log2_x = math.log2(x)
log2_y = math.log2(y)


print("\nResults:")
print(f"x^y = {x:.2f} ^{y} = {z:.4f}")
print(f"log2(x) = log2({x:.2f}) = {log2_x:.4f}")
print(f"log2(y) = log2({y}) = {log2_y:.4f}")