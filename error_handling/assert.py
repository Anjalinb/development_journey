def is_palindrome(word):
    result=word==word[::-1]
    return result
try:
    assert is_palindrome("dad")==True,"test case 1 failed"
    assert is_palindrome("tan")==False,"test case 2 failed"
    assert is_palindrome("malayalam")==True,"test case 3 failed"
except:
    print("error")
else:
    print("success")
