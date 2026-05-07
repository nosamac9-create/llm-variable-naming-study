public boolean contains(String v1, String v2) {
    int v3 = v1.length();
    int v4 = v2.length();
    for (int v5 = 0; v5 <= v3 - v4; v5++) {
        String v6 = v1.substring(v5, v5 + v4);
        if (v6.equals(v2)) return true;
    }
    return false;
}
