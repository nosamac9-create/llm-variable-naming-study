public int countEven(List<Integer> v1) {
    int v2 = 0;
    int v3 = 0;
    for (int v4 : v1) {
        if (v4 % 2 == 0) v2++;
        else v3++;
    }
    return v2;
}
