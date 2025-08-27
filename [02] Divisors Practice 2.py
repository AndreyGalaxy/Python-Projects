import math
number = int(input("Input Number Here: "))
sqrt = int(math.sqrt(number))
divisors = set()
for element in range(1, sqrt + 1):
    quotient, remainder = divmod(number, element)
    if remainder == 0:
        divisors.add(element)
        divisors.add(quotient)
list2 = sorted(divisors)
print(list2)