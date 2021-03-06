from django.views import generic
from .models import Event
from .models import Member
import datetime


class IndexView(generic.TemplateView):
    template_name = 'info/index.html'


class EventListView(generic.ListView):
    model = Event

    today = datetime.datetime.today()


class MemberListView(generic.ListView):
    model = Member


class EventDetailView(generic.DetailView):  # 追加
    model = Event
