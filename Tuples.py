tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
#Tuples are immutable, so you can not add new elements

tuplex = tuplex + (9,)
print(tuplex)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

tuple2 = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

_slice = tuple2[3:5]

print(_slice)

_slice = tuple2[:6]
print(_slice)