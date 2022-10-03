# how it works ?
    #returns the sum of unique elements from list
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.


def sumOfUnique(nums):              #function
        s=0                         #counter value
        for i in nums:              #for loop to count unique iterations
            if nums.count(i)==1:
                s=s+i               #append new value to count
        return s

# Driver program to test above function
if __name__=='__main__':
    nums = [1,2,3,2]
    print(sumOfUnique(nums))