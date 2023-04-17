


# Convert unit1 to unit2
# Return 
# True : To quit the program
# False : want convert 

def convert(unit1: str, unit2:str, factor:float, reverse: bool = False):
    if reverse:
        unit1, unit2 = unit2, unit1
        factor = 1/factor

    value_str = input(f"Convert {unit1} => {unit2}. Give value in {unit1} (or q to end): ")
    if value_str == "q":
        return True
    try:
        value_float = float(value_str)
    except:
        print("Error: You must enter a number \n (use point instead of comma)")
        return convert(unit1, unit2, factor)
    value_convert = round(value_float * factor, 2)
    print(f"Result of the conversion : {value_float} {unit1} = {value_convert} {unit2}")
    return False


while True:
    # Menu: convertor choice
    print("The programme is for unit conversion")
    print("Example")
    print("1 - inch to cm")
    print("2 - cm to inch")
    choice = input("Your choice (1 or 2): ")
    if choice == "1" or choice == "2":
        break
    print("Error : Choose 1 or 2 \n")

while True:
    # Menu ask the value to convert
    if choice == "1":
        if convert("inch", "cm", 2.54):
            break
    elif choice =="2":
        if convert("inch", "cm", 2.54, reverse=True):
            break

while True:
    # Menu ask the value to convert
    if convert("inch", "cm", 2.54, reverse = False if choice == "1" else True):
        break



# if choice == "1":
#     value_str = input("Convert inch => cm. Give value in inch : ")
#     value_float = float(value_str)
#     value_convert = round(value_float * 2.54, 2)
#     print(f"Result of the conversion : {value_float} inch = {value_convert} cm")


#     convert("inch", "cm", 2.54)
# if choice == "2":
#     value_str = input("Convert cm => inch. Give value in cm : ")
#     value_float = float(value_str)
#     value_convert = round(value_float * 0.394, 2)
#     print(f"Result of the conversion : {value_float} cm = {value_convert} inch")
#     convert("cm", "inch", 0.394)

#convert("inch", "cm", 2.54)

