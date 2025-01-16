# a= int(input("Enter your age-> ")) 
# print("your age is:" , a)

# if(a>18):
#  print("you can drive")
# else:
#  print("you can't drive")



# num= int(input("Enter a number-> "))    
# if(num<0):
#  print("number is negative")    
# elif(num==0):
#  print("number is zero")    
# else:  
#     print("number is positive") 


# num= int(input("Enter a number-> "))
# if(num%2):
#     print("number is odd")

# else:
#     print("number is even")

 #nested if else

# num=18
# if(num<0):
#     print("number is negative")
# elif(num>0):
#     if(num<=10):
#         print("Number is between 0 to 10")
#     elif(num>10 and num<=20):
#         print("Number is between 11 to 20") 
#     else:
#         print("Number is greater than 20")
# else:
#     print("number is zero")
# x= int(input("Enter a number-> "))
# match x:
#     case 0:
#         print("number is zero")
#     case 4:
#         print("number is 4")
#     case _:
#         print(x)

#input-amount amount of purchase and calculate discount ,find price payable amount 


amount= int(input("Enter amount of purchase-> "))

if(amount>=10000):
    discount=amount*0.15
elif(amount>=5000 and amount<10000):
    discount=amount*0.10
    price=amount-discount
    print("Discount is:",discount)
    print("price payable amount is:",price)
else:
    print("No discount")
    print("price payable amount is:",amount)

