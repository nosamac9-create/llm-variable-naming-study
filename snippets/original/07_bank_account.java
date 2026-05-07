public void withdraw(double amount) {
    if (amount > 0 && amount <= this.balance) {
        this.balance -= amount;
        this.transactions.add(amount);
    }
}
