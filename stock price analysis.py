"""
3. You are building a stock price analysis tool. One feature of this tool is to find the next greater price for each day's stock price in an array of daily stock prices. Write a function that takes an array of daily stock prices as input and returns an array where each element is replaced by the next greater element to its right. If there is no greater element, replace it with -1.
Note using recursion.
Example Inputs and Outputs
Input: int[] arr = {6, 8, 0, 1, 3}
Output: [8, -1, 1, 3, -1]
Input: int[] arr = {1, 3, 2, 4}
Output: [3, 4, 4, -1]
Input: int[] arr = {10, 20, 30, 50}
Output: [20, 30, 50, -1]
Input: int[] arr = {50, 40, 30, 10}
Output: [-1, -1, -1, -1]
"""
def takingvalues():
    b=[]
    maxnum=int(input("enter the no of numbers u want to enter : "))
    for i in range(maxnum):
        a=input("enter the stock prices of day 1 : ")
        b.append(a)

def checkgret():
    c=[]
    for i in b:
        for j in b:
            if i<j:
                c.append(j)
                
            
