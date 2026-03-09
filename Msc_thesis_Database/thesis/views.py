from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Department, Student, Supervisor, Thesis, Evaluation, Submission, UserProfile, CommitteeMember
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# ---------------- Home ----------------
def home(request):
    return render(request, 'home.html')

# ---------------- Admin Login ----------------
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_dashboard')
        return render(request, 'admin_login.html', {'error': 'Invalid Login'})
    return render(request, 'admin_login.html')

# ---------------- Professor Login ----------------
def prof_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('prof_dashboard')   # IMPORTANT
        else:
            return render(request,"prof_login.html",{"error":"Invalid credentials"})

    return render(request,"prof_login.html")

# ---------------- Student Login ----------------
def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.role == "student":
                    login(request, user)
                    return redirect('student_dashboard')
                return render(request, 'student_login.html', {'error': "You are not a student"})
            except UserProfile.DoesNotExist:
                return render(request, 'student_login.html', {'error': "User role not assigned"})
        return render(request, 'student_login.html', {'error': "Invalid login"})
    return render(request, 'student_login.html')

# ---------------- Admin Dashboard ----------------

def admin_dashboard(request):
    context = {
        "departments": Department.objects.count(),
        "students": Student.objects.count(),
        "supervisors": Supervisor.objects.count(),
        "theses": Thesis.objects.count(),
        "evaluations": Evaluation.objects.count(),
        "submissions": Submission.objects.count(),
    }
    return render(request, "admin_dashboard.html", context)

# ---------------- Professor Dashboard ----------------
def prof_dashboard(request):

    supervisor = Supervisor.objects.get(user=request.user)

    theses = Thesis.objects.filter(supervisor=supervisor)

    total = theses.count()
    pending = theses.filter(status="Pending").count()
    approved = theses.filter(status="Approved").count()

    context = {
        'theses': theses,
        'total': total,
        'pending': pending,
        'approved': approved
    }

    return render(request, "prof_dashboard.html", context)
# ---------------- Student Dashboard ----------------

@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    thesis = Thesis.objects.filter(student=student).first()
    submissions = Submission.objects.filter(thesis=thesis)

    if request.method == "POST":
        Submission.objects.create(
            thesis=thesis,
            version=request.POST.get("version"),
            thesis_file=request.FILES.get("thesis_file"),
            approval_status="Pending"
        )
        return redirect("student_dashboard")

    context = {
        "student": student,
        "thesis": thesis,
        "submissions": submissions
    }
    return render(request, "student_dashboard.html", context)

# ---------------- Add Department ----------------
@login_required
def add_department(request):
    if request.method == "POST":
        Department.objects.create(
            department_name=request.POST['department_name'],
            office_location=request.POST['office_location']
        )
        return redirect("admin_dashboard")
    return render(request, "admin/add_department.html")

# ---------------- Add Student ----------------
@login_required
def add_student(request):
    departments = Department.objects.all()
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['email'],
            password=request.POST['password']
        )
        Student.objects.create(
            user=user,
            student_name=request.POST['student_name'],
            email=request.POST['email'],
            batch=request.POST['batch'],
            program=request.POST['program'],
            department=Department.objects.get(department_id=request.POST['department'])
        )
        UserProfile.objects.create(user=user, role="student")
        return redirect("admin_dashboard")
    return render(request, "admin/add_student.html", {'departments': departments})

# ---------------- Add Supervisor ----------------
@login_required
def add_supervisor(request):
    departments = Department.objects.all()
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['email'],
            password=request.POST['password']
        )
        Supervisor.objects.create(
            user=user,
            supervisor_name=request.POST['supervisor_name'],
            email=request.POST['email'],
            designation=request.POST['designation'],
            department=Department.objects.get(department_id=request.POST['department'])
        )
        UserProfile.objects.create(user=user, role="professor")
        return redirect("admin_dashboard")
    return render(request, "admin/add_supervisor.html", {'departments': departments})

# ---------------- Add Thesis ----------------
@login_required
def add_thesis(request):
    students = Student.objects.all()
    supervisors = Supervisor.objects.all()
    if request.method == "POST":
        Thesis.objects.create(
            title=request.POST['title'],
            abstract=request.POST['abstract'],
            submission_year=request.POST['submission_year'],
            status=request.POST['status'],
            student=Student.objects.get(student_id=request.POST['student']),
            supervisor=Supervisor.objects.get(supervisor_id=request.POST['supervisor'])
        )
        return redirect("admin_dashboard")
    return render(request, "admin/add_thesis.html", {'students': students, 'supervisors': supervisors})

# ---------------- Add Evaluation ----------------
@login_required
def add_evaluation(request):
    theses = Thesis.objects.all()
    if request.method == "POST":
        Evaluation.objects.create(
            thesis=Thesis.objects.get(thesis_id=request.POST['thesis']),
            evaluation_date=request.POST['evaluation_date'],
            marks=request.POST['marks'],
            result=request.POST['result']
        )
        return redirect("admin_dashboard")
    return render(request, "admin/add_evaluation.html", {'theses': theses})

# ---------------- Add Submission ----------------
@login_required
def add_submission(request):
    theses = Thesis.objects.all()
    if request.method == "POST":
        Submission.objects.create(
            thesis=Thesis.objects.get(thesis_id=request.POST['thesis']),
            submission_date=request.POST['submission_date'],
            version=request.POST['version'],
            approval_status=request.POST['approval_status'],
            thesis_file=request.FILES.get("thesis_file")
        )
        return redirect("admin_dashboard")
    return render(request, "admin/add_submission.html", {'theses': theses})