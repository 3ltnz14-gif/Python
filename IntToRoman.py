class py_solution:
    def inttoroman(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        rnum = ""
        i = 0
        while num > 0:
            for x in range(num // val[i]):
                rnum += syb[i]
                num -= val[i]
            i += 1
        return rnum

print(py_solution().inttoroman(1))
print(py_solution().inttoroman(35))
print(py_solution().inttoroman(int(input("Enter a number from 1 = 1000"))))
    