class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1,l2):                   # Leetcode : 2
    result = ListNode()                     # create an object of ListNode class
    current = result                        # create a dummy instance of result to monitor the currect Node
    carry = 0                               # variable to keep note of carry in summation
    while l1 or l2 or carry:                # allow only if the exist l1 or l2 or carry
        v1 = l1.val if l1 else 0            # extract value from l1 and l2
        v2 = l2.val if l2 else 0
        
        total = v1 + v2 + carry             # make the summation
        carry = total // 10                 # take out the carry
        current.val = total % 10            # take out the remainder and assign to current node value

        l1 = l1.next if l1 else None        # move to next node only if the next node exist
        l2 = l2.next if l2 else None        

        if l1 or l2 or carry:               # create new node for the result if, only there exist l1 or l2 or carry
            current.next = ListNode()
            current = current.next 
    while result:                           
        print(result.val)
        result = result.next
    return result                           # return result
l1 = ListNode(2,ListNode(4,ListNode(3,ListNode(1,ListNode(2)))))
l2 = ListNode(5,ListNode(6,ListNode(4)))
print(addTwoNumbers(l1,l2))