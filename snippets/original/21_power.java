public double power(double base, int exponent) {
    double result = 1.0;
    int absExp = Math.abs(exponent);
    for (int i = 0; i < absExp; i++) {
        result *= base;
    }
    return exponent < 0 ? 1.0 / result : result;
}
