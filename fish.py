#-*- coding=utf-8 -*-

class Queue:
    data = []
    head = 1
    tail = 1

class Stack:
    data = []
    top = 0


q1 = Queue()
q2 = Queue()
s = Stack()
book = []
t = 0


for i in range(1,10):
    book.append(0)
    

q1.data = [1,9,5,6,8,3]
q1.tail = 7

q2.data = [1,5,3,6,9,8]
q2.tail = 7

print(book)

while(q1.head<q1.tail && q2.head<q2.tail):
    t = q1.data[q1.head]
    if book[t] == 0:
        q1.head++
        s.top++
        s.data.append(t)
        book[t] = 1
    else:
        


