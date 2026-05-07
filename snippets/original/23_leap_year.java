public boolean isLeapYear(int year) {
    boolean divisibleBy4 = year % 4 == 0;
    boolean divisibleBy100 = year % 100 == 0;
    boolean divisibleBy400 = year % 400 == 0;
    return divisibleBy4 && (!divisibleBy100 || divisibleBy400);
}
