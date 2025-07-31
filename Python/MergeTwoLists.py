class ListNode:                                     # Leetcode : 21
    def __init__(self, val=0, next=None):           # class definition for the linked list
        self.val = val                              # already present inside leetcode no need to define again
        self.next = next                            # while submitting the answer.

def mergeTwoLists(list1,list2):                     
    if list1 is None and list2 is None:             # this is to identify if a list is empty
        return None                                 # if both are empty return None
    elif list1 is None:                             # if list1 is empty return list2
        return list2
    elif list2 is None:                             # else if list2 is empty return list1
        return list1
    
    current1 = list1                                # create a instance of list1 and list2
    current2 = list2
    if current1.val <= current2.val:                # identify the smallest value and add to the result_list
        result_list = ListNode(current1.val)    
        current1 = current1.next                    # this is done at first to create the result node
    else:
        result_list = ListNode(current2.val)        
        current2 = current2.next

    result = result_list                            # create a instance for result_list to traverse 
    while current1 and current2:                    
        if current1.val <= current2.val:            # here both the lists would be traversed to find
            result.next = ListNode(current1.val)    # the smallest val to add to the linkedlist
            result = result.next
            current1 = current1.next
        else:
            result.next = ListNode(current2.val)
            result = result.next
            current2 = current2.next
    while current1:                                 # this list is used to add the left over values inside
        result.next = ListNode(current1.val)        # the list
        current1 = current1.next
        result = result.next
    while current2:                                 # another loop to add the left over values to the 
        result.next = ListNode(current2.val)        # result_list
        current2 = current2.next
        result = result.next
    
    return result_list

list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))
result = mergeTwoLists(list1,list2)
current = result
while current:
    print(current.val)
    current = current.next

# Revised today ( 18 JUL 2025 )
# Revised today ( 24 JUL 2025 )
# Revised today ( 31 JUL 2025 )