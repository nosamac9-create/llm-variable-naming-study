public int linearSearch(int[] data, int target) {
    int n = data.length;
    for (int index = 0; index < n; index++) {
        if (data[index] == target) return index;
    }
    return -1;
}
