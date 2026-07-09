#Part 1
scores = [340, 120, 410, 85, 270, 190, 55]
print(f"Head            : {scores[0]}")
print(f"Tail            : {scores[1:]}")
print(f"Head of tail    : {scores[1:][0]}")
print(f"Tail of tail    : {scores[1:][1:]}")

#Part 2:
def showshrink(a, depth):
    if len(a) == 1:
        print(a)
        return
    print(a, len(a))
    showshrink(a[1:], depth + 1)
showshrink([410, 270, 190, 55], 0)


#Part 3:
def issorted(a):
    if len(a) <= 1:
        return(True)
    return a[0] <= a[1] and issorted(a[1:])

#Part 4:
def totalscore(a):
    if len(a) == 1: return a[0]
    return a[0] + totalscore(a[1:])
print(f"Total Team Score: {totalscore(scores)}")

#Part 5:
def topscore(a):
    if len(a) == 1: return a[0]
    return max(a[0], topscore(a[1:]))

print(f"Top Score       : {topscore(scores)}")