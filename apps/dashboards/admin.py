from django.contrib import admin
from .models import GradeLevel, Club, Student, ClubMember

admin.site.register(GradeLevel)
admin.site.register(Club)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "grade_level")
    search_fields = ("lastname", "firstname")

@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_student_grade_level", "club", "date_joined")
    search_fields = ("student__lastname", "student__firstname")

    @admin.display(description="Grade Level")
    def get_student_grade_level(self, obj):
        return obj.student.grade_level
