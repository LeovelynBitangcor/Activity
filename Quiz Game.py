print("WELCOME TO OUR QUIZ GAME!")
name = input("Please enter your name: \n")
print("\nWelcome", name, "! Thank for participating our game !")
print("""\nBefore we are going to start, I would like
you to know that every question has different
difficulties, and contains 5 points if you guess
it right. You only have 1 attempts. And you can
continue to next level if you passed, the game
stops if you fail.\n""")
start = input("Enter to Continue ")
while start == "":
    print("\nOkay! START!")
    print("\n----------Difficulty: EASY----------")
    total = 0
    ans1 = '=='
    q1 = input("\nQ1. Symbol for 'equal-to'\n\n")
    if q1 == ans1:
        print("Correct!")
        total += 5
    else:
        print("Sorry wrong guess.\n"
              "Correct answer is '=='")

    ans2 = '%'

    q2 = input("\nQ2. What is the symbol for modulos\n\n")
    if q2 == ans2:
        print("Correct")
        total += 5
    else:
        print("Sorry, wrong guess")
        print("Correct Answer is '%'")

    ans3 = '*'

    q3 = input("\nQ3. What is the symbol for multiplication\n\n")
    if q3 == ans3:
        print("Correct!")
        total += 5
    else:
        print("Sorry, wrong guess\n"
              "Answer is '*'")

    print("\nTotal score in EASY Level is:", total,"/ 15")
    print("Passing score is 10\n")

    eas_totals = 10
    passed = True
    while True:
        for game in range(1):
            if eas_totals <= total:
                print("You Passed!\n"
                      "Let's proceed in MODERATE Level.")

                start_2 = input("\nEnter to Continue\n")

                while start_2 == "":
                    print("\n----------Difficulty: MODERATE----------\n")
                    total_2 = 0
                    ans_1 = 'A'

                    q_1 = input("""\nQ1. What is the code for this output\n
['Cow', 'Dog', 'Cat']
['Cow', 'Dog', 'Cat']
['Cow', 'Dog', 'Cat']

{A.}
name_list=["Cow","Dog", "Cat"]
for x in name_list:
    print(name_list)

{B.} 
name_list=["Cow","Dog", "Cat"]
For x in names_list:
    print(name_list)\n\n""")
                    if q_1 == ans_1 or q_1 == 'a':
                        print("Correct!\n")
                        total_2 += 3
                    else:
                        print("Sorry, wrong guess")
                        print("Correct Answer is A.\n")

                    ans_2 = 'B'

                    q_2 = input("""\n\nQ2.
count=0
for i in range(1, 5):
	if i%2 != 0:
        count+=1
        print(i)
print("We have ",count,"odd")

What will be the output?

{A.} Error
{B.} 1
     3
     We have 2 odd
{C.} 1
     2
     3
     4
     We have 2 odd\n\n""")
                    if q_2 == ans_2 or q_2 == 'b':
                        print("Correct!\n")
                        total_2 += 3
                    else:
                        print("Sorry, wrong guess."
                              "Correct answer is B.\n")

                    ans_3 = 'A'

                    q_3 = input("""\n\nQ3.What will be the output of the code?

OnlineGames = ['Mobile legend', 'Call of duty ', 'Dota 2', 'Apex legend']
for i in range(len(OnlineGames)):
    print("I love playing this game ", OnlineGames[i])

A. I love playing this game Mobile legend
   I love playing this game Call of duty
   I love playing this game Dota 2
   I love playing this game Apex legend

B. I love playing this game Mobile legend Call of duty Dota 2 Apex legend\n\n""")
                    if q_3 == ans_3 or q_3 == 'a':
                        print("Correct!\n\n")
                        total_2 += 4
                    else:
                    	print("Sorry, wrong guess."
                              "Correct answer is A.\n")

                    ans_4 = ("Repetition Structure", "repetition stucture".lower())

                    print("""\nQ4. Is used when a program needs to repeatedly process
one or more instructions until some condition
is met, at which time the loops end.\n""")
                    q_4 = input("".lower())
                    if q_4 == ans_4 or q_4 == 'loop' or q_4 == 'loops' or q_4 == 'Loops':
                        print("Correct!\n\n")
                        total_2 += 2
                    else:
                        print("Sorry, wrong guess."
                              "Correct answer is 'Loop' or 'Repetition Structure'.\n")

                    ans_5 = ("while loops".lower())

                    print("\nQ5. Python has two primitive loop command.\n")
                    q_5 = input("".lower())
                    if q_5 == ans_5 or q_5 == 'for loops' or q_5 == 'While loops' or q_5 == 'For loops' or q_5 == 'For loop' or q_5 == 'While loop' or q_5 == 'while loop':
                        print("Correct!\n\n")
                        total_2 += 2
                    else:
                        print("Sorry, wrong guess."
                              "Correct answer is 'For loops' or 'While Loops'\n")

                    ans_6 = "a"

                    print("""Q6. What are the 'Inputs'?\n          
a. Data entered into a program, either by the programmer or digitally.
b. Strings entered into a program, either by the programmer or digitally.
c. Data entered into a program, either by the bugs.
d. Loops entered into a program, either by the bugs.\n""")
                    q_6 = input("".lower())
                    if q_6 == ans_6 or q_6 == 'a':
                        print("Correct!\n\n")
                        total_2 += 1
                    else:
                        print("Sorry, wrong guess."
                              "Correct answer is A.\n")
                    print("Total score in MODERATE level is ", total_2,"/ 15")
                    print("Passing score is 13.\n")

                    med_totals = 13
                    passed = True
                    while True:
                        for game_2 in range(1):
                            if med_totals <= total_2:
                                print("You Passed!\n"
                                      "Let's proceed in HARD Level.")

                                start_3 = input("\nEnter to Continue.\n")

                                while start_3 == "":
                                    print("\n----------Difficulty: HARD----------")
                                    total_3 = 0
                                    ans__1_1 = 'quora', 'uber', 'dropbox', 'reddit', 'pinterest'
                                    
                                    print("""
                                    Q1. 
Quora       Snapchat        Dropbox      	    Lazada              Uber
Firefox     Vim	            Adobe Photoshop	    VLC Media player
WinRAR      Node.js	        AngularJS      	    Git     	
Reddit	    Pinterest	    Mailchimp	        Flickr

From the programs and software applications
listed above, input a program
or app that is mainly created 
through Python.

NOTE: Bunos Round.
""")
                                    q__1 = input(">>>")
                                    
                                    if q__1 == ans__1_1:
                                    	print("Correct!")
                                    	total_3+=5
                                    else:
                                        
                                        print(" The answer is 'quora, uber, dropbox, reddit, pinterest'.\nNice try.")
                                        
                                        total_3 += 5

                                    ans__2 = ["February", "february"]
                                    dat=20
                                    yer=1991

                                    q__2 = input("Q3. When was the Python programming language created?\nJanuary	July\nFebruary   August\nMarch	  September\nApril	  October\nMay	    November\nJune	   December\nEnter Month>>>")
                                    Q2_2=int(input("Enter date >>>"))
                           
                                    Q2_3=int(input("Enter the year>>>"))
                                   
                                    if q__2==ans__2:
                                    	print("  ")
                                    if Q2_2==dat:
                                        print("  ")
                                    if Q2_3==yer:   
                                        print("Correct")
                                        total_3 += 5
                                        print("\nPython was created and first released on February 20, 1991.\nWhile you may know the python as a large snake, the name of the Python programming language comes from an old BBC television comedy sketch series called Monty Python's Flying Circus.")
                                    else:
                                        print("Sorry, wrong guess.\n")
                                        print("Correct Answer is February 20 1991")

                                    

                                    print("\nTotal score in HARD Level is:", total_3)
                                    print("Passing score is 10")

                                    har_totals = 10
                                    passed = True
                                    while True:
                                    	for okay in range(1):
                                            if har_totals == total_3:
                                                print("\nYou Passed!")
                                                print("You COMPLETED the Game,", name, "!")
                                                print("Congratulations!!\n")
                                                print("Total Scores:", total + total_2 + total_3,"/ 40")
                                                average=total+total_2+total_3
                                                if average == 40:
                                                	print("PERFECT!")
                                                elif average <= 39:
                                                	print("PASSED")
                                                elif average <= 32:
                                                	print("PASSED")
                                                else:
                                                	print("FAILED")
                                                
                                                exit()
                                               
                                    
                                    	break
                        else:
                            print("Failed\n"
                                  "Try Again")
                            break
        else:
            print("Failed\n"
                  "Try Again")
            break