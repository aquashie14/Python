#Reverse the order
def order(number):
    y = 0
    while(number >= 1):
        z = number % 10
        y = 10 * y + z
        number = number / 10
        number = int(number)
    return(y)
Digits = int(input("Enter a number: "))
reverse_digit = order(Digits)
print("The reverse number of",Digits, "is", reverse_digit)
