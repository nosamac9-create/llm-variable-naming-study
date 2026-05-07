public int[][] transpose(int[][] v1) {
    int v2 = v1.length;
    int v3 = v1[0].length;
    int[][] v4 = new int[v3][v2];
    for (int v5 = 0; v5 < v2; v5++) {
        for (int v6 = 0; v6 < v3; v6++) {
            v4[v6][v5] = v1[v5][v6];
        }
    }
    return v4;
}
