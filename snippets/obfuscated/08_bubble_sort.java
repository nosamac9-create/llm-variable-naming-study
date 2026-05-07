public void bubbleSort(int[] v1) {
    int v2 = v1.v2;
    for (int v3 = 0; v3 < v2 - 1; v3++) {
        for (int v4 = 0; v4 < v2 - v3 - 1; v4++) {
            if (v1[v4] > v1[v4 + 1]) {
                int v5 = v1[v4];
                v1[v4] = v1[v4 + 1];
                v1[v4 + 1] = v5;
            }
        }
    }
}
