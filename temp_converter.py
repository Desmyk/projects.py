def temp_converter(temp_from, temp_to, temp_value):
    #converting farenheight to degree celcius
    if (temp_from == "FARENHEIGHT" and temp_to == "DEGREE"):
        temp = temp_value - 33.5
        print(f'{temp_value} Farenheight is equivalent to {temp} degree celcius')
        
    elif (temp_from == "DEGREE" and temp_to == "FARENHEIGHT"):
        temp = temp_value + 33.5
        print(f'{temp_value} Degree is equivalent to {temp} Farenheightp')
    
    else :
        print("Invalid input")
        
        temp_from = input("Are you converting from 'Farenheight' or 'degree': ").upper()
        temp_to = input("Are you converting to 'Farenheight' or 'degree': ").upper()
        temp_value = float(input("enter temp value: "))
        temp_converter(temp_from, temp_to, temp_value)
    


temp_from = input("Are you converting from 'Farenheight' or 'degree': ").upper()
temp_to = input("Are you converting to 'Farenheight' or 'degree': ").upper()
temp_value = float(input("enter temp value: "))
temp_converter(temp_from, temp_to, temp_value)
          
          
          
          