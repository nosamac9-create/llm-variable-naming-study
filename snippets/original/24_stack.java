public Item pop() {
    if (top < 0) {
        throw new IllegalStateException("Stack is empty");
    }
    Item popped = stack[top];
    stack[top] = null;
    top--;
    return popped;
}
