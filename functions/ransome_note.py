def is_ransome(note,magazine):
    for ch in note.lower():
        if ch not in magazine:
            print(False)
            break
    else:
        print(True)

is_ransome("hi","hill")
is_ransome("hens","chicken")