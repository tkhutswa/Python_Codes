count = 0
user = str(input("Enter Word: \n"))
for i in user:
    count += 1
    a = i
    x = a.count(i)

print("The word {p} contains {d} letters!".format(p=user, d=count))
