# Write a function named check_numbers which takes two numbers and then print "both are even" if both numbers are even (divide by 2) otherwise print "both numbers are not even".
def check_number(num1,num2):
    if num1%2==0 and num2%2==0:
        print("both are even")
    else:
        print("both number are not even")
check_number(23,22)
check_number(20,18)