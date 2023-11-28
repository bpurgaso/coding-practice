'''
Platform: Leet Code
Question: 23. Merge k Sorted Lists
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> [ListNode]:
        """
        Merge k sorted linked lists into one sorted list.

        Complexity:
            O(nk) time where n is the average length of the lists and k the number of lists.

        Args:
            lists (list[ListNode]): A list of ListNode objects representing the head nodes of the k sorted lists.

        Returns:
            ListNode: The head node of the merged sorted list.
        """
        merged_list = [ListNode]

        # get the first node in each list
        tmp_head = tmp = ListNode()

        # while any of the lists have a next node
        while True:
            # get the minimum value of the current nodes
            try:
                min_value = min(node.val for node in lists if node is not None)
            except ValueError:
                return tmp_head.next

            # get the index of the minimum value
            for x in lists:
                if x is not None and x.val == min_value:
                    min_index = lists.index(x)
                    break
            
            # move the node to the merged list
            tmp.next = lists[min_index]
            tmp = lists[min_index]
            
            # pop the node with minimum value
            if lists[min_index].next is None:
                del lists[min_index]
            else:
                lists[min_index] = lists[min_index].next
                
            
                
                

if __name__ == '__main__':
    solution = Solution()

    # create the lists
    raw_input = [[1,4,5],[1,3,4],[2,6]]
    input_lists = []
    for i in raw_input:
        tmp_head = tmp = ListNode()
        for j in i:
            tmp.next = ListNode(j)
            tmp = tmp.next
        input_lists.append(tmp_head.next)
    
    #print(solution.mergeKLists(input_lists))
