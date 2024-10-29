def is_match(s, p):
    # Initialize a DP table with False values
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True  # Empty pattern matches an empty string

    # Handle patterns with '*' at the beginning (e.g., "a*")
    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]  # '*' can match zero of the preceding character

    # Fill the DP table
    for i in range(1, len(s) + 1):  # Iterate over each character in the string
        for j in range(1, len(p) + 1):  # Iterate over each character in the pattern
            if p[j - 1] == '*':
                # '*' can match zero of the preceding character
                dp[i][j] = dp[i][j - 2]
                # '*' can also match one or more of the preceding character if there is a match
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                # Match current characters or '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]  # Move diagonally in the DP table

    # Return the result of matching the entire string with the pattern
    return dp[len(s)][len(p)]  # Return True if there's a match, False otherwise


# Example usage
if __name__ == "__main__":
    s = "abcd"
    p = "a*bcd"
    print(is_match(s, p))  # Output: True

    s = "abcd"
    p = "a*bc"
    print(is_match(s, p))  # Output: False
