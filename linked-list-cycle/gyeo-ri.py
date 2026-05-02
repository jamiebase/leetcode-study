# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        visited_nodes = set()
        while head is not None:
            if head in visited_nodes:
                return True

            visited_nodes.add(head)
            head = head.next
        return False


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ]

    solution = Solution()

    for idx, (inp, pos, expected) in enumerate(test_cases, start=1):
        head = None
        nodes = []

        for value in reversed(inp):
            head = ListNode(value, head)

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        if pos != -1 and nodes:
            nodes[-1].next = nodes[pos]

        result = solution.hasCycle(head)

        assert (
            result == expected
        ), f"Test Case {idx} Failed: Expected {expected}, Got {result}"

    print("All test cases passed.")
