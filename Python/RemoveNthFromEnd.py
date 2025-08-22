class ListNode:                             # Leetcode : 19
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0,head)                # Create a dummy node to point to the head
    slow = fast = dummy                     # create 2 pointers slow and fast

    for _ in range(n+1):                    # use for loop to make the fast pointer move
        fast = fast.next                    # before the slow pointer n+1 (coz : start -> 0) steps ahead 
    
    while fast:                             # now increment other pointers until fast is valid
        fast = fast.next                    
        slow = slow.next                    # a gap of length n would have been created 
                                            # that's what we need to remove the nth node
    slow.next = slow.next.next              # remove the nth node from the last

    return dummy.next                       # return head, dummy is pointing to head

answer = removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),2)    

# Revised Today ( 21 AUG 2025 )