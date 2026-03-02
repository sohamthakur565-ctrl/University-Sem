String=input("Enter the string: ")
vowel=['a','e','i','o','u','A','E','I','O','U']
count_vowel=0
count_consonent=0
for i in range(0,(len(String)),1):
    if String[i] in vowel:
        count_vowel+=1
    else:
        count_consonent+=1
print(String,"have:","\nVowel:",count_vowel,"\nConsonent:",count_consonent)
