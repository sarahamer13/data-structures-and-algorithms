## Linked List

### Author: Sarah Mahdi

### Notes:

- We have several methods inside the linked list class
     method insert here insert a node node with a given value, then
     create a new Node object with the provided value, then the next line
     will ensure the new Node will be the new head of the list, then the
     following line will updates the head attribute by pointing to the
     new node which will make it the new head in the list

- Then we have the includes method, to check if a node
    with the given value exists in the linked list, if it does, it return
    True and if it's not found it will be False. First initialize a variable current
    to the head of the linked list to start traversing from the beginning, then the while loop
    will iterate through the linked list as long as it is not none. It will check if the
    value of the current list is equal to value we want, it will return true,
    after it will update the current variable to point to the next node in the linked list,
    then if the node with the value is not found,it will return false.

- Empty method checks if the linked list is empty by
    testing if the head attribute is None and it has no nodes, if it's none, the list is empty and it will return
    true, if it is not, it will return false

- The str method is a custom string, it will check if the linked list is empty, it will return Null
    then initialize a variable current to head to start traversing. After set an empty list to result to store
    the string representation of the nodes. Then it will start a while loop to iterate through the linked list.
    Next line will start appending the string representation of the current node values to result list we have.
    after it will update the current variable to point to the next node in linked list. When the loop is done,
    the str method will append the "Null" to the result list to indicate it's the end of the linked list.
    At last, the result will be returned, but with the use of the arrow and join will concatenate
    all the string representation in result list, by having
    the arrow, it will create a structured format of the string

#### Attribution

- Lecture demo was very helpful

- reading materials from class

- [freecodecamp](https://www.freecodecamp.org/news/introduction-to-linked-lists-in-python/#:~:text=Linked%20Lists%20are%20a%20data,list%20is%20called%20a%20node.)

- Chatgbt to further explain about linked list and correct errors in the code

