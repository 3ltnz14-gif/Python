scores = [123, 43, 12445321, 235, 234, 2**21, 1]
print(f"Head: {scores[0]}")
print(f"Tail: {scores[1:]}")
print(f"Head of Tail: {scores[1:][0]}")
print(f"Tail of Tail: {scores[1:][1:]}")

def showshrink(a, depth):
    if len(a) == 1:
        print(a)
        return
    print(a, len(a))
    showshrink(a[1:], depth + 1)
showshrink(scores, 1)

def issorted(a):
    if len(a) <= 1: return True
    return a[0] <= a[1] and issorted(a[1:])

def totalscore(a):
    if len(a) == 1: return a[0]
    return a[0] + totalscore(a[1:])
print(f"Total score: {totalscore(scores)}")

def topscore(a):
    if len(a) == 1: return a[0]
    return max(a[0], topscore(a[1:]))
print(f"Top score: {topscore(scores)}")