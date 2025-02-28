def hcf_is(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print(f"The H.C.F. is {hcf_is(num1, num2)}")
