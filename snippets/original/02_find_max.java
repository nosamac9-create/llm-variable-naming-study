public int findMax(int[] values) {
    int max = values[0];
    int n = values.length;
    for (int i = 1; i < n; i++) {
        if (values[i] > max) {
            max = values[i];
        }
    }
    return max;
}
