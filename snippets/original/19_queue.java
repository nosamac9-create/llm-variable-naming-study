public void enqueue(Item item) {
    if (size >= capacity) {
        throw new IllegalStateException("Queue is full");
    }
    items[tail] = item;
    tail = (tail + 1) % capacity;
    size++;
}
