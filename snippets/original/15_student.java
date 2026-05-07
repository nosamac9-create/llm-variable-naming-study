public double computeGPA(List<Course> courses) {
    double weightedSum = 0;
    double totalCredits = 0;
    for (Course course : courses) {
        double points = course.getGrade() * course.getCredits();
        weightedSum += points;
        totalCredits += course.getCredits();
    }
    return weightedSum / totalCredits;
}
