#--Algorithm Analysis--Counting Game Points
#Topics: Algorithm | Pseudocode | Time Complexity | Space Complexity
#One Problem, Three Solutions | Comparing Efficiency

#Part 1: The Problem | set n = 4 rounds
#In a game, Round 1 = 1 point, 2 = 2 points, so on. Round n = n points.
#We will solve "find the total" THREE ways and count the steps each one takes.

n = 4
print(f"-=[Counting Game points (n = {n} rounds)]=-")
print()

#Part 2: The Formula Way | Always 1 step
#Algorithm: Use the s hortcut formula to get the answer instantly
#Pseudocode: total = n* (n + 1) / 2
#Time cost: 1 step, stays the same no matter how big n is
#Space cost: 1 variable, (total.)

total = n * (n + 1) // 2
print(f"-=[Formula way: total = {n} |steps = 1]=-")

#Part 3: The Loop Way | n steps
#Pseudocode: FOR round FROM 1 TO n: total = total + round
#Time cost: n steps -- grows with the number of rounds
#Space cost: 2 variables (total, round_num)

total = 0
steps = 0
for round_num in range(1, n + 1):
    total += round_num
    steps += 1
print(f"-=[Loop way: total = {total} | steps = {steps}]=-")


#Part 4: The Nested Loop Way | Roughly n*n steps
#Algorithm: Add 1 at a time for every single point in every round
#Pseudocode: FOR round FROM 1 to n: For point FROM 1 TO round: total += 1
#Time cost: Roughly n*n steps | exponentially grows!
#Space cost: 3 variables (total, round_num, point)

total = 0
steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        total += 1
        steps += 1
print(f"-=[Nested loop: total = {total} | steps = {steps}]=-")


#Part 5: Try n = 10 and see what happens to the steps

n = 10
nested_steps = 0
for round_num in range(1, n + 1):
     for point in range(1, round_num + 1):
         nested_steps += 1

print()
print(f"-=[Now with n = {n} rounds]=-")
print("Formula way: steps = 1 (always 1!)")
print(f"Loop way: steps = {n}")
print(f"Nested loop: steps = {nested_steps} (grows much faster!)")
print()
print("Time complexity = Same answer but very different costs!")