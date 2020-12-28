text_file = open("fighterName.txt", "r")
lines = text_file.readlines()
print(lines[0:10])
text_file.close()
