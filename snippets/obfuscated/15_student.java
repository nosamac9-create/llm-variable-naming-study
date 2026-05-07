public double computeGPA(List<Course> v1) {
    double v2 = 0;
    double v3 = 0;
    for (Course v4 : v1) {
        double v5 = v4.getGrade() * v4.getCredits();
        v2 += v5;
        v3 += v4.getCredits();
    }
    return v2 / v3;
}
