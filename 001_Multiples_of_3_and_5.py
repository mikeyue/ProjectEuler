# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

res = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        res += i
print(res)  # 233168


# Submission attempts: 1
# Congratulations, the answer you gave to problem 1 is correct.

# You are the 807250th person to have solved this problem.

# This problem had a difficulty rating of 5%. The highest difficulty rating you had previously solved was 0%.
# This is a new record. Well done!