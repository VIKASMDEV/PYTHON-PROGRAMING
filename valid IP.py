"""
1. Imagine you are working on a network configuration tool for a company. This tool needs to validate the IPv4 addresses entered by users to ensure they are correctly formatted before saving them in the system. An incorrectly formatted IP address could lead to network connectivity issues, making validation a crucial part of the tool.
Input: "222.111.111.111"
Output: true
Explanation: All parts are numeric and within the range 0-255.

Input: "5555..555"
Output: false
Explanation: The address is not properly split into 4 parts, and it contains empty parts.

Input: "0.0.0.255"
Output: true
Explanation: All parts are numeric and within the range 0-255.

Input: "0.0.0.0255"
Output: false
Explanation: The last part 0255 is not a valid representation of an IP address segment. Although 255 is within the range, the leading zero makes it invalid.
"""
a=input("Enter the IP :")
b = []
s=""
flag=0
c=0
for i in a:
    if i.isnumeric():
        s=s+i
        c=0
        #print(s)
    elif i=="." and c==0:
        b.append(s)
        s=""
        c+=1
    else:
        flag = 1
b.append(s)
for i in b:
    if int(i) not in range (0,225):
        print(f"{i} invalid")
        flag=1
    if len(b)>=4:
        print("length extended")
        flag=1
    if c>=2:
        print("invalid format")
        flag=1
if flag==0:
    print("IP VALID")
else :
    print("Invalid")
        
    
     
        
        
