def runningSum(nums): # Задан массив nums.
    # Мы определяем текущую сумму массива как runningSum[i] = sum(nums[0]…nums[i])
    runningSum = []
    runningSum.append(nums[0])
    for i in range(1,len(nums)):
        count=0
        for j in range(i+1):
            count += nums[j]
        runningSum.append(count)
    return runningSum

def pivotIndex( nums): # Учитывая массив целых nums чисел, вычислите сводный индекс этого массива.
        if sum(nums[1::]) == 0:
            return 0
        else:           
            for i in range(1,len(nums)-1):
                sum_left = sum(nums[:i:])
                sum_right = sum(nums[i+1::])
                if sum_left == sum_right:
                    return i
        if sum(nums[:len(nums)-1:]) == 0:
            return len(nums)-1
        else:
            return -1