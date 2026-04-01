def multituple(nums):
    temp = list(nums)
    product = 1
    for x in temp:
        product *= x
    return product

nums = (4, 3, 2, 2, -1, 18)
print("Original Tuple:")
print(nums)

print("The product of nums: ", multituple(nums))

nums1 = (2, 4, 8, 8, 3, 2, 9)
print("\nOriginal Tuple: ")
print(nums1)
print("Product of nums1: ", multituple(nums1))