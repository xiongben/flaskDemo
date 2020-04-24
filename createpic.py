#-*- coding=utf-8 -*-
# import numpy as np
# import matplotlib.pyplot as plt


# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([3,5,7,6,2,6,10,15])
# plt.plot(x,y,'r')
# plt.plot(x,y,'g',lw=10)
# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([13,25,17,36,21,16,10,15])
# plt.bar(x,y,0.2,alpha=1,color='b')
# plt.show()

# nums = [2,7,11,15]
# target = 9

# def way1(nums, target):
#     num_dict = {nums[i]: i for i in range(len(nums))}
#     num_dict2 = {i: target - nums[i] for i in range(len(nums))}
#     result = []
#     for i in range(len(nums)):
#         j = num_dict.get(num_dict2.get(i))
#         if(j is not None) and (j != i):
#             result = [i,j]
#             break
#     print result

# way1(nums,target)

# def bubbleSort(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-i-1):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#     return nums


# data_set = [1,9,22,31,45,3,6,2,11]
# # smallest_num_index = 0
# loop_count = 0
# for j in range(len(data_set)-1):
#     smallest_num_index = j
#     print ("smallindex:",smallest_num_index)
#     for i in range(j+1,len(data_set)):
#         if data_set[i] < data_set[smallest_num_index]:
#             smallest_num_index = i
        
#     print("smallest num is ",data_set[smallest_num_index])
#     tmp = data_set[smallest_num_index]
#     data_set[smallest_num_index] = data_set[j]
#     data_set[j] = tmp
#     loop_count += 1
#     print("the %d times order:%s"%(loop_count,data_set))
# print data_set
# print("loop times ",loop_count)




nums = [7,9,3,6,5]
# for index in range(1,len(nums)):
#     current_val = nums[index]
#     positon = index
#     while positon > 0 and nums[positon-1] > current_val:
#         nums[positon] = nums[positon-1]
#         positon -=1
#     nums[positon] = current_val
#     print nums


# def quick_sort(array,left,right):
#     if left >= right:
#         return
#     low = left
#     high = right
#     key = array[low]
#     while low < high:
#         while low < high and array[high]>key:
#             high -= 1
#         array[low] = array[high]
#         array[high] = key
#         print ('aa: ',array)
#         while low < high and array[low] <= key:
#             low += 1
#         array[high] = array[low]
#         array[low] = key
#         print ('bb: ',array)
#     quick_sort(array,left,low-1)
#     quick_sort(array,low+1,right)

# quick_sort(nums,0,len(nums)-1)
# print nums

import time,random

# class TreeNode(object):
#     def __init__(self,data=0,left=0,right=0):
#         self.data=data
#         self.left=left
#         self.right=right

# class BTree(object):
#     def __init__(self,root=0):
#         self.root=root

#     def preOrder(self,treenode):
#         if treenode is 0:
#             return
#         print(treenode.data)
#         self.preOrder(treenode.left)
#         self.preOrder(treenode.right)

#     def inOrder(self,treenode):
#         if treenode is 0:
#             return
#         self.inOrder(treenode.left)
#         print(treenode.data)
#         self.inOrder(treenode.right)

#     def postOrder(self,treenode):
#         if treenode is 0:
#             return
#         self.postOrder(treenode.left)
#         self.postOrder(treenode.right)
#         print(treenode.data)


# n1 = TreeNode(data=1)
# n2 = TreeNode(2,n1,0)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5,n3,n4)
# n6 = TreeNode(6,n2,n5)
# n7 = TreeNode(7,n6,0)
# n8 = TreeNode(8)
# root = TreeNode('root',n7,n8)
# bt = BTree(root)

# print("preOrder".center(50,'-'))
# print(bt.preOrder(bt.root))

# print("inOrder".center(50,'-'))
# print (bt.inOrder(bt.root))

# print("postOrder".center(50,'-'))
# print (bt.postOrder(bt.root))


# source = [random.randrange(10000+i) for i in range(20)]
# print source

# step = int(len(source)/2)

# while step > 0:
#     print("======step======",step)
#     for index in range(0,len(source)):
#         if index + step < len(source):
#             current_val = source[index]
#             if current_val > source[index+step]:
#                 source[index],source[index+step] = source[index+step],source[index]
#     step = int(step/2)
# else:
#     for index in range(1, len(source)):
#         current_val = source[index]
#         position = index
#         while position > 0 and source[position - 1] > current_val:
#             source[position] = source[position - 1]
#             position -= 1
#         source[position] = current_val
#     print(source)


def heap_sort(lst):
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root],lst[child] = lst[child],lst[root]
                root = child
            else:
                break

    for start in xrange((len(lst)-2)//2,-1,-1):
        sift_down(start,len(lst)-1)

    for end in xrange(len(lst)-1,0,-1):
        lst[0],lst[end] = lst[end],lst[0]
        sift_down(0,end - 1)
    
    return lst


def testfn():
    l = [9,2,1,7,6,8,5,3,4,3]
    res = heap_sort(l)
    print res


testfn()
            