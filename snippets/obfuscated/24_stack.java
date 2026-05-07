public Item pop() {
    if (v1 < 0) {
        throw new IllegalStateException("Stack is empty");
    }
    Item v2 = v3[v1];
    v3[v1] = null;
    v1--;
    return v2;
}
