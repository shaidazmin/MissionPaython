
Programming = ["C++","Java","C","C#","Django"]

print(Programming)
#. List Length
print(len(Programming))

#. Add List

Programming.append("Visul Basi")
print(Programming)

# Insert List

Programming.insert(4,"Html & Css")

print(Programming)
print(len(Programming))

Programming.insert(6,"Javascript")
print(Programming)

#.Delete data from lish
Programming.remove("Javascript")
print("After Delete Data ", Programming)


#. Sorting  Assending data from list

Programming.sort()
print(Programming)


#. Sorting Desending data from List

Programming.reverse()
print(Programming)

Programming.sort()
#. Delete Last valu from list

Programming.pop()
print(Programming)

# Copy List

LearningProgramming = Programming.copy()
print(LearningProgramming)

# Clear List

Programming.clear()
print(Programming)


#. Find Data Position From List

position = LearningProgramming.index("Java")
print("Java Position is :  ",position)


LearningProgramming.insert(5,"Java")
#. Item Count From List

ItemCount = LearningProgramming.count("Java")
print(ItemCount)