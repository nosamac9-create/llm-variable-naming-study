public boolean isPalindrome(String v1) {
    int v2 = 0;
    int v3 = v1.length() - 1;
    while (v2 < v3) {
        char v4 = v1.charAt(v2);
        char v5 = v1.charAt(v3);
        if (v4 != v5) return false;
        v2++;
        v3--;
    }
    return true;
}
