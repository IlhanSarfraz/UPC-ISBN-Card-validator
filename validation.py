class validation():
    def __init__(self,valinput):
        self.input=valinput
    
    def validate_card(self):
        self.input = [int(num) for num in self.input]   #Changing datatype to list

        checkDigit = self.input.pop(-1)
        self.input.reverse()
        self.input = [num * 2 if idx % 2 == 0   #Doubling the digits at even indices
                    else num for idx, num in enumerate(self.input)]

        # 5. Subtracting 9 at even indices if digit is over 9
        self.input = [num - 9 if idx % 2 == 0 and num > 9
                    else num for idx, num in enumerate(self.input)]
        self.input.append(checkDigit)   #Adding the checkDigit back to the list:

        checkSum = sum(self.input)  #Adding all digits:
        if checkSum % 10 == 0:
            print("The card number is valid")
        else:
            print("The card number is not valid")

    def validate_upc (self) :
        self.input = [int(x) for x in self.input]
        if len(self.input) == 12:
            odd = 0
            even = 0
            for i in range (0, 12,2) : 
                odd += self.input [i]
            odd=odd*3
            for j in range(1, 11,2) :
                even += self.input[j]
            total = even + odd
            total2 = 10-((even + odd)%10)
            if total2==10:
                total2=0
            if total2 == self.input[-1]:
                print ("The UPC is Valid!")
            else:
                print ("The UPC is Not Valid!")
        else:
            print ("Not Valid!")
            againinput = input ("Enter UPC number to Check for Validation:")
            v=validation(againinput)
            v.upc()


    def validate_isbn (self):      
        self.input = [int(x) for x in self.input]
        if len(self.input) == 13:
            odd = 0
            even = 0
            for i in range (1,13,2): #for even
                even = even+self.input[i]*3  #multiplying even numbers by 3
            for j in range (0,12,2): #for odd
                odd += self.input[j]  #multiplying odd numbers by 1
            X = (odd + even) % 10
            if X==0:
                print ("The ISBN is Valid!")
            else:
                print ("The ISBN is Not Valid!")
        elif len (self.input) == 10:
            sum = 0
            l = [10,9,8,7,6,5,4,3,2]
            for i in range (9):
                sum += (self.input [i] * l[i])
            X = sum % 11
            if X==0:
                print ("The ISBN is Valid!")
            else:
                print ("The ISBN is Not Valid!")
        else:
            print ("Not A Valid ISBN Number!")
            againinput = input("Enter the ISBN Number to Check for Validation: ")
            v=validation(againinput)
            v.isbn()

# sample_isbn="9783161484100"
# sample_upc="512345678900"
# sample_card_number="6011111111111117"
while True:
    try:
        print("Which number do you want to validate:\n[1]ISBN\n[2]UPC\n[3]Card Number\n[4]Exit")
        choice=eval(input("Enter your choice: "))
        if choice ==1:
            inputv=input("Enter the number you want to validate: ")
            v=validation(inputv)
            v.validate_isbn()
            break
        elif choice ==2:
            inputv=input("Enter the number you want to validate: ")
            v=validation(inputv)
            v.validate_upc()
            break        
        elif choice ==3:
            inputv=input("Enter the number you want to validate: ")
            v=validation(inputv)
            v.validate_card()
            break
        elif choice==4:
            print("Exited!")
            break
        else:
            print("Wrong option, Try again !")
    except:
        print("try again")