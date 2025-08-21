class ListNode:                                 # Linked list definition
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val} -> {repr(self.next)}" # Best for visualisation in debugger

def reorderList(head):                          # Leetcode : 143
    slow, fast = head, head                     # create a fast and slow pointer

    while fast and fast.next:                   # implementation of fast and slow pointer
        slow = slow.next                        # increment slow pointer to one step
        fast = fast.next.next                   # increment fast pointer to two step
                                                # split linkedlist into half

    prev = None                                 # create 3 pionters to store all three
    current = slow.next                         # values. Before, current and after.
    slow.next = None                            

    while current:                              # reverse the second half 
        next_temp = current.next                # after reversing the list would be 
        current.next = prev                     # merged to form a single list
        prev = current                          # No additonal memory is used in this method
        current = next_temp                     # values are swapped in place

    first = head                                # create a pointer to access the first 
    second = prev                               # and last half
    while second:                               # Merge both the list into a single list
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
    
    return head                                 # return the head

answer = reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
# print(answer)

# while answer:
#     print(answer.val)
#     answer = answer.next
print(answer)                                   # Just do this instead

# Revised Today ( 27 JUL 2025 )
# Revised Today ( 21 AUG 2025 )