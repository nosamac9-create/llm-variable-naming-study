public boolean isPalindrome(String word) {
    int left = 0;
    int right = word.length() - 1;
    while (left < right) {
        char leftChar = word.charAt(left);
        char rightChar = word.charAt(right);
        if (leftChar != rightChar) return false;
        left++;
        right--;
    }
    return true;
}
