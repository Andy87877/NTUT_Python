def is_unique(given_string):
    # creating an empty set
    chars_set = set()
    for char in given_string:
        # if char already in set
        # it is duplicate
        if char in chars_set:
            return False
        else:
            # char not in set, add it to chars_set
            chars_set.add(char)
            # if no duplicates
    return True


print(is_unique("just"))
