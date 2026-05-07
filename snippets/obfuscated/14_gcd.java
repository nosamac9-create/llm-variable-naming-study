public int gcd(int v1, int v2) {
    while (v2 != 0) {
        int v3 = v1 % v2;
        v1 = v2;
        v2 = v3;
    }
    return v1;
}
