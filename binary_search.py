def binary_search(nums,s, e, target):
    if len(nums[s:]) == 1:
            index = s if target == nums[s] else -1
            return index
    mid = (s + e)//2
    print([s,e,' mid:', mid])
    if nums[mid] == target:
        print('equal')
        return mid
    elif nums[mid] < target:
        print('right')
        return binary_search(nums, mid + 1, e, target)
    else:
        print('left')
        return binary_search(nums, s, mid - 1, target)

if __name__ == "__main__":
    test = [-1,0,3,5,9,12]
    target = -2
    print(binary_search(test, 0, len(test)-1, target))
            
