public int countVowels(String text) {
    int vowels = 0;
    String lower = text.toLowerCase();
    String vowelSet = "aeiou";
    for (int i = 0; i < lower.length(); i++) {
        char ch = lower.charAt(i);
        if (vowelSet.indexOf(ch) >= 0) vowels++;
    }
    return vowels;
}
