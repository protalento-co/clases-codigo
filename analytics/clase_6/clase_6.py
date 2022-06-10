# 1)
# Array montaña (mountain array)


def mountain_validator(arr):
    pico = False
    pico_n = 0
    for i in range(1, len(arr)-1):
        actual = arr[i]
        anterior = arr[i-1]
        siguiente = arr[i+1]
        if (actual >= anterior) and (actual >= siguiente):
            pico_n += 1
            # pico_n = pico_n + 1
            # variable += otra_variable
            # variable = variable + otra_variable
            # *=
            # -=
            # /=
            # if (pico):
            #     return False
            # else:
            #     pico = True
            pico = True
    # return pico, pico_n
    return pico_n == 1


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Example 3:
# Input: nums = [3, 2, 4], target = 8
# Output: [-1, -1]

def suma_objetivo(arr, objetivo):
    for i in arr:
        for j in arr:
            print(i, j)


if __name__ == "__main__":
    # m_valid = [0, 1, 4, 6, 8, 7, 5, 4, 1]
    # m_invalid = [0, 1, 4, 6, 8, 7, 10, 8, 1]
    # print(mountain_validator(m_valid))
    # print(mountain_validator(m_invalid))
    nums = [2, 7, 11, 15]
    target = 9
    suma_objetivo(nums, target)
