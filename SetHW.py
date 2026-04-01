setx = {"green", "blue"}
sety = {"blue", "yellow"}

print("Original set elements:")
print(setx)
print(sety)
print("\nDifference of two said sets:")
setz = setx.difference(sety)
print(setz)
setz1 = sety.difference(setx)
print(setz1)
setz2 = sety.symmetric_difference(setx)
print(setz2)
setz3 = setx.symmetric_difference(sety)
print(setz3)
