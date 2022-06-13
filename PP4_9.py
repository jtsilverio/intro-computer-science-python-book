file = "PP4_9.txt"

# Print only lines that contains a certain substring
def myGrep(file, substring):
    file = open(file)
    for line in file:
        if substring in line:
            print(line, end = '')
    
myGrep(file, "line")