from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from core.models import DailyRecord
from datetime import date
from core.forms import DailyRecordForm
# Create your views here.


@login_required
def dashboard(request):
    habits = request.user.habits.annotate(
        last_updated=Max('daily_records__date'))
    return render(request, "core/dashboard.html", {
        "habits": habits,
        "today": date.today()
    })


@login_required
def update_daily_record(request, habit_pk, year, month, day):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    try:
        record = habit.daily_records.get(date=date(year, month, day))
    except DailyRecord.DoesNotExist:
        record = DailyRecord(habit=habit, date=date(year, month, day))

    form = DailyRecordForm(data=request.POST, instance=record)

    if request.method == "POST" and form.is_valid():
        record = form.save()
    return render(request, "core/update_record.html", {
        "habit": habit,
        "record": record,
        "form": form,
    })
