public int fibonacci(int v1) {
    if (v1 <= 1) return v1;
    int v2 = 0, v3 = 1;
    for (int v4 = 2; v4 <= v1; v4++) {
        int v5 = v2 + v3;
        v2 = v3;
        v3 = v5;
    }
    return v3;
}
