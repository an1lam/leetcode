def printSum(candidates, index, n):
    for i in range(1, n+1):
        candidates[index[i]] = "" if i == n else "+"
        print(candidates[index[i]])
    print("\n")

def solveHelper(target, s, candidates, sz, index, n):
    if s > target:
        return
    if s == target:
        printSum(candidates, index, n)
    for i in range(index[n], sz):
        index.append(i)
        solveHelper(target, s + candidates[i], candidates, sz, index, n+1)

def solve(target, candidates, sz):
    index = []
    index.append(0)
    solveHelper(target, 0, candidates, sz, index, 0)

def main():
    solve(7, [2,3,6,7], 4)
if __name__ == "__main__":
    main()
