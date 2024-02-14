# Function to compute the average of a list of numbers
def compute_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Main function
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

    if len(numbers) == 0:
        print("No numbers entered.")
    else:
        average = compute_average(numbers)
        largest = max(numbers)
        smallest = min(numbers)
        
        print("Numbers entered:", numbers)
        print("Average:", average)
        print("Largest number:", largest)
        print("Smallest number:", smallest)

if __name__ == "__main__":
    main()
