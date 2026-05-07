public double power(double v1, int v2) {
    double v3 = 1.0;
    int v4 = Math.abs(v2);
    for (int v5 = 0; v5 < v4; v5++) {
        v3 *= v1;
    }
    return v2 < 0 ? 1.0 / v3 : v3;
}
