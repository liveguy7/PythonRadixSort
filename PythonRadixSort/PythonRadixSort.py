import sys

def radixSort(nums):
    RADIX = 10
    placement = 1
    maxDigits = max(nums)
    while(placement < maxDigits):
        buckets = [list() for i in range(RADIX)]
        for i in nums:
            tmp = int((i/placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                nums[a] = i
                a = a + 1
        placement = placement * RADIX

    return nums

user_input = input("Input numbers separated by a comma:\n").strip()
nums = [int(i) for i in user_input.split(',')]
print(radixSort(nums))

