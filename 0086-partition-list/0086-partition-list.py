class Solution:
    def partition(self, head, x):
        # Dummy nodes
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)

        # Pointers for the two lists
        small = small_dummy
        big = big_dummy

        current = head

        while current:
            if current.val < x:
                small.next = current
                small = small.next
            else:
                big.next = current
                big = big.next

            current = current.next

        # Connect the two lists
        small.next = big_dummy.next

        # Very important: end the big list
        big.next = None

        return small_dummy.next