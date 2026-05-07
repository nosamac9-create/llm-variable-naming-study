public double computeTotal(List<Product> v1) {
    double v2 = 0;
    double v3 = 0;
    double v4 = 0.15;
    for (Product v5 : v1) {
        double v6 = v5.getPrice() * v5.getQuantity();
        v2 += v6;
    }
    v3 = v2 * v4;
    return v2 + v3;
}
