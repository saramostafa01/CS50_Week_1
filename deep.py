Answer = input("What's the Great Question of Life, the Universe and Everything? ").lower()

if Answer == "42":
    print("Yes")
elif Answer == "forty two":
    print("Yes")
elif Answer == "forty-two":
    print("Yes")
else:
    print("No")
