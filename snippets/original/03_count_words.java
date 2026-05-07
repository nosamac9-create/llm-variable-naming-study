public int countWords(String sentence) {
    int count = 0;
    String trimmed = sentence.trim();
    String[] tokens = trimmed.split("\\s+");
    for (String word : tokens) {
        if (!word.isEmpty()) count++;
    }
    return count;
}
