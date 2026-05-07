public double computeTotal(List<Product> products) {
    double subtotal = 0;
    double tax = 0;
    double taxRate = 0.15;
    for (Product product : products) {
        double lineTotal = product.getPrice() * product.getQuantity();
        subtotal += lineTotal;
    }
    tax = subtotal * taxRate;
    return subtotal + tax;
}
