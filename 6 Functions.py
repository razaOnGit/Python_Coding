# def calculateMean(a,b):
#     Mean =(a*b)/(a+b)
#     print(Mean)

# #functionn 2
# def calculatemean(a,b):
#     Mean =(a+b)/2
#     print(Mean)

# #function call
# def isgreater(a,b):
#     if a>b:
#         print("First no. is grater")
#     else:
#         print("Second no. is grater")
# a=4
# b=8 
# calculateMean(a,b)
# calculatemean(a,b)
# isgreater(a,b)

#defaul argument function
# def sum(a,b=5):
#     print(a+b)
# sum(4)

# def name(fname ="john" , lname ="doe"):
#     print(fname,lname)
# name("jane")
def average(*numbers):
    sum = 0
    for i in numbers:
        sum =sum +i
    print(sum/len(numbers))
average(5,6) 