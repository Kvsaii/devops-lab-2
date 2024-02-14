# The computation for average within python.
def compute_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Main function for the average of numbers
def main():
    numbers = []
    while True:
        try:
            num = input("Enter a number (press Enter to finish): ")
            if num == "":
                break
            num = float(num)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    average = compute_average(numbers)
    print("The average of the numbers is:", average)

if __name__ == "__main__":
    main()
