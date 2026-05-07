public int sumArray(int[] numbers) {
    int total = 0;
    int length = numbers.length;
    for (int i = 0; i < length; i++) {
        total += numbers[i];
    }
    return total;
}
