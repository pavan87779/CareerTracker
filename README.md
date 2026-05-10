CareerTracker – Job Application Tracker & Career Dashboard

Overview

CareerTracker is a full-stack Django web application designed to help users efficiently manage and track their job applications, interview progress, resumes, recruiter communication, and career analytics through a centralized dashboard system.

The project demonstrates real-world full-stack web development concepts including authentication, CRUD operations, dashboard analytics, REST-style APIs, pagination, filtering, responsive UI design, and file handling.


---

Features

Authentication System

User Registration

User Login & Logout

Password Change

Protected Routes using @login_required

Session-Based Authentication

CSRF Protection



---

Dashboard Analytics

Total Applications Count

Interviews Count

Rejections Count

Offers Count

Pending Applications

Joined Applications

Interactive Analytics Charts using Chart.js



---

Job Application Management

Users can:

Add Job Applications

Edit Job Applications

Delete Job Applications

Track:

Company Name

Role

Location

Salary

Status

Application Date

Recruiter Details

Notes




---

Application Status Tracking

Supported statuses:

Applied

OA Scheduled

Interview Scheduled

HR Round

Rejected

Offer Received

Joined



---

Resume Management

Upload Resumes

Store Resume Versions

Download Resume Files

Resume Tracking



---

Interview Notes System

Store Technical Questions

Store HR Questions

Save Feedback Notes

Save Preparation Notes



---

Search, Filter & Sorting

Search by Company Name

Filter by Application Status

Sort by Latest/Oldest Applications



---

Pagination

Efficiently manage large numbers of applications

Improved scalability and performance



---

REST-Style APIs

Implemented JSON API endpoints using Django JsonResponse.

Example:

/jobs/api/

/jobs/api/<id>/

/dashboard/api/



---

Responsive UI

Responsive Bootstrap Design

Mobile-Friendly Layout

Interactive Dashboard Cards

Modern UI Components



---

Tech Stack

Backend

Python

Django

SQLite


Frontend

HTML

CSS

JavaScript

Bootstrap

Chart.js


Tools & Concepts

Django ORM

CRUD Operations

Authentication & Authorization

REST APIs

Pagination

File Upload Handling

Database Relationships

Responsive Web Design



---

Project Architecture

Django follows the MVT (Model-View-Template) architecture.

Models

Handle database structure and database operations.

Views

Contain backend business logic and request handling.

Templates

Handle frontend UI rendering using HTML, CSS, Bootstrap, and Django Template Language.


---

Database Models

JobApplication

Stores:

Company Name

Role

Status

Salary

Application Date

Recruiter Details

Notes



---

Resume

Stores uploaded resumes using Django FileField.


---

InterviewNote

Stores:

Technical Questions

HR Questions

Interview Feedback

Preparation Notes



---

Security Features

CSRF Protection

Secure Authentication

Password Validation

Protected Routes

POST-Based Logout

Session Management



---

APIs

The project includes REST-style JSON API endpoints.

Example API Response

{
    "company_name": "Google",
    "role": "Software Engineer",
    "status": "Interview Scheduled"
}


---

Screenshots

Home Page

Add screenshot here


---

Dashboard

Add screenshot here


---

Job Applications Page

Add screenshot here


---

Resume Management

Add screenshot here


---

Installation & Setup

Clone Repository

git clone https://github.com/pavan87779/CareerTracker.git


---

Navigate to Project

cd CareerTracker


---

Create Virtual Environment

python -m venv venv


---

Activate Virtual Environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate


---

Install Dependencies

pip install -r requirements.txt


---

Run Migrations

python manage.py migrate


---

Start Development Server

python manage.py runserver


---

Open in Browser

http://127.0.0.1:8000/


---

Deployment

The project can be deployed using:

Render

Railway

PythonAnywhere

AWS



---

Future Improvements

Email Notifications

AI Resume Analyzer

Job Recommendation System

Export Reports to PDF/Excel

Django REST Framework Integration

AJAX-Based Dynamic UI

Cloud Deployment



---

Learning Outcomes

This project helped strengthen:

Full-Stack Web Development

Django Framework

Authentication Systems

CRUD Operations

Database Management

APIs & JSON

Dashboard Analytics

Responsive UI Design

Backend Architecture

Problem Solving



---

Resume Description

Developed a full-stack CareerTracker web application using Django, Python, SQL, HTML, CSS, JavaScript, Bootstrap, and Chart.js to manage job applications, interview tracking, resume uploads, and analytics dashboards with authentication, CRUD operations, pagination, filtering, and REST-style APIs.


---

Author

Pavan Babu

Python Full-Stack Developer | Django Developer | Data Analyst Enthusiast
