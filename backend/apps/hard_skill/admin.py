from django.contrib import admin

from .models import HardSkill, UnknownHardSkill
from ..vacancy.models import Vacancy


@admin.register(HardSkill)
class HardSkillAdmin(admin.ModelAdmin):
    def vacancies_with_skill(self, obj):
        vacancies = Vacancy.objects.filter(hard_skills=obj)
        return len(vacancies)

    vacancies_with_skill.short_description = "Vacancies with this skill"

    list_display = ["name", "vacancies_with_skill"]


@admin.register(UnknownHardSkill)
class UnknownHardSkillAdmin(admin.ModelAdmin):
    list_display = ["name", "create_count"]
