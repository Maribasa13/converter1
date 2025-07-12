# chile


def convert(ops, value):
    if ops == "km":
        return f"{ value * 1000}"

    elif ops == "m":
        return f"{ value / 1000}"
    else: 
        return "Error"
print("Hello! \n")



ops = input(" m  or  km")
value = int(input("enter number: "))
print(convert(ops, value))