def unique_values(arr):
    unique_set = set(arr)
    return list(unique_set)

if __name__ == "__main__":
    # Taking user input for the elements of the array
    input_array = list(map(int, input("Enter the elements of the array separated by space: ").split()))

    # Get the array with unique values
    unique_array = unique_values(input_array)

    # Print the unique values
    print("Unique values:", unique_array)
