while True:
    coffee = input("What is the coffee situation? (empty/full) ")
    if coffee.lower() == 'empty':
        print('fill')
        break
    elif coffee.lower() == 'full':
        print('drink')
        break
    else:
        print("it's okay")
        
print('so proceed...☕')
 
 
 
