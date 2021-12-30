from django.contrib import admin

from admincustomization.models import Instructor, Student

# Customize models by extending ModelAdmin class

# Customize Instructor
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name","teaches","no_of_students")
    def no_of_students(self, obj):
        from django.db.models import Count
        total_students = Student.objects.filter(instructor = obj).aggregate(Count('std_name'))
        return total_students["std_name__count"]

# Customize Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ("std_name","takes_course")
    list_filter = ("takes_course",)

# Register models and model admins
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Student,StudentAdmin)