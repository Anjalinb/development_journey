try:
    fr=open("error_handling\\read_keywords.txt")
    for line in fr:
        print(line)

except Exception as e:
    print(e)

finally:
    print("db commit")