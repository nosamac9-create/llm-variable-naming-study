public double average(double[] grades) {
    double sum = 0;
    int count = grades.length;
    for (double grade : grades) {
        sum += grade;
    }
    return sum / count;
}
