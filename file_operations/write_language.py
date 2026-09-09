languages=['python','java','javascrpt','c#','c++']
fw=open("file_operations\\languages.txt","w")

for l in languages:
    fw.write(l+'\n')

print("Write completed")