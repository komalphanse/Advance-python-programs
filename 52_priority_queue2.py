print("priority queue with numbers")
import queue
q=queue.PriorityQueue()
q.put((1,"rohan"))
q.put((3,"sharuk"))
q.put((4,"ajay"))
q.put((2,"shiva"))
while not q.empty():
    print(q.get()[1])#1st index value is printed
    #print(q.get()[0])#0th index value is printed by using number wise