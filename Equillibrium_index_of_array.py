def EquilibriumIndex(array):
    totalsum=sum(array)
    left_sum=0
    for i in range(len(array)):
        totalsum-=array[i]
        if left_sum==totalsum:
            return i
        left_sum+=array[i]
    return -1


array = list(map(int, input().split()))
print(EquilibriumIndex(array))

        