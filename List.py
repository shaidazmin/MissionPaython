

studentsName = ["Azmin","Zame", "Sompa","Polas","Tipu"]

user= input("Enter a students name : ")

if user in studentsName:
    print(user +" is here. \n")
else:
    print("Congratulations!")

# we can also use here els statement for one  condition
if user not in studentsName:
    print(user +" is not here. \n ")
else:
    print("Sorry!")

#todo .......
addStudent = input("Add Students")
studentsName +[addStudent]

print(studentsName)
#print(studentsName[0])
i = 0
while i<=4:
    print(studentsName[i])
    i = i+1

    print("\nRevere : \n")
i = 4
while i>=0:
    print(studentsName[i])
    i= i -1