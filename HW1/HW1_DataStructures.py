# Diego Fernando Montaño Pérez A01282875
# Tarea1 Creado: 17/02/2021
# Instrucciones: Desarrolla y/o documenta una implementación apropiada para las siguientes clases: STACK (lifo), QUEUE (fifo),
# TABLE/HASH/DICTIONARY (order)
# Se implementan clases de librerías ya creadas

#Public libraries use to implement Stack and Queue
from queue import Queue
from collections import deque

#Using deque to implement Stack
def UseStack():
    #Creating stack 
    stack = deque()
    #Adding/Pushing values
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    #Check values in stack
    print(stack)
    #Getting and deleting items from stack
    print("Pull and deleting",stack.pop())
    print("Pull and deleting",stack.pop())
    print("Pull and deleting",stack.pop())
    #Check values in stack
    print(stack)



#Using Queue library
def UseQueue():
    #Initiaize a Queue with maxsize
    q = Queue(maxsize=10)
    #Adding/Pushing values
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    #Check Queue size
    print("Actual size:",q.qsize())
    #Getting and deleting items from queue
    print("Pull and deleting",q.get())
    print("Pull and deleting",q.get())
    #Check Queue size
    print("Actual size:",q.qsize())
    #Checking if queue is full
    print(q.full())
    #Checking if queue is empty
    print(q.empty())


# Call queue function
print("Queue:")
UseQueue()
print('\n')

print("Stack:")
# Call stack function
UseStack()
print('\n')

print("Dictionary:")
# Dictionary Example
myDictionary = {
    "name" : "Diego",
    "age" : 22,
    "major" : "Computer Science",
    "semester" : 8
}
# Creating empty dictionaries
auxDic2 = {}
auxDic3 = dict()
# Creating dictionary with list of tuples
auxDic4 = [("School","Tec"),("Country","Mexico"),("Foundation", 1943)]
# Getting specific values from dictionary using key
print(myDictionary.get("name"))

# Getting all items in dictionary
print("Dictionary =",list(myDictionary.items()))

# Removing a key from dictionary
myDictionary.pop("semester")

# Getting all items in dictionary
print("Dictionary after pop =",list(myDictionary.items()))

