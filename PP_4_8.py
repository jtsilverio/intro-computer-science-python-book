file = "PP4_9.txt"

# removes punctuations from a file
def words(file):
    file = open(file)

    content = file.read()
    changes = content.maketrans("!,.:;?","      ")
    
    return content.translate(changes).lower()

text = words(file)
print(text)
