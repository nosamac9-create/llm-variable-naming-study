public int linearSearch(int[] v1, int v2) {
    int v3 = v1.length;
    for (int v4 = 0; v4 < v3; v4++) {
        if (v1[v4] == v2) return v4;
    }
    return -1;
}
