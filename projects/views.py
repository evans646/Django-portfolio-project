from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from .forms import ContactForm
from .models import Contact, Project
 

# Create your views here.
def index(request):
    projects = Project.objects
    # contact form
    # form = ContactForm()
    return render(request, 'projects/index.html',{'projects':projects}) 


def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id) #every model in the db has a pk(primary key)
    return render(request, 'project/detail.html', {'project':project_detail})


