'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
https://leetcode.com/problems/reverse-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        
        return prev
        