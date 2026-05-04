#Write a program that requests a number from the user. Have the program print "Even" or "Odd" depending on whether they entered an even or odd number. 
# Remember that you can check if a number is even or odd using the modulus operator, like this:


number = int(input("Enter a number, 0 to exit the program: "))

while number != 0:
    if number % 2 == 0:
        print("Even")
    else:    
        print("Odd")
    number = int(input("Enter a number: "))

print("Goodbye!")


#Copilot version
# while True:
#     number = int(input("Enter a number, 0 to exit the program: "))
    
#     if number == 0:
#         print("Goodbye!")
#         break
    
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")