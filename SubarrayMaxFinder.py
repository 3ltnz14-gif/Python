# KADANE'S ALGORITHM
# Topics: Subarrays | The drag of negatives | Running sum with
# reset | Max-so-far tracker | Kadane's algorithm

# Part 1: Subarrays: slices of an array
nums = [2, -5, 3, 4, -1, 6, 3]
print("Full array:", nums)
print("Some subarrays:")
print(f"[0:2] {nums[0:2]} sum = {sum(nums[0:2])}")
print(f"[2:6] {nums[2:6]} sum = {sum(nums[2:6])}")
print(f"[3:7] {nums[3:7]} sum = {sum(nums[3:7])}")
print()

# Part 2: The drag of negatives: running sum with reset
print("Running sum trace:")
running = 0
for num in nums:
    running += num
    if running < 0:
        print(f"{num} -> sum = {running} <- negative! reset to 0")
        running = 0
    else:
        print(f"{num} -> sum = {running}")
print()

# Part 3: Max-so-far: capture the best before reset erases it
running = 0
best = 0
for num in nums:
    running += num
    if running < 0:
        running = 0
    if running > best:
        best = running
print(f"Array: {nums}")
print(f"Max subarray sum: {best}")
print()

# Part 4: Kadane on a harder array
hard = [1, 2, 3, -4, 5, -22, -4, 25, 2, -9]
running = 0
best = 0
for num in hard:
    running += num
    if running < 0:
        running = 0
    if running > best:
        best = running
print(f"Array: {hard}")
print(f"Max subarray sum: {best}")