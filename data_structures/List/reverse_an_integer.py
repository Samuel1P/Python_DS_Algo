# reverse an integer
# leading zero and trailing zero post reversal are funky
num = 54321

#initalize return value variable
reveresed_integer = 0
# initialize remainder which will append (add) to the return value
remainder = 0

while num > 0:
    # comments for iteration 1
    remainder = num % 10 # 1
    num = num // 10 # 5432
    reveresed_integer = reveresed_integer * 10 + remainder # 0 * 10 + 1 = rev  = 1

print (reveresed_integer)