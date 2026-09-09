text="england won by 6 wickets with 3 balls remaining. england leads the series with 2-1."
alpha_count=0
digit_count=0
sp_char=0
for ch in text:
    if ch.isalpha():
        alpha_count+=1
    elif ch.isdigit():
        digit_count+=1
    else:
        sp_char+=1

print("Alphabet count=",alpha_count)
print("Digit count=",digit_count)
print("Special character count=",sp_char)