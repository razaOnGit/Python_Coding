# Create a program capable of displaying Questions to the user like KBC
# Use list data-type to store the questions and their correct answers
# Display the final amount the person takes home post game-play
# Use a random function to select questions from the list


# name = input("What is your name ?\n")

# print("\nGood to see you",name,",Welcome to Kaun Banega Crorepati !\n")

# print("Here is your first question \n", )

# questions = ["What is capital of India? ", "Who won FIFA 2022? ","How many planets in Solar system? ", "What is value of 1 kg?"]

# answers = ["delhi", "argentina","8","1000g"]

# a = 1000
# b = 2000
# c = 3000
# d = 4000

# answers1 = input(questions[0])
# if answers1.lower() == answers[0]:
#     print("Correct answer. You have won", a, "INR\n")

#     answer2 = input(questions[1])
#     if answer2.lower() == answers[1]:
#         print("Correct answer. You have won", b, "INR\n")

#         answer3 = input(questions[2])
#         if answer3.lower() == answers[2]:
#             print("Correct answer. You have won", c, "INR\n")
            
#             answer4 = input(questions[3])
#             if answer4.lower() == answers[3]:
#                 print("Correct answer. You have won", d, "INR\n")
#             else:
#                 print("Wrong answer.Your take home amount is",c,"INR\n")
#         else:
#             print("Wrong answer.Your take home amount is",b,"INR\n")
        
#     else:
#         print("Wrong answer.Your take home amount is",a,"INR\n")

# else:
#     print("Galat Jawab, Tumse na ho paayega",0,"INR\n")
    
# print("It was great playing with you",name) 



# Solution 2
questions = [
             ["What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", 1],
             ["Who won FIFA 2022?", "Argentina", "Brazil", "Germany", "France", 2],
             ["How many planets are there in the Solar System?", "8", "9", "10", "11", 2],
             ["What is the value of 1 kg?", "1000g", "500g", "2000g", "1500g", 1],
             ["What is the capital of France?", "Paris", "London", "Berlin", "Rome", 1], 
            
             ["How many continents are there in the world?", "5", "6", "7", "8", 3],
             ]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(question[0])
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")