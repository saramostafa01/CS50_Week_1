# Prompt the user for the time
def main():
    time = input("what's the time? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    meal = float(hours) + float(minutes)/60
    if 7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print("lunch time")
    elif 18 <= meal <= 19:
        print("dinner time")
    else :
        print("")
    

if __name__ == "__main__":
    main()