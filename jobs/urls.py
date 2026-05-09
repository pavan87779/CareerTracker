from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.job_list,
        name='job_list'
    ),

    path(
        'add/',
        views.add_job,
        name='add_job'
    ),

    path(
    'edit/<int:job_id>/',
    views.edit_job,
    name='edit_job'
    ),

    path(
    'delete/<int:job_id>/',
    views.delete_job,
    name='delete_job'
    ),

    path(
    'detail/<int:job_id>/',
    views.job_detail,
    name='job_detail'
    ),

    path(
    'note/add/<int:job_id>/',
    views.add_interview_note,
    name='add_interview_note'
    ),

    path(
    'api/',
    views.jobs_api,
    name='jobs_api'
    ),

    path(
    'api/<int:job_id>/',
    views.single_job_api,
    name='single_job_api'
    ),



]