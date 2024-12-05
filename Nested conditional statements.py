Name=input('Enter Your Name: ')
score=0
print('Select your quiz')
print('1.Sports')
print('2.geography')
option=input('Enter your option 1 or 2: ')

if option=="1":
    print('Select your sports Category: ')
    print('a.Cricket')
    print('b. Football')
    option1=input('Enter your option a or b: ')
    if option1=="a" or option1=="A":
         print('Welcome to Cricket Quiz..')
         print('which Cricket team won Highest ICC Men world cup? ')
         print('1. Australia')
         print('2. India')
         quiz=input('Enter your answer=')
         if quiz=="1":
              score=score+10
              print(f"Congrats {Name}!!")
              print (f"Congrats {Name}!!! Correstc answer, your score is {score}")
         else:
              print('Incorrect answer. Try again')

    elif option1=="a" or option1=="A":
         print('Welcome to Cricket Quiz..')
         print('which Cricket team won Highest ICC Men world cup? ')
         print('1. Australia')
         print('2. India')
         quiz=input('Enter your answer=')
         if quiz=="1":
              score=score+10
              print(f"Congrats {Name}!!")
              print (f"Congrats {Name}!!! Correstc answer, your score is {score}")
         else:
              print('Incorrect answer. Try again')

if option=="2":
    print('Select your sports Category: ')
    print('a.Country')
    print('b. osean')
    option1=input('Enter your option a or b: ')
    if option1=="a" or option1=="A":
         print('Welcome to Country Quiz..')
         print('which Country in makka? ')
         print('1. arab')
         print('2. dubai')
         quiz=input('Enter your answer=')
         if quiz=="1":
              score=score+10
              print(f"Congrats {Name}!!")
              print (f"Congrats {Name}!!! Correstc answer, your score is {score}")
         else:
              print('Incorrect answer. Try again')

    elif option1=="b" or option1=="B":
         print('Welcome to country Quiz..')
         print('which is the largest osean  ? ')
         print('1. russia')
         print('2. china')
         quiz=input('Enter your answer=')
         if quiz=="1":
              score=score+10
              print(f"Congrats {Name}!!")
              print (f"Congrats {Name}!!! Correstc answer, your score is {score}")
         else:
              print('Incorrect answer. Try again')
    