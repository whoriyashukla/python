
with open("riya.txt", mode='w') as file:
    file.write("this is a new file called riya.txt\n")
    file.write("Hello, world!")

with open("riya.txt", mode='r') as file:
    print(file.read())