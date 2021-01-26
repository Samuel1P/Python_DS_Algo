num = 54321

#initalize return value variable
rev = 0
# initialize remainder which will append (add) to the return value
rem = 0

while num > 0:
    # comments for iteration 1
    rem = num % 10 # 1
    num = num // 10 # 5432
    rev = rev * 10 + rem # 0 * 10 + 1 = rev = 1

print (rev)