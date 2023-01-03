#Thomas Heer and James Bush
#CS 021 Final Project
#Daily Calorie and Macro Counter.

def menu(): #menu function allows the user to easliy navigate through the different
    #functionalities of the program
    #Made by Tommy
    print('Hello! Welcome to calorie counter thing')
    print('Options are listed below')
    print('For Setting Daily Goals, select 1')
    print('To record a meal, select 2')    
    print('To add a food to the database, select 3')
    print('To search the database, select 4')
    print('To see a printout of the list, select 5')
    print('To quit, type 6')
    
    #try excepts for input validation, makes sure the value is an integer within the range
    try:
        user_choice = int(input('which option would you like to select? '))
    except:
        print('Input must be a numeric value')
        user_choice = int(input('Which option would you like to select? '))
    while user_choice<1 or user_choice >6:
        user_choice = int(input('Invalid input, which option would you like to select? '))

    if user_choice == 1:
        goals()
    elif user_choice ==2:
        record_meal()   
    elif user_choice == 3:
        add_food()
    elif user_choice ==4:
        search()  
    elif user_choice ==5:
        printout()
    elif user_choice == 6:
        exit()#kills the function
        

def goals(): #the goals function allows the user to set daily calorie, protein, carb, and 
    #fat intake goals and stores them in a file for later use
    #made by Tommy
    goalsfile = open('goalfile.txt', 'w')
    #opens in write so it can overwrite itself when new goals are set
    print('Here, you will set you daily goals for calories, protein, carbohydrates, and fat')
    print('For more information about calories, google is a very good resource')


    #inputted values are converted to integer values so the try-excepts can make sure they
    #are integer values
    try:
        calories = int(input('What is your calorie goal?'))
    except ValueError:
        print('Inputted value must be an integer value. ')
        calories = int(input('What is your calorie goal?'))
    while calories<0:
        print('Inputted value must be greater than zero')
        calories = int(input('What is your calorie goal?'))
    try:
        protein = int(input('What is your protein intake goal?'))
    except ValueError:
        print('Inputted value must be an integer value. ')
        protein = int(input('What is your protein intake goal?'))
    while calories<0:
        print('Inputted value must be greater than zero')
        protein = int(input('What is your protein intake goal?'))
    try:
        carbs = int(input('What is your carbohydrate intake goal?'))
    except ValueError:
        print('Inputted value must be an integer value. ')
        carbs = int(input('What is your carbohydrate intake goal?'))
    while calories<0:
        print('Inputted value must be greater than zero')
        carbs = int(input('What is your carbohydrate intake goal?'))
    try:
        fat = int(input('What is your fat intake goal?'))
    except ValueError:
        print('Inputted value must be an integer value. ')
        fat = int(input('What is your fat intake goal?'))
    while calories<0:
        print('Inputted value must be greater than zero')
        fat = int(input('What is your fat intake goal?'))

#converts back to string so that they can be written into the goalsfile. 
    calories = str(calories)  
    protein = str(protein)
    carbs = str(carbs)
    fat = str(fat)

#writes the inputted values to the goals file  
    goalsfile.write(calories)
    goalsfile.write(',')
    goalsfile.write(protein)
    goalsfile.write(',')
    goalsfile.write(carbs)
    goalsfile.write(',')
    goalsfile.write(fat)

    goalsfile.close()
    print('\n')
    menu()

def add_food(): #this function allows the user to add a food into the database
    #including a name, its calories, protein, carbs, and fat.
    #made by Tommy and James
    print('\n')
    foodata = open('foodata.txt','a') #
    my_food = []
    name_food = input('What is the name of the food? ')
    name_food = name_food.lower()
    my_food+=[name_food]

    #try excepts to make sure valid integer values are added. 
    try:
        calories = int(input('How many calories are in this food? '))
        my_food += [calories] #adds each food to the list
    except:
        print('The calorie count must be a numerical value.')
        calories = int(input('How many calories are in this food? '))
        my_food += [calories]
    try:
        
        protein = int(input('How many grams of protein are in this food? '))
        my_food += [protein]
    except:
        print('The grams of protein count must be a numerical value.')
        protein = int(input('How many grams of protein are in this food? '))
        my_food += [protein]
    try:
        carbs = int(input('How many grams of carbohydrates are in this food? '))
        my_food += [carbs]
    except:
        print('The grams of carbohydrates must be a numerical value.')
        carbs = int(input('How many grams of carbohydrates are in this food? '))
        my_food += [carbs]
    try:
        fat = int(input('How many grams of fat are in this food? '))
        my_food += [fat]
    except:
        print('The grams of fat must be a numerical value.')
        fat = int(input('How many grams of fat are in this food? '))
        my_food += [fat]

    count = 0
    foodata.write('\n')
    for item in my_food: #loop writes each item into the database in a comma seperated list
        item = str(item)
        foodata.write(item)
        if count < 4: 
            foodata.write(',')
        count += 1
    foodata.close() # closes foodata file 
    print('Your food has been added to the database!')
    print('')
    menu() #calls menu fuction 
   

