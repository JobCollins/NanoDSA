#implement a linked list using the concept of nodes
# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval=None

class LinkedList:
    def __init__(self):
        self.headval=None

    # traverse a linked list
    #only in forward direction for singly lists
    #from the first data element
    def listprint(self):
        #first data element
        printval = self.headval

        #print next element by assigning the pointer
        #of the next node to the current data element
        while printval is not None:
            print(printval.dataval)
            #assign pointer of next node to current element
            printval = printval.nextval

    def insertAtBeginning(self, newdata):
        # involves pointing the next pointer of the new data node to the current head 
        # of the linked list. So the current head of the linked list becomes the second
        # data element and the new node becomes the head of the linked list.
        newNode = Node(newdata)

        # update the new node's next val to current head val
        newNode.nextval = self.headval
        # make the new node the new head val
        self.headval = newNode

    def insertAtEnd(self, newdata):
        # involves pointing the next pointer of the the current last node of the linked list 
        # to the new data node. So the current last node of the linked list becomes the second last
        # data node and the new node becomes the last node of the linked list.
        newNode = Node(newdata)

        if self.headval is None: #if the linked list is empty
            self.headval = newNode #add the node to the list
            return

        #assign current element to last variable
        last = self.headval
        while(last.nextval): #check whether there's an element next to it
            last = last.nextval #assign that element to last and repeat
        last.nextval=newNode #when there is no next element above add the newNode

    def insertBetween(self, left_node, new_data):
        # involves changing the pointer of a specific node to point to the new node. 
        # That is possible by passing in both the new node and the existing node 
        # after which the new node will be inserted. 
        # So we define an additional class which will change the next pointer 
        # of the new node to the next pointer of middle node
        if left_node is None:
            print("The left node is absent")
            return

        newNode = Node(new_data)
        newNode.nextval = left_node.nextval  #now the new node points to the node that was right of the left node
        left_node.nextval = newNode #now the left node points to the new node

    def removeNode(self, remove_key):
        # locate the previous node of the node which is to be deleted. 
        # Then point the next pointer of this node to the next node 
        # of the node to be deleted.
        headval = self.headval

        if(headval is not None): #if there is a head value
            if(headval.dataval == remove_key): #if it equals the to-be-removed node
                self.headval = headval.nextval #make the element next to it the new head value
                headval = None #headval becomes non
                return
        while(headval is not None): 
            if headval.dataval == remove_key:
                break
            prev = headval
            headval = headval.nextval

        if (headval == None):
            return
        
        prev.nextval = headval.nextval

        headval=None

list1 = LinkedList()
list1.headval = Node('Mon')
node2 = Node('Wed')
node3 = Node('Thu')

# link the first Node to the second node
list1.headval.nextval = node2

#link the second Node to the third node
node2.nextval = node3

list1.insertAtBeginning("Sun")

list1.insertAtEnd("Fri")

list1.insertBetween(list1.headval.nextval, "Tue")

list1.removeNode("Sun")

list1.listprint()