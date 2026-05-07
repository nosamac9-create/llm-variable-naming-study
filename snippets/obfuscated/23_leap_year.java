public boolean isLeapYear(int v1) {
    boolean v2 = v1 % 4 == 0;
    boolean v3 = v1 % 100 == 0;
    boolean v4 = v1 % 400 == 0;
    return v2 && (!v3 || v4);
}
