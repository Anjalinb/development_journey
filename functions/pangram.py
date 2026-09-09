def is_pangram(word):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for ch in alphabet:
        if ch not in word.lower():
            print(False)
            break
    else:
        print(True)

is_pangram("hello")

is_pangram("the quick brown fox jumps over laZy dog")