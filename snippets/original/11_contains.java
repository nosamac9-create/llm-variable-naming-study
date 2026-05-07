public boolean contains(String text, String pattern) {
    int textLen = text.length();
    int patternLen = pattern.length();
    for (int i = 0; i <= textLen - patternLen; i++) {
        String window = text.substring(i, i + patternLen);
        if (window.equals(pattern)) return true;
    }
    return false;
}
