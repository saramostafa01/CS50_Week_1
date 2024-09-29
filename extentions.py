# Prompt the user for the name of the file
def main():
    file = input("Whats's the name of the file? ").lower()
    if "." in file:
        suffix(file)
    else :
        print("application/octet-stream")


def suffix(x):
    first , last = x.split(".")

    if last == "gif":
        print("image/gif")
    elif last == "jpg":
        print("image/jpeg")
    elif last == "jpeg":
        print("image/jpeg")
    elif last == "png":
        print("image/png")
    elif last == "pdf":
        print("application/pdf")
    elif last == "txt":
        print("text")
    elif last == "zip":
        print("archive file/zip")
    else :
        print("application/octet-stream")

main()

