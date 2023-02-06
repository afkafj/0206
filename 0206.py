# 함수 선언
def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else :
        return False
    

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False
    
def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        return
    top += 1
    stack[top] = data

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()) :
        return None
    return stack[top]

# 변수 선언
SIZE = 100
stack =[None for _ in range(SIZE)]
top = -1

# 메인 코드
if__name__== "__main__" :
  
with open("진달래꽃.txt", 'r' ,encoding="UTF8") as rfp :
  lineAry = rfp.readlines()

  print("-----원본-----")
  for line in lineAry :
      push(line)
      print(line, end=' ')
print()

print("-----거꾸로 처리된 결과-----")
while True :
    line = pop()
    if line == None :
        break
    ministack = [None for_in range(len(line))]
    miniTop = -1
    for ch in line :
        miniTop += 1
        ministack[miniTop] = ch

while True :
    if miniTop == -1 :
        break
    ch = ministack[minitop]
    miniTop -= 1
    print(ch, end = ' ')
