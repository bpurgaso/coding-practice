# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> [ListNode]:
        merged_list = [ListNode]

        # get the first node in each list
        tmp_head = tmp = ListNode()

        # while any of the lists have a next node
        while any(node for node in lists if node is not None):
            
            # get the minimum value of the current nodes
            #print(f"lists: {lists}")
            min_value = min(node.val for node in lists if node is not None)
            #print(f"min_value: {min_value}")

            # get the index of the minimum value
            for x in lists:
                if x is not None and x.val == min_value:
                    min_index = lists.index(x)
                    break
            
            # move the node to the merged list
            tmp.next = lists[min_index]
            tmp = lists[min_index]
            
            # pop the node with minimum value
            lists[min_index] = lists[min_index].next
            #print(f"lists [end]: {lists}")

        #print(f"lists [Final]: {lists}")
        return tmp_head.next
                
            
                
                

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
    
    print(solution.mergeKLists(input_lists))
