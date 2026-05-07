public String reverse(String input) {
    char[] chars = input.toCharArray();
    int start = 0, end = chars.length - 1;
    while (start < end) {
        char temp = chars[start];
        chars[start++] = chars[end];
        chars[end--] = temp;
    }
    return new String(chars);
}
