class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):                 # Leetcode : 141
    if not head or not head.next:   # If head is empty return False
        return False
    
    slow, fast = head, head         # create slow and fast pointers
    
    while fast and fast.next:       # go through the linkedlist to check loop
        slow = slow.next            # increment one step
        fast = fast.next.next       # increment two steps
        if slow == fast:            # if the slow and faster pointers meet 
            return True             # there's a loop 
    return False                    # else return false

# Revised Today ( 30 AUG 2025 )