# Part 1: Slices and their sums
arr = [-4, 6, 2, 0, 0, 1, 1]
print("Full array          :", arr)
print("Left of index 2     :", arr[:2])
print("Right of index 2    :", arr[3:])
print("Left sum at index 2 :", sum(arr[:2]))
print("Right sum at index 2:", sum(arr[3:]))

# Part 2: Balance at every index
print("\nBalance check:")
for i in range(len(arr)):
    L = sum(arr[:i])
    R = sum(arr[i + 1:])
    print(f"Index {i}\n  Left: {L}\n  Right: {R}")

# Part 3: Equilibrium point
print("\nEquilibrium point:")
for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
        print(f"Index {i}\n  Element: {arr[i]}")

# Part 4: Growing subarray window
nums = [3, 6, 2, 2, 56, 1, 0, 9]
target = 10
print(f"\nGrowing window (start = 1, target = {target})")
curr = 0
for j in range(1, len(nums)):
    curr  += nums[j]
    print(f"nums[1 to {j}] = {nums[1:j+1]} sum = curr")
    if curr == target: break

# Part 5: Find subarray with target sum:
print("Searching all windows:")
found = False
for i in range(len(nums)):
    curr += nums[j]
    if curr == target:
        print(f"Found! Indexes {i} to {j} : {nums[i:j+1]}")
        found = True
        break
    if curr > target:
        break
if not found: 
    print("No subarray found")