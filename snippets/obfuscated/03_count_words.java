public int countWords(String v1) {
    int v2 = 0;
    String v3 = v1.trim();
    String[] v4 = v3.split("\\s+");
    for (String v5 : v4) {
        if (!v5.isEmpty()) v2++;
    }
    return v2;
}
