def palindrome(lst):
    if len(lst) <= 1:
        return True

    if lst[0] == lst[-1]:
        return palindrome(lst[1:-1])
    else:
        return False

