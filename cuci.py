files = open('files/txt.txt','a+')

files.write("OHIO MIINA\n")
files.seek(0)

print(files.read())


files.close()
