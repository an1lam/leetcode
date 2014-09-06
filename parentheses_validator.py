
def parensValidator(s):
    opened = []
    openers = ["{", "(", "["]
    closers = ["}", ")", "]"]
    complements = dict((o, closers[i]) for (i, o) in enumerate(openers))
    for c in s:
        if c in openers:
            opened.append(c)
        elif c in closers:
            if len(opened) <= 0 or c != complements[opened.pop()]:
                return False
    return True

assert parensValidator("()") == True
assert parensValidator("{})") == False
assert parensValidator("[()]") == True
