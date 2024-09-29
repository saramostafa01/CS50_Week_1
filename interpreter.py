# Prompt user for arithmatic expression
math = input("Enter Expression: ")
x , y , z = math.split(" ")

if y == "+" :
    result = float(int(x) + int(z))
elif y == "-" :
    result = float(int(x) - int(z))
elif y == "*" :
    result = float(int(x) * int(z))
elif y =="/" and z != "0":
    result = float(int(x) / int(z))

print(f"{result:.1f}")