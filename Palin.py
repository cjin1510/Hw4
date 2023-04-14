def palindrome(lst):
    # Check if the list is empty or contains only one element
    if len(lst) <= 1:
        return True

    # Check if the first and last elements are the same
    if lst[0] == lst[-1]:
        return palindrome(lst[1:-1])
    else:
        return False

