# Prompt the user for a greeting
greeting = input("Input greeting: ").lower().strip()

# Test if the customer was greeted properly
if greeting == "hello":
    print("$0")
elif greeting[0] == "h" and greeting != "hello":
    print("$20")
else :
    print("$100")
