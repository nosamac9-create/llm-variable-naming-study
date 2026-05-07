public int countEven(List<Integer> numbers) {
    int evenCount = 0;
    int oddCount = 0;
    for (int n : numbers) {
        if (n % 2 == 0) evenCount++;
        else oddCount++;
    }
    return evenCount;
}
