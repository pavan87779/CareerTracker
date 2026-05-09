from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .forms import ResumeForm
from .models import Resume


# UPLOAD RESUME

@login_required
def upload_resume(request):

    if request.method == 'POST':

        form = ResumeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            resume = form.save(commit=False)

            resume.user = request.user

            resume.save()

            return redirect('resume_list')

    else:

        form = ResumeForm()

    return render(
        request,
        'resumes/upload_resume.html',
        {'form': form}
    )


# RESUME LIST

@login_required
def resume_list(request):

    resumes = Resume.objects.filter(
        user=request.user
    ).order_by('-uploaded_at')

    return render(
        request,
        'resumes/resume_list.html',
        {'resumes': resumes}
    )


# DELETE RESUME

@login_required
def delete_resume(request, resume_id):

    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    if request.method == 'POST':

        resume.delete()

        return redirect('resume_list')

    return render(
        request,
        'resumes/delete_resume.html',
        {'resume': resume}
    )