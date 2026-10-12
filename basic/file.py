with open("Sample.txt","w") as file:
    file.write("Hello Python")

with open("Sample.txt","r") as file:
    print(file.read())