while True:
    s = input()
    if s == ".":       # 종결 마침표가 입력될때까지 반복
      break

    stack = []                # (, [ 를 담는 스택 생성
    pair = {')':'(', ']':'['} # 괄호쌍을 키-벨류로 저장

    for char in s:
        if char in '([':          # ([ 가 나오면 스택에 저장
            stack.append(char)
        elif char in pair:        # )] 가 나오면 스택의 맨위가 ([ 인지 확인
            if len(stack) != 0 and pair[char] == stack[-1]:
                stack.pop()       # 쌍이 맞다면 스택에서 제거
            else:         # 쌍이 안맞다면
                stack.append(char)
                break

    if len(stack) == 0:   # 반복문이 끝나고 스택이 비어있다면 올바른문장
        print("yes")      # 스택이 비어있다? -> 괄호쌍이 맞아서 모두pop했다
    else:
        print("no")       # 스택이 비어있지않다? -> 괄호쌍이 안맞아서 pop안된 괄호가 남아있다
