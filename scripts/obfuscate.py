"""
Generates the 25 Java snippet pairs (original + obfuscated) for the dataset.
This script is what created the snippets/ folder contents.
"""
import os
import re

# Each snippet is a tuple: (filename, original_code, list of var names in obfuscation order)
SNIPPETS = [
    # 1: array sum
    ("01_array_sum.java", """public int sumArray(int[] numbers) {
    int total = 0;
    int length = numbers.length;
    for (int i = 0; i < length; i++) {
        total += numbers[i];
    }
    return total;
}""", ["numbers", "total", "length", "i"]),

    # 2: max value
    ("02_find_max.java", """public int findMax(int[] values) {
    int max = values[0];
    int n = values.length;
    for (int i = 1; i < n; i++) {
        if (values[i] > max) {
            max = values[i];
        }
    }
    return max;
}""", ["values", "max", "n", "i"]),

    # 3: count words
    ("03_count_words.java", """public int countWords(String sentence) {
    int count = 0;
    String trimmed = sentence.trim();
    String[] tokens = trimmed.split("\\\\s+");
    for (String word : tokens) {
        if (!word.isEmpty()) count++;
    }
    return count;
}""", ["sentence", "count", "trimmed", "tokens", "word"]),

    # 4: reverse string
    ("04_reverse_string.java", """public String reverse(String input) {
    char[] chars = input.toCharArray();
    int start = 0, end = chars.length - 1;
    while (start < end) {
        char temp = chars[start];
        chars[start++] = chars[end];
        chars[end--] = temp;
    }
    return new String(chars);
}""", ["input", "chars", "start", "end", "temp"]),

    # 5: factorial
    ("05_factorial.java", """public long factorial(int n) {
    long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}""", ["n", "result", "i"]),

    # 6: is prime
    ("06_is_prime.java", """public boolean isPrime(int number) {
    if (number < 2) return false;
    int limit = (int) Math.sqrt(number);
    for (int divisor = 2; divisor <= limit; divisor++) {
        if (number % divisor == 0) return false;
    }
    return true;
}""", ["number", "limit", "divisor"]),

    # 7: bank account
    ("07_bank_account.java", """public void withdraw(double amount) {
    if (amount > 0 && amount <= this.balance) {
        this.balance -= amount;
        this.transactions.add(amount);
    }
}""", ["withdraw", "amount", "balance", "transactions"]),

    # 8: bubble sort
    ("08_bubble_sort.java", """public void bubbleSort(int[] arr) {
    int length = arr.length;
    for (int pass = 0; pass < length - 1; pass++) {
        for (int j = 0; j < length - pass - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int swap = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = swap;
            }
        }
    }
}""", ["arr", "length", "pass", "j", "swap"]),

    # 9: linear search
    ("09_linear_search.java", """public int linearSearch(int[] data, int target) {
    int n = data.length;
    for (int index = 0; index < n; index++) {
        if (data[index] == target) return index;
    }
    return -1;
}""", ["data", "target", "n", "index"]),

    # 10: average
    ("10_average.java", """public double average(double[] grades) {
    double sum = 0;
    int count = grades.length;
    for (double grade : grades) {
        sum += grade;
    }
    return sum / count;
}""", ["grades", "sum", "count", "grade"]),

    # 11: contains substring
    ("11_contains.java", """public boolean contains(String text, String pattern) {
    int textLen = text.length();
    int patternLen = pattern.length();
    for (int i = 0; i <= textLen - patternLen; i++) {
        String window = text.substring(i, i + patternLen);
        if (window.equals(pattern)) return true;
    }
    return false;
}""", ["text", "pattern", "textLen", "patternLen", "i", "window"]),

    # 12: even count
    ("12_even_count.java", """public int countEven(List<Integer> numbers) {
    int evenCount = 0;
    int oddCount = 0;
    for (int n : numbers) {
        if (n % 2 == 0) evenCount++;
        else oddCount++;
    }
    return evenCount;
}""", ["numbers", "evenCount", "oddCount", "n"]),

    # 13: fibonacci
    ("13_fibonacci.java", """public int fibonacci(int n) {
    if (n <= 1) return n;
    int prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}""", ["n", "prev", "curr", "i", "next"]),

    # 14: gcd
    ("14_gcd.java", """public int gcd(int a, int b) {
    while (b != 0) {
        int remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}""", ["a", "b", "remainder"]),

    # 15: student record
    ("15_student.java", """public double computeGPA(List<Course> courses) {
    double weightedSum = 0;
    double totalCredits = 0;
    for (Course course : courses) {
        double points = course.getGrade() * course.getCredits();
        weightedSum += points;
        totalCredits += course.getCredits();
    }
    return weightedSum / totalCredits;
}""", ["courses", "weightedSum", "totalCredits", "course", "points"]),

    # 16: palindrome
    ("16_palindrome.java", """public boolean isPalindrome(String word) {
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
}""", ["word", "left", "right", "leftChar", "rightChar"]),

    # 17: matrix transpose
    ("17_transpose.java", """public int[][] transpose(int[][] matrix) {
    int rows = matrix.length;
    int cols = matrix[0].length;
    int[][] result = new int[cols][rows];
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            result[c][r] = matrix[r][c];
        }
    }
    return result;
}""", ["matrix", "rows", "cols", "result", "r", "c"]),

    # 18: vowel count
    ("18_vowel_count.java", """public int countVowels(String text) {
    int vowels = 0;
    String lower = text.toLowerCase();
    String vowelSet = "aeiou";
    for (int i = 0; i < lower.length(); i++) {
        char ch = lower.charAt(i);
        if (vowelSet.indexOf(ch) >= 0) vowels++;
    }
    return vowels;
}""", ["text", "vowels", "lower", "vowelSet", "i", "ch"]),

    # 19: queue add
    ("19_queue.java", """public void enqueue(Item item) {
    if (size >= capacity) {
        throw new IllegalStateException("Queue is full");
    }
    items[tail] = item;
    tail = (tail + 1) % capacity;
    size++;
}""", ["enqueue", "item", "size", "capacity", "items", "tail"]),

    # 20: discount
    ("20_discount.java", """public double applyDiscount(double price, double percent) {
    double rate = percent / 100.0;
    double discount = price * rate;
    double finalPrice = price - discount;
    return finalPrice;
}""", ["price", "percent", "rate", "discount", "finalPrice"]),

    # 21: power
    ("21_power.java", """public double power(double base, int exponent) {
    double result = 1.0;
    int absExp = Math.abs(exponent);
    for (int i = 0; i < absExp; i++) {
        result *= base;
    }
    return exponent < 0 ? 1.0 / result : result;
}""", ["base", "exponent", "result", "absExp", "i"]),

    # 22: temperature
    ("22_temperature.java", """public double celsiusToFahrenheit(double celsius) {
    double scaled = celsius * 9.0 / 5.0;
    double fahrenheit = scaled + 32.0;
    return fahrenheit;
}""", ["celsius", "scaled", "fahrenheit"]),

    # 23: leap year
    ("23_leap_year.java", """public boolean isLeapYear(int year) {
    boolean divisibleBy4 = year % 4 == 0;
    boolean divisibleBy100 = year % 100 == 0;
    boolean divisibleBy400 = year % 400 == 0;
    return divisibleBy4 && (!divisibleBy100 || divisibleBy400);
}""", ["year", "divisibleBy4", "divisibleBy100", "divisibleBy400"]),

    # 24: stack pop
    ("24_stack.java", """public Item pop() {
    if (top < 0) {
        throw new IllegalStateException("Stack is empty");
    }
    Item popped = stack[top];
    stack[top] = null;
    top--;
    return popped;
}""", ["top", "popped", "stack"]),

    # 25: shopping cart
    ("25_cart_total.java", """public double computeTotal(List<Product> products) {
    double subtotal = 0;
    double tax = 0;
    double taxRate = 0.15;
    for (Product product : products) {
        double lineTotal = product.getPrice() * product.getQuantity();
        subtotal += lineTotal;
    }
    tax = subtotal * taxRate;
    return subtotal + tax;
}""", ["products", "subtotal", "tax", "taxRate", "product", "lineTotal"]),
]


def obfuscate(code, var_names):
    """Replace each variable name with v1, v2, ... using whole-word matching."""
    out = code
    for i, name in enumerate(var_names, start=1):
        # word-boundary replace
        out = re.sub(r'\b' + re.escape(name) + r'\b', f'v{i}', out)
    return out


def main(out_dir="."):
    orig_dir = os.path.join(out_dir, "snippets/original")
    obf_dir = os.path.join(out_dir, "snippets/obfuscated")
    os.makedirs(orig_dir, exist_ok=True)
    os.makedirs(obf_dir, exist_ok=True)

    total_vars = 0
    for fname, code, vars in SNIPPETS:
        with open(os.path.join(orig_dir, fname), "w") as f:
            f.write(code + "\n")
        with open(os.path.join(obf_dir, fname), "w") as f:
            f.write(obfuscate(code, vars) + "\n")
        total_vars += len(vars)

    print(f"Wrote {len(SNIPPETS)} snippet pairs ({total_vars} total variables) to {out_dir}/")


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