def search(): #allows the user to search for a specific item in the database, made by Tommy and James
    print('\n')
    foodfile = open('foodata.txt','r')
    foodlist = []   #reads the file and converts it into a list
    for line in foodfile:
        line = line.rstrip()
        line = line.split(',')
        foodlist +=line
    
    food = input('Enter a food to see if it is found in the database: ')
    food = food.lower()
    if food in foodlist: #compares the user input to the list
        index = foodlist.index(food)
        food = foodlist[index]
        calories = foodlist[index+1] #finds macros from databases
        protein = foodlist[index+2]
        carbs = foodlist[index+3]
        fat = foodlist[index+4]
        print('')
        print('Food Name: ', food)
        print('Calories: ', calories)
        print('Protein: ', protein)
        print('Carbohydrates: ',carbs)
        print('Fat: ',fat)
        print('')
        print('If you would like to try another food, type 1')
        print('If you would like to add it to the database, type 2')
        print('If you would like to return to the menu, type 3')


        #input validation for menu
        try:
            choice = int(input('which option would you like to select? '))
        except:
            print('Input must be a numeric value')
            choice = int(input('Which option would you like to select? '))
        while choice<1 or choice >3:
            choice = int(input('Invalid input, which option would you like to select? '))
        if choice == 1:
            search()
        elif choice ==2:
            add_food()
        elif choice ==3:
            print('\n')
            menu()
    else:
        print('Your entry was not found in the database.')
        print('If you would like to try another food, type 1')
        print('If you would like to add it to the database, type 2')
        print('If you would like to return to the menu, type 3')
        

        #input validation for menu
        try:
            choice = int(input('which option would you like to select? '))
        except:
            print('Input must be a numeric value')
            choice = int(input('Which option would you like to select? '))
        while choice<1 or choice >3:
            choice = int(input('Invalid input, which option would you like to select? '))
        if choice == 1:
            search()
        elif choice ==2:
            add_food()
        elif choice ==3:
            print('\n')
            menu()
        
def printout():     #provides the user a printout of every food on the list, made by Tommy
    print('\n')
    foodfile = open('foodata.txt','r')
    foodlist = []
    for line in foodfile:
        line = line.rstrip()
        line = line.split(',')
        foodlist +=line
    for i in range(0,len(foodlist),5): #moves in intervals of five so only the name of the food is printed
        print(foodlist[i])
    foodfile.close()
    print('\n')
    menu()
