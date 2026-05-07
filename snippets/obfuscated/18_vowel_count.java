public int countVowels(String v1) {
    int v2 = 0;
    String v3 = v1.toLowerCase();
    String v4 = "aeiou";
    for (int v5 = 0; v5 < v3.length(); v5++) {
        char v6 = v3.charAt(v5);
        if (v4.indexOf(v6) >= 0) v2++;
    }
    return v2;
}
