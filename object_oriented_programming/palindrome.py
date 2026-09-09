class Palindrome:
    def solution(self,word):
        result=True
        left=0
        right=len(word)-1
        word=list(word)
        while(left<right):
            word[left],word[right]=word[right],word[left]
            left+=1
            right-=1

        print(word)
        return result

pal_instance=Palindrome()
pal_instance.solution("madam")
    
    




        







       
       

pal_instance=Palindrome()