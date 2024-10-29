import heapq

def find_kth_largest(nums, k):
    """
    Finds the Kth largest element in an unsorted list.

    Parameters:
    - nums (list): The list of numbers.
    - k (int): The 'Kth' position for the largest element.

    Returns:
    - int: The Kth largest element in the list.
    """
    # Initialize a min-heap with the first k elements from the list
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # Transform the list into a heap in-place

    # Iterate over the remaining elements in the list starting from index k
    for num in nums[k:]:
        # If the current number is larger than the smallest element in the heap
        if num > min_heap[0]:
            # Replace the smallest element (root) with the current number
            heapq.heappushpop(min_heap, num)
    
    # The root of the min-heap now contains the Kth largest element
    return min_heap[0]

# Example usage
if __name__ == "__main__":
    # An unsorted list of numbers
    nums = [3, 1, 5, 6, 4, 2]
    k = 3  # We want to find the 3rd largest element

    # Call the function to find the Kth largest element
    kth_largest = find_kth_largest(nums, k)
    print(f"The {k}th largest element is: {kth_largest}")  # Output the result
