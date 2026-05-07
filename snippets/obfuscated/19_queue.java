public void v1(Item v2) {
    if (v3 >= v4) {
        throw new IllegalStateException("Queue is full");
    }
    v5[v6] = v2;
    v6 = (v6 + 1) % v4;
    v3++;
}
