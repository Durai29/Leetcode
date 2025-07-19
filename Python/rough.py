class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1,list2):
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    
    current1 = list1
    current2 = list2
    if current1.val <= current2.val:
        result = ListNode(current1.val)
        current1 = current1.next
    else:
        result = ListNode(current2.val)
        current2 = current2.next

    cur_res = result

    while current1 and current2:
        if current1.val <= current2.val:
            cur_res.next = ListNode(current1.val)
            current1 = current1.next
            cur_res = cur_res.next
        else:
            cur_res.next = ListNode(current2.val)
            current2 = current2.next
            cur_res = cur_res.next

    while current1:
        cur_res.next = ListNode(current1.val)
        current1 = current1.next
    while current2:
        cur_res.next = ListNode(current2.val)
        current2 = current2.next

    return result


result = mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))),ListNode(1,ListNode(3,ListNode(4))))

while result:
    print(result.val)
    result = result.next