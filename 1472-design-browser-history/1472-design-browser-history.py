class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        # self.tail = self.head

        self.curr = self.head

    def visit(self, url: str) -> None:
        new_node = ListNode(url)

        # new_node.next = self.curr.next
        if self.curr.next:
            self.curr.next.prev = new_node

        self.curr.next = new_node
        new_node.prev = self.curr

        self.curr = new_node


        # self.tail.next = new_node
        # new_node.prev = self.tail
        # self.tail = new_node
        

        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        print("")

    def back(self, steps: int) -> str:
            tempb = self.curr
            i = 0
            while i != steps and tempb.prev:
                tempb = tempb.prev
                i += 1
            
            self.curr = tempb
            return tempb.val

    def forward(self, steps: int) -> str:
            
            tempf = self.curr
            i = 0
            while i != steps and tempf.next:
                tempf = tempf.next
                i += 1
            
            self.curr = tempf

            return tempf.val
        
 
    
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)