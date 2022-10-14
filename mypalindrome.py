
print("Welcome to the PALINDROME CHECKER!")

def my_palindrome():
    
    word=input("Enter the word you would like to check: ")

    if word==word[::-1]:
        print("Congratulations, your word is a PALINDROME!")
    else:
        print("Your input is not a PALINDROME.")
my_palindrome()

def dotryagain():
    tryagain=input("Would you like to check another word? yes or no\n>> ").lower()

    if tryagain=="yes":
        my_palindrome()
    elif tryagain=="no":
        print("Thank you for using PALINDROME CHECKER!")
    else:
        dotryagain()
dotryagain()
while dotryagain():
    my_palindrome()