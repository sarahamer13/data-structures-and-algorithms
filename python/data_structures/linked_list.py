class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = None


class LinkedList:
    """
    This is the beginning of linked list
    """

    def __init__(self):

       """ initializing an empty linked list by setting it to None """

       self.head = None

        ## used multiple resources, class demo, freecodecamp.org, class materials, and chat gbt

    """ Now we have several methods inside the linked list class
     method insert here insert a node node with a given value, then
     create a new Node object with the provided value, then the next line
     will ensure the new Node will be the new head of the list, then the
     following line will updates the head attribute by pointing to the
     new node which will make it the new head in the list """


    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    """ Afterward, we have the includes method, to check if a node
    with the given value exists in the linked list, if it does, it return
    True and if it's not found it will be False. First initialize a variable current
    to the head of the linked list to start traversing from the beginning, then the while loop
    will iterate through the linked list as long as it is not none. It will check if the
    value of the current list is equal to value we want, it will return true,
    after it will update the current variable to point to the next node in the linked list,
    then if the node with the value is not found,it will return false """

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    """ The below method empty checks if the linked list is empty by
    testing if the head attribute is None and it has no nodes, if it's none, the list is empty and it will return
    true, if it is not, it will return false """


    def is_empty(self):
        return self.head is None


    """ The str method is a custom string, it will check if the linked list is empty, it will return Null
    then initialize a variable current to head to start traversing. After set an empty list to result to store
    the string representation of the nodes. Then it will start a while loop to iterate through the linked list.
    Next line will start appending the string representation of the current node values to result list we have.
    after it will update the current variable to point to the next node in linked list. When the loop is done,
    the str method will append the "Null" to the result list to indicate it's the end of the linked list.
    At last, the result will be returned, but with the use of the arrow and join will concatenate
    all the string representation in result list, by having
    the arrow, it will create a structured format of the string """

    def __str__(self):
        if self.is_empty():
            return "NULL"

        current = self.head
        result = []
        while current:
            result.append(f"{{ {current.value} }}")
            current = current.next
        result.append("NULL")
        return " -> ".join(result)


    """
        tried to remove the target error and I noticed If I do all the tests
        that has passed, it won't show up anymore. Instead, it shows  2 others linked list files has errors
    """
class TargetError:
    pass
