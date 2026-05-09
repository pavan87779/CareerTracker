from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from django.contrib import messages

from django.http import JsonResponse

from .forms import JobApplicationForm

from .forms_notes import InterviewNoteForm

from .models import (
    JobApplication,
    InterviewNote
)


# ==============================
# ADD JOB
# ==============================

@login_required
def add_job(request):

    if request.method == 'POST':

        form = JobApplicationForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.user = request.user

            job.save()

            messages.success(
                request,
                'Application added successfully!'
            )

            return redirect('job_list')

    else:

        form = JobApplicationForm()

    return render(
        request,
        'jobs/add_job.html',
        {'form': form}
    )


# ==============================
# JOB LIST
# SEARCH + FILTER + SORT + PAGINATION
# ==============================

@login_required
def job_list(request):

    jobs = request.user.jobapplication_set.all()

    # SEARCH

    search_query = request.GET.get('search')

    if search_query:

        jobs = jobs.filter(
            company_name__icontains=search_query
        )

    # FILTER BY STATUS

    status_filter = request.GET.get('status')

    if status_filter:

        jobs = jobs.filter(
            status=status_filter
        )

    # SORTING

    sort_order = request.GET.get('sort')

    if sort_order == 'oldest':

        jobs = jobs.order_by('application_date')

    else:

        jobs = jobs.order_by('-application_date')

    # PAGINATION

    paginator = Paginator(jobs, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {

        'jobs': page_obj,

        'page_obj': page_obj,

        'search_query': search_query,

        'status_filter': status_filter,

        'sort_order': sort_order,
    }

    return render(
        request,
        'jobs/job_list.html',
        context
    )


# ==============================
# EDIT JOB
# ==============================

@login_required
def edit_job(request, job_id):

    job = get_object_or_404(
        JobApplication,
        id=job_id,
        user=request.user
    )

    if request.method == 'POST':

        form = JobApplicationForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Application updated successfully!'
            )

            return redirect('job_list')

    else:

        form = JobApplicationForm(instance=job)

    return render(
        request,
        'jobs/edit_job.html',
        {'form': form}
    )


# ==============================
# DELETE JOB
# ==============================

@login_required
def delete_job(request, job_id):

    job = get_object_or_404(
        JobApplication,
        id=job_id,
        user=request.user
    )

    if request.method == 'POST':

        job.delete()

        messages.success(
            request,
            'Application deleted successfully!'
        )

        return redirect('job_list')

    return render(
        request,
        'jobs/delete_job.html',
        {'job': job}
    )


# ==============================
# JOB DETAIL
# ==============================

@login_required
def job_detail(request, job_id):

    job = get_object_or_404(
        JobApplication,
        id=job_id,
        user=request.user
    )

    notes = InterviewNote.objects.filter(
        job_application=job
    ).order_by('-created_at')

    context = {

        'job': job,

        'notes': notes,
    }

    return render(
        request,
        'jobs/job_detail.html',
        context
    )


# ==============================
# ADD INTERVIEW NOTE
# ==============================

@login_required
def add_interview_note(request, job_id):

    job = get_object_or_404(
        JobApplication,
        id=job_id,
        user=request.user
    )

    if request.method == 'POST':

        form = InterviewNoteForm(request.POST)

        if form.is_valid():

            note = form.save(commit=False)

            note.job_application = job

            note.save()

            messages.success(
                request,
                'Interview note added successfully!'
            )

            return redirect(
                'job_detail',
                job_id=job.id
            )

    else:

        form = InterviewNoteForm()

    context = {

        'form': form,

        'job': job,
    }

    return render(
        request,
        'jobs/add_interview_note.html',
        context
    )


# ==============================
# JOBS API
# ==============================

@login_required
def jobs_api(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    )

    data = []

    for job in jobs:

        data.append({

            'id': job.id,

            'company_name': job.company_name,

            'role': job.role,

            'location': job.location,

            'salary': str(job.salary),

            'status': job.status,

            'application_date': str(job.application_date),

            'notes': job.notes,
        })

    return JsonResponse(
        data,
        safe=False,
        json_dumps_params={'indent': 4}
    )


# ==============================
# SINGLE JOB API
# ==============================

@login_required
def single_job_api(request, job_id):

    job = get_object_or_404(
        JobApplication,
        id=job_id,
        user=request.user
    )

    data = {

        'id': job.id,

        'company_name': job.company_name,

        'role': job.role,

        'location': job.location,

        'salary': str(job.salary),

        'status': job.status,

        'application_date': str(job.application_date),

        'notes': job.notes,
    }

    return JsonResponse(
        data,
        json_dumps_params={'indent': 4}
    )