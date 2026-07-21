# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node=l1
        node2=l2
        l_1=""
        l_2=""
        while node:
            l_1=l_1+str(node.val)
            node=node.next
        while node2:
            l_2=l_2+str(node2.val)
            node2=node2.next
        l_1 = l_1[::-1]
        l_2 = l_2[::-1]
        result = int(l_1)+int(l_2)
        num_str = str(result)
        num_str=num_str[::-1]
        digits = [int(d) for d in num_str]
        head = ListNode(digits[0])
        current=head
        for i in digits[1:]:
            print(i)
            current.next=ListNode(i)
            current=current.next
        return head