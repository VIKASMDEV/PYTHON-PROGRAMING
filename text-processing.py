"""
2. You are developing a text-processing application that needs to analyze strings for palindromic substrings. A palindromic substring is a substring that reads the same forward and backward. Write a function that takes a string S as input and returns the number of distinct palindromic substrings in S.
Input: Madam Arora teaches Malayalam
Output: 3
Input: Nitin speaks Malayalam
Output: 2
"""
def adding(a):
    b = []
    s=""
    c=0
    for i in a:
        if i != " ":
            s=s+i
            c=0
        elif i==" " and c==0:
            b.append(s)
            s=""
            c+=1
        else:
            continue
    b.append(s)
    print(b)
    return b
def checkpali(b):
    co=0
    for i in b:
        if i[::-1]==i:
            #print("palindrome")
            co+=1
        #else :
            #print(f"{i} is not a palindrome")
    print("Count : ",co)
        
    

a=str(input("Enter the string :"))
l=adding(a)
checkpali(l)

