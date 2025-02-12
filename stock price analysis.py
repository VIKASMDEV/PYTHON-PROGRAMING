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
def find_next_greater(prices):
 
    n = len(prices)
    result = [-1] * n  # Initialize result list with -1

    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] > prices[i]:
                result[i] = prices[j]
                break  # Found the next greater, move to the next price
    return result


if __name__ == "__main__":
    
    size = int(input(f"Enter the number of days: "))
        
    prices = []
    print(f"Enter the stock prices for {size} days:")
    for _ in range(size):
        price = int(input())
        prices.append(price)
        #print(prices)

    result = find_next_greater(prices)
    print("Next greater prices:", *result)  # * unpacks the list for printing


                
            
