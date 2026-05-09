from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from jobs.models import JobApplication
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    )

    total_applications = jobs.count()

    interviews = jobs.filter(
        status='Interview Scheduled'
    ).count()

    rejected = jobs.filter(
        status='Rejected'
    ).count()

    offers = jobs.filter(
        status='Offer Received'
    ).count()

    joined = jobs.filter(
        status='Joined'
    ).count()

    pending = jobs.exclude(
        status__in=[
            'Rejected',
            'Offer Received',
            'Joined'
        ]
    ).count()

    recent_jobs = jobs.order_by(
        '-created_at'
    )[:5]

    context = {

        'total_applications': total_applications,

        'interviews': interviews,

        'rejected': rejected,

        'offers': offers,

        'joined': joined,

        'pending': pending,

        'recent_jobs': recent_jobs,
    }

    return render(
        request,
        'dashboard.html',
        context
    )

@login_required
def dashboard_api(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    )

    data = {

        'total_applications': jobs.count(),

        'interviews': jobs.filter(
            status='Interview Scheduled'
        ).count(),

        'rejected': jobs.filter(
            status='Rejected'
        ).count(),

        'offers': jobs.filter(
            status='Offer Received'
        ).count(),

        'joined': jobs.filter(
            status='Joined'
        ).count(),
    }

    return JsonResponse(data)