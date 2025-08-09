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

# Revised today ( 17 JUL 2025 )

def reverseList(head):                  # Leetcode : 206
    current = head                      # create a pointer for current node
    prev = None                         # create a pointer to hold previous val
    while current:                      # loop through until current
        next_temp = current.next        # store next value of current here
        current.next = prev             # current.next would be prev
        prev = current                  # then store the current value in prev
        current = next_temp             # then increment the current Node
    return prev                         # return prev

# Revised today ( 25 JUL 2025 )
# Revised today ( 09 AUG 2025 ) 