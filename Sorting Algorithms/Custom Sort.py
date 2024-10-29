def sort_dicts_by_key(dicts, key):
    """
    Sorts a list of dictionaries based on a specified key.

    Parameters:
    - dicts (list): A list of dictionaries to be sorted.
    - key (str): The key to sort the dictionaries by.

    Returns:
    - list: A new list of dictionaries sorted by the specified key.
    """
    # Use the sorted function with a lambda expression to sort the dictionaries.
    # The lambda function accesses the value of the specified key in each dictionary.
    return sorted(dicts, key=lambda d: d.get(key))

# Example usage
if __name__ == "__main__":
    # A list of dictionaries to be sorted
    dictionaries = [
        {"name": "Alice", "age": 25}, 
        {"name": "Bob", "age": 30}, 
        {"name": "Charlie", "age": 20}
    ]

    # Sort the list of dictionaries by the "age" key
    sorted_dictionaries = sort_dicts_by_key(dictionaries, "age")

    # Iterate through the sorted list and print each dictionary
    for dictionary in sorted_dictionaries:
        print(dictionary)
        # Output:
        # {"name": "Charlie", "age": 20}
        # {"name": "Alice", "age": 25}
        # {"name": "Bob", "age": 30}
