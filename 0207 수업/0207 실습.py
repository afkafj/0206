def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE-1) : 
        return True
    else :
        return False
    
def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False
    
def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print("큐가 꽉 참")
        return
    rear += 1
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 빔")
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front+1, rear+1) :
        queue[i-1]=queue[i]
        queue[i]=None
    front = -1
    rear -= 1

    return data


def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 빔")
        return None
    return queue[front+1]


SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


if __name__ =="main" :
    enQueue('정국') 
    enQueue('뷔') 
    enQueue('지민') 
    enQueue('진') 
    enQueue('슈가')
    print("대기 줄 상태")

    for _ in range(rear+1) :
        print(deQueue(), '님 식당으로 들어감')
        print("대기 줄 상태 :", queue)

    print("식당 영업종료") 
