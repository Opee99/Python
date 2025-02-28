# Function to get sum of digits 
def getSum(num):
    sum = 0
    for digit in str(num): 
      sum += int(digit)      
    return sum
   
num = int(input("Enter Num: "))
print(getSum(num))