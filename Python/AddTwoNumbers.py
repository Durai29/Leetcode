# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next

# def addTwoNumbers(l1,l2):                   # Leetcode : 2
#     result = ListNode()                     # create an object of ListNode class
#     current = result                        # create a dummy instance of result to monitor the currect Node
#     carry = 0                               # variable to keep note of carry in summation
#     while l1 or l2 or carry:                # allow only if the exist l1 or l2 or carry
#         v1 = l1.val if l1 else 0            # extract value from l1 and l2
#         v2 = l2.val if l2 else 0
        
#         total = v1 + v2 + carry             # make the summation
#         carry = total // 10                 # take out the carry
#         current.val = total % 10            # take out the remainder and assign to current node value

#         l1 = l1.next if l1 else None        # move to next node only if the next node exist
#         l2 = l2.next if l2 else None        

#         if l1 or l2 or carry:               # create new node for the result if, only there exist l1 or l2 or carry
#             current.next = ListNode()
#             current = current.next 
#     while result:                           
#         print(result.val)
#         result = result.next
#     return result                           # return result
# l1 = ListNode(2,ListNode(4,ListNode(3,ListNode(1,ListNode(2)))))
# l2 = ListNode(5,ListNode(6,ListNode(4)))
# print(addTwoNumbers(l1,l2))

# My solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val} -> {repr(self.next)}"

def addTwoNumbers(l1,l2):                       # Leetcode : 2
    first, second = l1, l2                      # create 2(first & second) pointers for both the lists
    front, back = 0, 0                          # to track the carry and sum
    while first and second:                     # loop through the 2 linkelists
        sum = first.val + second.val + front    # take the sum of 2 numbers with the carry
        back = sum % 10                         # extract the last number
        first.val = back                        # store the back value in list1
        front = sum // 10                       # extract the carry outof sum
        first = first.next                      # increment both lists
        second = second.next                    # Here we use inplace operation without and extra space
    while first:                                
        sum = first.val + front                 # If list1 remains :
        back = sum % 10                         # same rule but without list2
        first.val = back 
        front = sum // 10
        first = first.next
    if second:                                  # we are solving this problem by storing the answer in list1
        first = l1                              # so first we need to know the last position of list1 to add new nodes
        while first.next:                       # create another new pointer and find the last element's position
            first = first.next
        while second:                           # now do the same operation that we performed with only list1 case
            sum = second.val + front            
            back = sum % 10
            first.next = ListNode(back)         # but there is a small change we don't store in list2 but list1 (remember: answer -> list1)
            first = first.next
            front = sum // 10
            second = second.next
    if front != 0:                              # finally if there a remainder
        cur = l1                            
        while cur.next:                         # find the last element's position in list1
            cur = cur.next
        cur.next = ListNode(front)              # create a node and add it the last with the value of carry
    return l1                                   # return l1

l1 = ListNode(3,ListNode(7))
l2 = ListNode(9,ListNode(2))
answer = addTwoNumbers(l1,l2)
print(answer)

# Revised Today (30 JUL 2025)