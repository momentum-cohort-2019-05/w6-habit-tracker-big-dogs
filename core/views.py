from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Max
# Create your views here.


@login_required
def dashboard(request):
    habits = request.user.habits.annotate(
        last_updated=Max('daily_records__date'))
    return render(request, "core/dashboard.html", {"habits": habits})
