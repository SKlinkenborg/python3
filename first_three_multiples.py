# Write your first_three_multiples function here
def first_three_multiples(num):
  for i in range(0,3):
    sums = []
    sums.append(num * (i + 1))
    print(sums)
  result = sums[-1]
  return(result)

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# Challenge: Recreate using map(), lambda

numbers = range(1,4)
doubled = list(map(lambda x: x * 2, numbers)) 
print(doubled)