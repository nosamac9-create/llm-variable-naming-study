public boolean isPrime(int number) {
    if (number < 2) return false;
    int limit = (int) Math.sqrt(number);
    for (int divisor = 2; divisor <= limit; divisor++) {
        if (number % divisor == 0) return false;
    }
    return true;
}
