# p = open(r"C:\Users\Hp\Desktop\SIH")
# print(p.read)

# r = open("superman.txt" , 'w')
# r.write("and my friend is gaurav")
# r.close()

from pathlib import Path


def readFileandFolder():
    path = Path('')
    items = list(path.rglob('*')) 
    for i, items in enumerate():     # if you want items ko alag and value ko alag then we can do write list as a enumerate
        print(f"{i+1} : {items}")      

def createfile() :
    try:
        readFileandFolder()
        name = input("please tell your for file name:-")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("What you want to write in this file :-")
                fs.write(data)

            print(F"FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists")


    except Exception as err:
        print(f"An error occured as {err}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for delete a file")

check = int(input("Please tell your response :- "))

if check == 1:
    createfile()

if check == 2:
    readFileandFolder()