f1 = open(r"C:\Users\student\Downloads\Example.txt","r")
f2 = open(r"C:\Users\student\Downloads\Example2.txt","r")

data1 = f1.read()
data2 = f2.read()

f1.close()
f2.close()

f3 = open(r"C:\Users\student\Downloads\merged.txt","w")
f3.write(data1)
f3.write(data2)
f3.close()

print("Files merged into merged.txt")
