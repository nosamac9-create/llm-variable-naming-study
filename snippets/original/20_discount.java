public double applyDiscount(double price, double percent) {
    double rate = percent / 100.0;
    double discount = price * rate;
    double finalPrice = price - discount;
    return finalPrice;
}
