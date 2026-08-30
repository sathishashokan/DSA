def insert(stack, temp):
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return

    val = stack.pop()
    insert(stack, temp)

    stack.append(val)


def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert(stack, temp)


stk = [4,3,1,2]
sort_stack(stk)
print(stk)
