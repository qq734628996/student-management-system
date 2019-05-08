from django.db import models

# Create your models here.
class Student(models.Model):
    SEX = (
        ('male', '男'),
        ('female', '女')
    )
    sid = models.BigIntegerField(verbose_name='学号', primary_key=True)
    sname = models.CharField(verbose_name='姓名', max_length=32)
    sex = models.CharField(choices=SEX, verbose_name='性别', max_length=8)
    inage = models.IntegerField(verbose_name='入学年龄')
    inyear = models.IntegerField(verbose_name='入学年份')
    sclass = models.CharField(verbose_name='班级', max_length=32)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

    def __str__(self):
        return str(self.sid)

class Course(models.Model):
    cid = models.IntegerField(verbose_name='课程编号', primary_key=True)
    cname = models.CharField(verbose_name='课程名称', max_length=32)
    teacher_name = models.CharField(verbose_name='授课老师', max_length=32)
    credit = models.IntegerField(verbose_name='学分')
    suitable_grade = models.IntegerField(verbose_name='课程适合年级')
    cancle_year = models.IntegerField(verbose_name='取消年份', null=True, blank=True)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = '课程信息'

    def __str__(self):
        return str(self.cid)

class Enroll(models.Model):
    eid = models.AutoField(primary_key=True)
    student_sid = models.ForeignKey(Student, verbose_name='学生学号', on_delete=models.CASCADE)
    course_cid = models.ForeignKey(Course, verbose_name='课程编号', on_delete=models.DO_NOTHING)
    year = models.IntegerField(verbose_name='选课年份')
    score = models.IntegerField(verbose_name='成绩')

    class Meta:
        verbose_name = '选课信息'
        verbose_name_plural = '选课信息'
    
    def __str__(self):
        return str(self.eid)
