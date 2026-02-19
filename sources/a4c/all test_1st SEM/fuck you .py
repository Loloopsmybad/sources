a=0
s=0
vowel="aeiou"
for i in range(len(s)):
            if s[i] in vowel :
                a+=1
            else:
                s+=1
print(a+s)