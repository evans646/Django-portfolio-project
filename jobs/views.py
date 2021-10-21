from django.shortcuts import render, get_object_or_404

from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects
    return render(request, 'jobs/index.html',{'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id) #every model in the db has a pk(primary key)
    return render(request, 'jobs/detail.html', {'job':job_detail})
