from django.contrib import admin
from .models import Stu_record, Course, Enrollment, Instructor

# Register student model here.
admin.site.register(Stu_record)
class studentAdmin(admin.ModelAdmin):
    list_display = ('stu_ID', 'name', 'age', 'gender', 'grade', 'major')
    search_fields = ('stu_ID', 'name')
    list_filter = ('gender', 'grade', 'major')


# Register Instructor model here.
admin.site.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('instructor_id', 'name', 'department', 'email')
    search_fields = ('instructor_id', 'name')
    list_filter = ('department',)


# Register course model here.
admin.site.register(Course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'name', 'credits', 'instructor')
    search_fields = ('course_id', 'name')
    list_filter = ('instructor',)

# Register Enrollment model here.
admin.site.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'grade_achieved')
    search_fields = ('student__name', 'course__name')
    list_filter = ('enrollment_date',)


