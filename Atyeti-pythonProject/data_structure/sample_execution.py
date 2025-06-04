"""
Fibonaci series
    def fibonaci(self , num):

        fibo_list = []
        x = 0
        y = 1
        inter = 0


        for i in range(num):
            fibo_list.append(x)
            x , y = y , x+y

        return fibo_list
-----------------------------------------------------------
list/array median

    def array_median(self , list1 , list2):

        final_list = list1 + list2
        final_list.sort()
        len(final_list)

        if len(final_list) % 2 != 0:
            return final_list[(len(final_list)//2)]
        else:
            return (final_list[(len(final_list)//2 - 1)] + final_list[(len(final_list)//2)])/2

-----------------------------------------------------------------------------------------------

list1 - [1,2,3]
list2 - ["one" , 'two' , 'three']

output - dict - {1: "one", 2:"two" , 3: "three"}

        final = dict(zip(list1, list2))
        return final

or
        dict = {}

        for i in range(len(list1)):
            for j in range(len(list2)):
                if i == j:
                    key = list1[i]
                    value = list2[j]
                    dict[key] = value

        return dict
------------------------------------------------------------------
name1 = sham
name = ram

"a" "m"

list = []

        for i in str1:
            for j in str2:
                if i == j:
                    if i in list:
                       pass
                    else:
                        list.append(i)
        return list




"""





class solution():
    def removeDuplicates(self, nums):

        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i+=1

        return i, nums

nums = [1,2,2,3,3,4,4,5]
sol = solution()
print(sol.removeDuplicates(nums))
