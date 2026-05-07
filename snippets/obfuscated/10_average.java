public double average(double[] v1) {
    double v2 = 0;
    int v3 = v1.length;
    for (double v4 : v1) {
        v2 += v4;
    }
    return v2 / v3;
}
