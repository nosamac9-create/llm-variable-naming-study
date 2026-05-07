public int findMax(int[] v1) {
    int v2 = v1[0];
    int v3 = v1.length;
    for (int v4 = 1; v4 < v3; v4++) {
        if (v1[v4] > v2) {
            v2 = v1[v4];
        }
    }
    return v2;
}
