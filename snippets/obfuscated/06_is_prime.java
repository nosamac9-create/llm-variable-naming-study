public boolean isPrime(int v1) {
    if (v1 < 2) return false;
    int v2 = (int) Math.sqrt(v1);
    for (int v3 = 2; v3 <= v2; v3++) {
        if (v1 % v3 == 0) return false;
    }
    return true;
}
