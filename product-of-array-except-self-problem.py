#Problem: Product of Array Except Self
#Description

#Given an array nums, return an array output such that output[i] is the product of all elements in nums except nums[i].

#Solve without using division

#Must run in O(n) time and O(1) extra space (excluding output array)

#Medium difficulty, common in interviews




def product_except_self(nums):
    n = len(nums)
    output = [1]*n

    # calculate prefix product
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # calculate suffix product and multiply
    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    nums = [1,2,3,4]
    print("Product except self:", product_except_self(nums))
