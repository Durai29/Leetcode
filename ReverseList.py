class ListNode():                               # Leetcode : 206
    def __init__(self,val,next):                # definition of LinkedList
        self.val = val                          # This is already defined in Leetcode no need to 
        self.next = next                        # define again in leetcode.
    
def reverseList(head):                          # Here is the reverselist method
    current = head                              # first we go through the linked list and
    lst = []                                    # store all the values inside this array
    while current:                              
        lst.append(current.val)                 # Then we can access the list values to create 
        current = current.next                  # a new linked list

    if not lst:                                 # if lst is empty return None
        return None                             # ( Edge Case )
    
    result = ListNode(lst[-1],None)             # now create a node with the last element of the list as head
    current = result                            # create a dummy
    for i in lst[-2::-1]:                       # now except the last values (5) go through all values from right
        current.next = ListNode(i,None)         # in reverse order.
        current = current.next                  # this helps us to create a proper linkedlist without any extra node
    return result

# testcase validation
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
result = reverseList(head)
current = result
while current:
    print(current.val)
    current = current.next