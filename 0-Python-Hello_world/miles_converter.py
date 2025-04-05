# ask user to enter miles and store it in variable miles
miles = input("Enter miles: ")
# convert string to number integer
miles = int(miles)

#convert miles to kilometers
kilometers = miles * 1.60934

#print results
print("{} miles equals {} kilometers".format(miles, kilometers))