def length_of_longest_substring(s):
    # Initialize pointers and a set to keep track of characters in the substring
    left = 0  # Pointer for the start of the current substring
    max_length = 0  # Variable to track the maximum length of substring found
    char_set = set()  # Set to store unique characters in the current substring
    
    # Iterate with the right pointer to expand the window
    for right in range(len(s)):
        # If there's a repeating character, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])  # Remove character at left pointer from the set
            left += 1  # Move left pointer forward to shrink the window
            
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update the maximum length if the current window is larger
        max_length = max(max_length, right - left + 1)  # Calculate the window size and update max_length
    
    return max_length  # Return the length of the longest substring without repeating characters

# Example usage
if __name__ == "__main__":
    s = "abcabcbb"
    print(length_of_longest_substring(s))  # Output: 3

    s = "bbbbb"
    print(length_of_longest_substring(s))  # Output: 1

    s = "pwwkew"
    print(length_of_longest_substring(s))  # Output: 3
