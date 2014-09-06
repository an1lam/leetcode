def is_palindrome(string):
    if len(string) < 2:
        return False
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

assert is_palindrome("foof") == True
assert is_palindrome("foo") == False
assert is_palindrome("f") == False
assert is_palindrome("bob") == True

def is_palindrome_possible(string):
    length = len(string)
    allowed_singletons = 0
    if length < 2:
        return False
    if length & 0x1:
        allowed_singletons = 1
    appearances = {}
    for c in string:
        if appearances.get(c) is not None:
            appearances[c] += 1
        else:
            appearances[c] = 1
    for v in appearances.values():
        if v != 2:
            allowed_singletons -= 1
    return allowed_singletons == 0

assert is_palindrome_possible("foof") == True
assert is_palindrome_possible("foxxo") == True
assert is_palindrome_possible("f") == False
