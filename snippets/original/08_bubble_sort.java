public void bubbleSort(int[] arr) {
    int length = arr.length;
    for (int pass = 0; pass < length - 1; pass++) {
        for (int j = 0; j < length - pass - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int swap = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = swap;
            }
        }
    }
}
