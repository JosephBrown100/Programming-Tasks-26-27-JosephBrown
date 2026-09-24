"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def populate(queue):
    for i in random(1,20):
        person = random(1-30)
        queue.append(person)

def dequeue(queue):
    firstelement = queue.pop[0]
    print("Dequeue: ", firstelement)

def enqueue(queue):
    person = random(1-30)
    queue.append(person)

def peek(queue):
    firstelement = queue[0]
    print("peek: ", firstelement)

def size(queue):
    print("size: ", len(queue))






def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    main()
    queue = []
    populate(queue)
    while True:
        queuemod = input("enter 1 to dequeue, 2 to enqueue, 3 to peek, 4 to hear list size")
        try:
            if queuemod == 1:
                dequeue(queue)
            elif queuemod == 2:
                enqueue(queue)
            elif queuemod == 3:
                peek(queue)
            elif queuemod == 4:
                size(queue)
        except:
            print("invalid, re-enter")

