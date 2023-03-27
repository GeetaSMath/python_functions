# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Given an integer array nums and an integer val, remove all occurrences of
# val in nums in-place. The relative order of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
#
# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.
#
# int k = removeElement(nums, val); // Calls your implementation
#
# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# Example 1:
#
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


def remove_elemets(nums, val):
    x = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[x] = nums[i]
            x += 1
    return x


nums = [3, 2, 2, 3]
val = 3
expected = [2, 2]
x = remove_elemets(nums, val)

assert x == len(expected)
nums[:x] = sorted(nums[:x])

for i in range(x):
    assert nums[i] == expected[i]

print(x)
print(nums)
