from django.db import models

# Create your student models here.
class Stu_record(models.Model):
    stu_ID = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female')])
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your Course model here
class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credits = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.course_id} - {self.name}"
    

# Create your Enrollment model here
# Many to many relationship with stu_record and Course
class Enrollment(models.Model):
    student = models.ForeignKey(Stu_record, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    grade_achieved = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
    

# Create your Instructor model here


