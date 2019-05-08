import json
from django.http import HttpResponse
from xadmin.plugins.actions import BaseActionView

class GetAvgScoreAction(BaseActionView):
    action_name = "get_avg_score"
    description = '显示成绩分布'
    model_perm = 'change'
    def do_action(self, queryset):
        res={
            '统计人数': len(queryset),
            '平均值': 0,
            '不及格': 0,
            '60-69': 0,
            '70-79': 0,
            '80-89': 0,
            '90-99': 0,
            '满分': 0,
        }
        for obj in queryset:
            res['平均值'] += obj.score
            if obj.score < 60:
                res['不及格'] += 1
            elif obj.score < 70:
                res['60-69'] += 1
            elif obj.score < 80:
                res['70-79'] += 1
            elif obj.score < 90:
                res['80-89'] += 1
            elif obj.score < 100:
                res['90-99'] += 1
            else:
                res['满分'] += 1
        res['平均值']/=len(queryset)
        return HttpResponse(json.dumps(res), content_type='application/json')