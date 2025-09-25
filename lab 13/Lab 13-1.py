f = open(r"C:\Users\student\Downloads\example.txt","r")
data = f.read()
f.close()

lines = data.split("\n")
words = data.split()
chars = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Chars:", chars)
