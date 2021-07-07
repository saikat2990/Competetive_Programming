class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList():
    def __init__(self):
        self.headval = None

class Solution(object):
    def swapPairs(head):
        listHead = LinkList()
        if len(head) >0:
            listHead.headval = ListNode(head[0])
            head.pop(0)
        traverseNode = listHead.headval
        for nodeVal in (head):
            traverseNode.next = ListNode(nodeVal)
            traverseNode = traverseNode.next

        printNode = listHead.headval
        while printNode and printNode.next is not None:
            tempNode = printNode.val
            printNode.val = printNode.next.val
            printNode.next.val = tempNode
            printNode = printNode.next
            printNode = printNode.next

        return listHead.headval