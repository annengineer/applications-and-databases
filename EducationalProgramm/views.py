from django.shortcuts import render, redirect
from .models import EducationProgram
from .forms import EducationProgramForm
from django.views.generic import DetailView
from django.db.models import Q

def main_page(request):
    projects = EducationProgram.objects.all()
    
    # Фильтрация
    # course_filter = request.GET.get('course')
    # if course_filter:
    #     projects = projects.filter(Q(course=2) & Q(year=2024))
    
    # team_filter = request.GET.get('is_team')
    # if team_filter:
    #     if team_filter == '1':
    #         projects = projects.filter(is_team=True)
    #     elif team_filter == '0':
    #         projects = projects.filter(is_team=False)

    projects = projects.filter(Q(course=2) & Q(year=2024))        
    
    # Сортировка 
    sort_by = request.GET.get('sort', 'name_asc')
    if sort_by == 'name_asc':
        projects = projects.order_by('name')
    elif sort_by == 'name_desc':
        projects = projects.order_by('-name')
    elif sort_by == 'year_asc':
        projects = projects.order_by('year')
    elif sort_by == 'year_desc':
        projects = projects.order_by('-year')
   
   
    
    # Общая статистика
    total_projects = projects.count()
    team_projects = projects.filter(is_team=True).count()
    individual_projects = total_projects - team_projects
    # NOteam_projects = projects.filter(Q(is_team=False) & Q(course=1)).count()
    
    # Курсовая статистика
    course_stats = []
    for course_value, course_name in EducationProgram.COURSE:
        course_projects = projects.filter(course=course_value)
        course_total = course_projects.count()
        if course_total > 0:
            course_team = course_projects.filter(is_team=True).count()
            course_stats.append({
                'name': course_name,
                'total': course_total,
                'team': course_team,
                'individual': course_total - course_team,
                'team_percent': round((course_team / course_total) * 100) if course_total else 0,
            })
    
    context = {
        # 'no_team_proj': NOteam_projects,
        'projects': projects,
        'course_choices': EducationProgram.COURSE,
        'total_projects': total_projects,
        'team_projects': team_projects,

        'individual_projects': individual_projects,
        'team_percent': round((team_projects / total_projects) * 100) if total_projects else 0,
        'course_stats': course_stats,
    }
    
    return render(request, 'main_page.html', context)

class NewDetailView(DetailView):
    model = EducationProgram
    template_name = 'detail_view.html'
    context_object_name = 'project'


def create(request):
    error = ''
    if request.method == 'POST':
        form = EducationProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/EducationalProgramm/main_page/')
        else:
            error = 'Форма неверно заполнена'

    form = EducationProgramForm()
    return render(request, 'create.html', {'form': form, 'error': error})

