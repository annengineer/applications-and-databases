from django.shortcuts import render
from .models import Members, Management, EP
# Create your views here.
def groupmates(request):
    
    groupmates = Members.objects.all()
    
    search_input = request.GET.get('search') or ''  
    if search_input:
        groupmates = groupmates.filter(name__icontains=search_input)
        

        
    sort = request.GET.get('sort', 'name')
    if sort in ['name', '-name', 'email', '-email']:
        groupmates = groupmates.order_by(sort)    
        
    
    context = {
        'groupmates': groupmates,
        'sort': sort, 
        'search_input':search_input 
    }
    return render(request,'groupmates.html', context)

def me(request):
    try:
        member = Members.objects.get(name="Анна Вишневская")
    except Members.DoesNotExist:
        member = None
    return render(request,'me.html', {"member" : member})   

def managers(request):
    managers = Management.objects.all()
    return render  (request, 'managers.html', {"managers" : managers}) 

def ep(request):
    try:
        ep = EP.objects.get(name="Городское планирование")
    except EP.DoesNotExist:
        ep = None
    return render(request,'ep.html', {"ep" : ep})   