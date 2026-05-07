public String reverse(String v1) {
    char[] v2 = v1.toCharArray();
    int v3 = 0, v4 = v2.length - 1;
    while (v3 < v4) {
        char v5 = v2[v3];
        v2[v3++] = v2[v4];
        v2[v4--] = v5;
    }
    return new String(v2);
}