def counter(meal,food,cal,prot,carb,fat): #Made by James and Tommy
    #The counter function's purpose is to get the total calories of the day,
    #to compare that to the goals, and to record these values to the output file and to the counter file
    #This function takes the name of the meal, the name of the food, the calorie count, the protein count,
    #carb count, and fat count of the food.

    #the total calorie count is stored in its own file so it can keep the values even outside of the functions and while
    #the program isn't running
    counts = open('counter.txt', 'r')
    outfile = open('outfile.txt','a')
    goals = open('goalfile.txt','r')
    goalstring = goals.read()

    outfile.write(meal + ':' + '\n') #writes the nutritional info of the current foods being entered 
    
    outfile.write('Food name: '+food) # format for food name 
    outfile.write('\n')

    outfile.write('Calories: '+cal)  # format for calories to be written to file 
    outfile.write('\n')
                
    outfile.write('Protein: ' + prot) # format for protein to be written to file  
    outfile.write('\n')

    outfile.write('Carbohydrates: ' + carb)# format for carbs to be written to file
    outfile.write('\n')

    outfile.write('Fat: ' + fat) # format for fat to be written to file
    outfile.write('\n')
    if goals !='': # if statement saying if there goals isn't empty 
        goallist = goalstring.split(',') #creates list split by the coma 

    #this block of code gets the running total of calories, proteins, carbs, and fats

    countstring = counts.read() #makes countstring equal to counts which is the opened counter.txt file 
    countlist = countstring.split(',') # makes a list split by commmas
    calories =countlist[0] 
    calories = int(calories)+int(cal)
    protein = int(countlist[1]) +int(prot)
    carbs = int(countlist[2]) +int(carb)
    fats = countlist[3]
    fats = fats.rstrip()
    fats = int(fats)+int(fat)

    item = ','
    #goal_cals/prot/carb/fat is the difference of the goal and what they are currently at
    if item in goals: # if statement saying if there goals isn't empty 
        goal_cals = int(goallist[0])-calories
        goal_prot = int(goallist[1]) -protein
        goal_carb = int(goallist[2]) - carbs
        goal_fat = int(goallist[3]) - fats


        #if else statements saying if the goal is negative then print that they have met their goal
        # else print how many they have remaining until they meet their goal
        if goal_cals <= 0:
            outfile.write('Your calorie goal is met')
            outfile.write('\n')
        else:
            goal_cals = str(goal_cals)
            outfile.write('You have '+goal_cals+' calories remaining')
            outfile.write('\n')
        if goal_prot <= 0:
            outfile.write('Your protein goal is met')
            outfile.write('\n')
        else:
            goal_prot = str(goal_prot)
            outfile.write('You have '+goal_prot+' grams of protein remaining')
            outfile.write('\n')
        if goal_carb <= 0:
            outfile.write('Your carbohydrates goal is met')
            outfile.write('\n')
        else:
            goal_carb = str(goal_carb)
            outfile.write('You have '+goal_carb+' grams of carbohydrates remaining')
            outfile.write('\n')
        if goal_fat <= 0:
            outfile.write('Your fat goal is met')
            outfile.write('\n')
        else:
            goal_fat = str(goal_fat)
            outfile.write('You have '+goal_fat+' grams of fat remaining')
            outfile.write('\n')
        # converts everything to string to be used to write to output file    
        goal_cals = str(goal_cals)
        goal_prot = str(goal_prot)
        goal_carb = str(goal_carb)
        goal_fat = str(goal_fat)
        calories = str(calories)
        protein = str(protein)
        carbs = str(carbs)
        fats = str(fats)
        counts.close() # closes count 
        counts_out = open('counter.txt', 'w') # opens count as a write so it erases the previous entries and adds the new one
        counts_out.write(calories)
        counts_out.write(',')
        counts_out.write(protein)
        counts_out.write(',')
        counts_out.write(carbs)
        counts_out.write(',')
        counts_out.write(fat)
        outfile.write('\n')
        outfile.write('\n')
    elif item not in goals:
        counts_out = open('counter.txt', 'w') # opens count as a write so it erases the previous entries and adds the new one
        calories = str(calories)
        protein = str(protein)
        carbs = str(carbs)
        fats = str(fats)
        counts_out.write(calories)
        counts_out.write(',')
        counts_out.write(protein)
        counts_out.write(',')
        counts_out.write(carbs)
        counts_out.write(',')
        counts_out.write(fats)
        outfile.write('\n')
        
        
        
        outfile.write('Total calories: '+ calories)
        outfile.write('\n')
        outfile.write('Total protein: '+ protein)
        outfile.write('\n')
        outfile.write('Total carbohydrates: '+ carbs)
        outfile.write('\n')
        outfile.write('Total fats: '+ fats)
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\n')

  
    


def record_meal(): #foodata, outfile, goalfile
    #foodata is the name of text file
    # outfile is output file
    # goalfile is the file everything is written to
 

    #made by James
    
    myfile = open('foodata.txt','r') # opens foodata as r and assings it to myfile 
    foodlist = []
    for line in myfile: # for loop to put items in foodata into a list 
        line = line.rstrip()
        line = line.split(',')
        foodlist += line   
        
    count = 1
    print('If this is your first entry, then today is a new day')
    day = input('Is today a new day?(y/n) ')
    while day != 'y' and day != 'n': # error handleing for day input 
        print('Please enter y or n.')
        day = input('Is today a new day?(y/n) ')
    
    if day == 'y': # if its a new day then write all 0s to the counter file
        counterfile = open('counter.txt','w')
        counterfile.write('0,') #calories
        counterfile.write('0,') # protein
        counterfile.write('0,') #carbs
        counterfile.write('0') #fat
        counterfile.close()
    if day == 'y' or day == 'n': # if statement for if it a yes or no       
        meal = input('What meal is this? ') # asks what meal it is and writes it to file with colon and new line
                
        new = 'y'
        while new == 'y': # while lopp asking to enter new foods
            new = input('Would you like to enter new food?(y/n) ')
            while new != 'y' and new != 'n': # error handleing for new input
                print('Please enter y or n.')
                new = input('Would you like to enter new food?(y/n) ')
            if new == 'y':
                food = input('Enter food: ')
                food = food.lower() #makes food input all lower case
            else:
                print('Going back to menu...')
                print('\n')
                menu()
            if food in foodlist: # if food is in list it gets the calories protein carbs and fat for the food else it says food not found
                index = foodlist.index(food)
                food = foodlist[index]
                calories = foodlist[index +1]
                protein = foodlist[index + 2]
                carbs = foodlist[index + 3]
                fat = foodlist[index + 4]

                
                #try:
                counter(meal,food,calories,protein,carbs,fat)
                #except:
                    #print('An exception occured, please try again')
            
                    #record_meal()

            
                
            else:
                print('Food was not found')
    outfile.close()
    foodata.close()
    print('\n')
    menu()

       
          
    
    
menu()
