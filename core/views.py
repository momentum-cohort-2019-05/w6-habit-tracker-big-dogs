from django.shortcuts import render, get_object_or_404, redirect
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
def update_daily_record(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    record_date = request.POST.get('date', date.today())
    try:
        record = habit.daily_records.get(date=record_date)
    except DailyRecord.DoesNotExist:
        record = DailyRecord(habit=habit, date=record_date)

    if request.method == "POST":
        form = DailyRecordForm(data=request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect(to='dashboard')
    else:
        form = DailyRecordForm(instance=record)

    return render(request, "core/update_record.html", {
        "habit": habit,
        "record": record,
        "form": form,
    })
