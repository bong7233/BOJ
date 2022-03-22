import sys

# 리스트로 스택 구현
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.size() == 0:
            return -1
        else:
            n = self.data.pop()
            return n

    def size(self):
        return len(self.data)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self.data[-1]


# 스택 인스턴스 생성
stack = Stack()

n = int(input())

for _ in range(n):
    command = list(sys.stdin.readline().split()) # 입력받은 명령을 리스트형태로 저장(['push',2]...)
    if command[0] == 'push':        # 명령이 push 라면 두번쨰로 받은 숫자를 활용
        stack.push(int(command[1]))
    elif command[0] == 'top':       # 나머지 명령은 함수기능 실행
        print(stack.top())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'pop':
        print(stack.pop())