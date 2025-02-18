def spy_game(nums):
    pattern = [0, 0, 7]
    for num in nums:
        if num == pattern[0]:
            pattern.pop(0)
        if not pattern:
            return True
    return False

spy_game([1,2,4,0,0,7,5]) #True
spy_game([1,0,2,4,0,5,7]) #True
spy_game([1,7,2,0,4,5,0]) #False

print(spy_game([1,2,4,0,0,7,5])) #True
print(spy_game([1,0,2,4,0,5,7])) #True
print(spy_game([1,7,2,0,4,5,0])) #False