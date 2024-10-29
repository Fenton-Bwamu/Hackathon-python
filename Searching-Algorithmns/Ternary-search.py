def ternary_search(arr, left, right, target):
    """
    Perform a ternary search to find a target value in a sorted array.

    Parameters:
    - arr (list): A sorted array of integers.
    - left (int): The starting index of the array segment to search.
    - right (int): The ending index of the array segment to search.
    - target (int): The integer value to search for.

    Returns:
    - int: The index of the target if found, otherwise -1.
    """
    # Check if the search space is valid
    if right >= left:
        # Calculate the two midpoints for ternary search
        mid1 = left + (right - left) // 3  # First third index
        mid2 = right - (right - left) // 3  # Second third index
        
        # Check if the target is at either of the midpoints
        if arr[mid1] == target:
            return mid1  # Return the index if found at mid1
        if arr[mid2] == target:
            return mid2  # Return the index if found at mid2

        # Target is in the left one-third
        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)  # Search in the left third

        # Target is in the middle one-third
        elif target > arr[mid1] and target < arr[mid2]:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)  # Search in the middle third

        # Target is in the right one-third
        else:
            return ternary_search(arr, mid2 + 1, right, target)  # Search in the right third
    
    # If the element is not present in the array, return -1
    return -1

# Driver code to test the ternary search function
if __name__ == "__main__":
    # Define a sorted array for searching
    arr = [1, 3, 4, 7, 10, 14, 18, 21, 28, 30, 35, 40, 50, 55, 60, 70]
    target = 28  # Define the target value to search for

    # Perform ternary search on the array
    result = ternary_search(arr, 0, len(arr) - 1, target)

    # Check if the result is not -1, meaning the target was found
    if result != -1:
        print(f"Element {target} found at index {result}.")  # Output the index if found
    else:
        print(f"Element {target} not found in the array.")  # Indicate the target was not found
