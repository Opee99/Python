# Taking value of kilometer from the user
km = float(input("Enter the value in kilometers: "))

# conversion factor
conv_factor = 0.621371

# calculate miles
miles = km * conv_factor
print('%0.2f kilometers is equal to %0.2f miles' %(km,miles))