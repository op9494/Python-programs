c= input()
if (c=='A' or c=='a' or c=='E' or c=='e' or c=='I'
 or c=='i' or c=='O' or c=='o' or c=='U' or c=='u'):

    print("Vowel") 
elif ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')): 
     print("Consonant")
else:
    print("invalid")

