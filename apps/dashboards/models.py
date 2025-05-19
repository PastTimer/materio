from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GradeLevel(BaseModel):
    level_name = models.CharField(max_length=50)  # e.g., "Grade 7", "Grade 10"

    def __str__(self):
        return self.level_name

class Club(BaseModel):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Student(BaseModel):
    student_id = models.CharField(max_length=15)
    lastname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

class ClubMember(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
