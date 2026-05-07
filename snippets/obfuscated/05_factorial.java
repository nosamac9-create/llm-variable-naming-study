public long factorial(int v1) {
    long v2 = 1;
    for (int v3 = 2; v3 <= v1; v3++) {
        v2 *= v3;
    }
    return v2;
}
