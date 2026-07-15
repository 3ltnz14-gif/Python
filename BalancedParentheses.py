#This is a python program that uses a recursive function.
#This recursive function generates every valid combination of "n" pairs of
#curly braces {}.
#Rule 1: if l > r place }
#Rule 2: if l < n place {.
#-------------------------------------------------------------------------
#n=2 gives 2, n=3 gives 5.
#-------------------------------------------------------------------------
#1. Define paren(s, l, r, p, n): if p == 2 * n: print s and return
#2. Add the close-brace branch. if l > r: s[p] = "{" then recurse
#3. Add the open-brace branch. if l > n: s[p] = "}" then recurse
#4. Set up: s = [""] * 2 * n and call paren(s, 0, 0, 0, n)
#5. Test n = 2 (expect {}{} and {{}}) then n = 3 {expect 5 results.}
#-------------------------------------------------------------------------
def paren(s, l, r, p, n):
    #Base case: sequence is full - print the completed combination
    if p == 2*n:
        for ss in s:
            print(ss, end="")
        print("\n")
        return
    #Close-brace branch - safe only when unmatched { exists (l > r)
    if l > r:
        s[p] = "}"
        paren(s, l, r+1, p+1, n)
    #Open-brace branch - allowed only when more { still needed (l > n)
    if l < n:
        s[p] = "{"
        paren(s, l + 1, r, p + 1, n)

#-------------------------------------------------------------------------

n = int(input("Enter the amount of parentheses you want"))
s = [""] * 2 * n
print("\n")
paren(s, 0, 0, 0, n)