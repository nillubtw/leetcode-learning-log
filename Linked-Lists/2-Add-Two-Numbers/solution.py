# Approach: Integer conversion using linked list traversal
# Time: O(n + m)
# Space: O(n + m)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # These will store the integer values represented by the linked lists
        # These will store the integer values represented by the linked lists
        num1=0
        num2=0
      
        # Traverse the first linked list (l1)
        # We use a 'curr' pointer so we don't lose the head of the list
        curr=l1
        power=0 #Track place value (1s, 10s, 100s) since we can't use len()
        while curr:
            num1+= curr.val * 10**power
            curr = curr.next
            power+=1
          
        #Traverse the second linked list (l2)
        curr=l2
        power=0
        while curr:
            num2+= curr.val * 10**power
            curr = curr.next
            power+=1

        #Calculate the sum of both numbers
        result = num1+num2
        # Convert to string and reverse
        # We reverse it because the output expects the 1s place at the head
        resultrev = str(result)[::-1]
      
        # Use a Dummy Node as an 'anchor' to build the new result chain
        dummy = ListNode(0) 
        # 'curr' now acts as our hand, attaching new nodes to the dummy
        curr = dummy
      
        for digit in resultrev:
            # Create a new ListNode for the digit and link it to our chain
            curr.next = ListNode(int(digit))
            # Move our 'hand' to the newly created node
            curr = curr.next
         #Return everything after the dummy (the actual head of the result)
        return dummy.next
        
