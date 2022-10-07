from django.shortcuts import render, get_object_or_404

from .models import Job

# Create your views here.
def index(request):
    projects = Job.objects
    return render(request, 'jobs/index.html',{'projects':projects})

def detail(request, project_id):
    project_detail = get_object_or_404(Job, pk=project_id) #every model in the db has a pk(primary key)
    return render(request, 'jobs/detail.html', {'project':project_detail})
