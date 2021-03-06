from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from app.models import Session
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
    return render(request,'index.html')

class SessionList(ListView):
    model = Session

class SessionDetail(DetailView):
    model = Session

class SessionCreate(CreateView):
    model = Session
    fields = ['title','abstract','track', 'speaker']

class SessionUpdate(UpdateView):
    model = Session
    fields = ['title','abstract','track', 'speaker']

class SessionDelete(DeleteView):
    model = Session
    success_url = reverse_lazy('sessions_list')

@login_required
def submit_session(request):
    return render(request,'app/submit_session.html')

