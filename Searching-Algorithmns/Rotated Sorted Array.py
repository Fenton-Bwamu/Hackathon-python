def search_rotated_sorted_array(nums, target):
    """
    Searches for a target value in a rotated sorted array.

    Parameters:
    - nums (list): A rotated sorted array of integers.
    - target (int): The integer value to search for.

    Returns:
    - int: The index of the target in the array, or -1 if not found.
    """
    # Initialize pointers for binary search: left starts at the beginning, right at the end of the array.
    left, right = 0, len(nums) - 1
    
    # Loop until the pointers cross each other, indicating the search space is exhausted.
    while left <= right:
        # Calculate the middle index of the current search space.
        mid = (left + right) // 2
        
        # Check if the middle element is the target value.
        if nums[mid] == target:
            return mid  # Target found at index mid; return the index.
        
        # Determine which half of the array is sorted.
        if nums[left] <= nums[mid]:  # If the left half is sorted.
            # Check if the target is within the bounds of the sorted left half.
            if nums[left] <= target < nums[mid]:
                # If the target is in the left half, adjust the right pointer to narrow the search.
                right = mid - 1
            else:
                # If the target is not in the left half, adjust the left pointer to search the right half.
                left = mid + 1
        else:  # If the right half is sorted.
            # Check if the target is within the bounds of the sorted right half.
            if nums[mid] < target <= nums[right]:
                # If the target is in the right half, adjust the left pointer to narrow the search.
                left = mid + 1
            else:
                # If the target is not in the right half, adjust the right pointer to search the left half.
                right = mid - 1
    
    # If the target was not found in the array, return -1.
    return -1

# Sample rotated sorted array and target value for testing.
nums = [4, 5, 6, 7, 0, 1, 2]  # A rotated sorted array.
target = 0  # The target value we want to search for in the array.

# Call the search function with the sample data and store the result.
result = search_rotated_sorted_array(nums, target)

# Print the result, showing the index of the target in the array.
print("Index of target:", result)  # Expected output: Index of target: 4
