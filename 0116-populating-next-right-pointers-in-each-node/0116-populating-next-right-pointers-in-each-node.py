class Solution:
    def connect(self, root):
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                # Connect left child to right child
                current.left.next = current.right

                # Connect right child to next parent's left child
                if current.next:
                    current.right.next = current.next.left

                current = current.next

            # Move to the next level
            leftmost = leftmost.left

        return root