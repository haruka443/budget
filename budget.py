maxBudgetEntertainment = 150
maxBudgetFood = 300
maxBudgetOthers = 500
remainingBudgetEntertainment = maxBudgetEntertainment
remainingBudgetFood = maxBudgetFood
remainingBudgetOthers = maxBudgetOthers

while True:
    usersAmount = input('Input an amount of your expenditure: ')
    if usersAmount == '':
        print(remainingBudgetEntertainment, remainingBudgetFood, remainingBudgetOthers)
    else:
        cost = float(usersAmount)
        if cost <= 0:
            print('An incorrect amount was inputted')
            continue
        print('''Goals of expense:
        Entertainment - e
        Food = f
        Others - o''')
        purpose = input('Input a goal of your expenditure: ')
        if purpose == "r":
            if cost > remainingBudgetEntertainment:
                print('The defined amount overruns your budget')
            else:
                remainingBudgetEntertainment -= cost
                print(f'Remaining amount for development: {remainingBudgetEntertainment} zł')
        elif purpose == "f":
            if cost > remainingBudgetFood:
                print('The defined amount overruns your budget')
            else:
                remainingBudgetFood -= cost
                print(f'Remaining amount for development: {remainingBudgetFood} zł')
            
        elif purpose == "o":
            if cost > remainingBudgetOthers:
                print('The defined amount overruns your budget')
            else:
                remainingBudgetOthers -= cost
                print(f'Remaining amount for development {remainingBudgetOthers} zł')
        else:
            print("Incorrect goal!")


