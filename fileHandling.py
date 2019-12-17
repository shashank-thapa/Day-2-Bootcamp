with open('sample.txt') as file:
    lines = file.readlines()
    for line in lines:
        print(line.capitalize())
    