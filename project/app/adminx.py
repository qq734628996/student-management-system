import xadmin
from xadmin import views
from xadmin.views.website import LoginView
from xadmin.views import CommAdminView
from .models import *
from .xadmin_action import *

class StudentAdmin(object):
    list_per_page=20
    list_display = (
        'sid',
        'sname',
        'sex',
        'inage',
        'inyear',
        'sclass',
    )
    search_fields = (
        'sid',
        'sname',
    )
    list_filter = (
        'sid',
        'sname',
        'sex',
        'inage',
        'inyear',
        'sclass',
    )

class CourseAdmin(object):
    list_per_page=20
    list_display = (
        'cid',
        'cname',
        'teacher_name',
        'credit',
        'suitable_grade',
        'cancle_year',
    )
    search_fields = (
        'cid',
        'cname',
        'teacher_name',
    )
    list_filter = (
        'cid',
        'cname',
        'teacher_name',
        'credit',
        'suitable_grade',
        'cancle_year',
    )

class EnrollAdmin(object):
    list_per_page=20
    list_display = (
        'student_sid',
        'course_cid',
        'year',
        'score',
    )
    search_fields = (
        'student_sid__sid',
        'student_sid__sname',
        'student_sid__sclass',
        'course_cid__cid',
        'course_cid__cname',
    )
    list_filter = (
        'student_sid',
        'course_cid',
        'year',
        'score',
    )
    actions = [
        GetAvgScoreAction,
    ]

class LoginViewAdmin(LoginView):
    title = '学生信息管理系统'

class GlobalSetting(CommAdminView):
    site_title = '学生信息管理系统'
    site_footer = 'Copyright 刘坤鑫 天津大学 2019'
    #menu_style = 'accordion'

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Enroll, EnrollAdmin)
xadmin.site.register(LoginView, LoginViewAdmin)
xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting)