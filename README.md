# MSc Thesis Management System

A professional Django-based Master's Thesis Management System with modular, production-ready architecture. This system manages the complete thesis lifecycle including student submissions, supervisor evaluations, and administrative oversight.

## 🎯 Features

### For Students
- 📝 Submit thesis documents in multiple versions
- 📊 Track submission status and evaluations
- 👁️ View feedback from supervisors and committee
- 📱 Responsive student dashboard

### For Supervisors/Professors
- 👥 Manage assigned thesis topics
- ✅ Review and evaluate student submissions
- 📋 Track thesis progress
- 🎓 Provide feedback and marks
- 📊 View department statistics

### For Administrators
- 🏛️ Manage departments and staff
- 👤 Create and manage user accounts
- 📚 Oversee all theses in the system
- 📈 Generate system-wide reports
- 🔐 Control access and permissions

## 🏗️ Architecture

This is a refactored Django application organized into 6 focused, domain-specific apps:

```
apps/
├── accounts/         Authentication & User Management
├── departments/      Department Management
├── students/         Student Management & Dashboard
├── supervisors/      Supervisor Management & Dashboard
├── theses/          Thesis Lifecycle & Operations
└── common/          Shared Utilities & Decorators
```

Each app contains:
- `models.py` - Database models
- `views.py` - Request handlers
- `forms.py` - Input validation
- `urls.py` - URL routing
- `admin.py` - Admin interface
- `apps.py` - App configuration

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 6.0+
- SQLite3 (included with Python)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Janak017/Msc_theses_system.git
cd Msc_theses_system
```

2. **Create a virtual environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install django
```

4. **Run migrations**
```bash
cd Msc_thesis_Database
python manage.py migrate
```

5. **Create a superuser (admin account)**
```bash
python manage.py createsuperuser
```

6. **Start the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Home: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Student Login: http://localhost:8000/login/
- Professor Login: http://localhost:8000/professor-login/
- Admin Login: http://localhost:8000/admin-login/

## 📚 Project Structure

```
Msc_thesis_Database/
├── apps/                        # Application modules
│   ├── accounts/                # Authentication & Authorization
│   ├── departments/             # Department Management
│   ├── students/                # Student Management
│   ├── supervisors/             # Supervisor Management
│   ├── theses/                  # Thesis Management
│   └── common/                  # Shared Utilities
├── templates/                   # HTML templates
├── static/                      # CSS, JavaScript, Images
├── media/                       # User uploads (thesis files)
├── Msc_thesis_Database/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py                    # Django CLI
├── db.sqlite3                   # Database
└── README.md                    # This file
```

## 🔐 User Roles & Access Control

### Admin
- Full system access
- Manage all users and data
- View all reports
- Access: `/admin-login/`

### Professor/Supervisor
- View assigned thesis topics
- Evaluate student submissions
- Provide feedback and marks
- Access: `/professor-login/`

### Student
- Submit thesis documents
- View own evaluations
- Track progress
- Access: `/login/`

## 🛠️ Development

### Running Tests
```bash
python manage.py test
python manage.py test apps.students
python manage.py test apps.theses
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Admin Interface
Access at `/admin/` with superuser credentials. Full admin configuration available for:
- Users & Profiles
- Departments
- Students
- Supervisors
- Theses
- Evaluations
- Submissions
- Committee Members

## 📖 Key URLs

### Authentication
| URL | Purpose |
|-----|---------|
| `/` | Home page |
| `/login/` | Student login |
| `/professor-login/` | Professor login |
| `/admin-login/` | Admin login |
| `/logout/` | Logout |

### Departments
| URL | Purpose |
|-----|---------|
| `/departments/` | List departments |
| `/departments/add/` | Create department |
| `/departments/<id>/edit/` | Edit department |
| `/departments/<id>/delete/` | Delete department |

### Students
| URL | Purpose |
|-----|---------|
| `/students/` | List students |
| `/students/add/` | Create student |
| `/students/<id>/edit/` | Edit student |
| `/students/dashboard/` | Student dashboard |

### Supervisors
| URL | Purpose |
|-----|---------|
| `/supervisors/` | List supervisors |
| `/supervisors/add/` | Create supervisor |
| `/supervisors/<id>/edit/` | Edit supervisor |
| `/supervisors/dashboard/` | Professor dashboard |

### Theses
| URL | Purpose |
|-----|---------|
| `/theses/` | List theses |
| `/theses/add/` | Create thesis |
| `/theses/<id>/` | View thesis details |
| `/theses/admin/dashboard/` | Admin dashboard |
| `/theses/evaluation/add/` | Add evaluation |
| `/theses/submission/add/` | Add submission |

## 🔄 Common Workflows

### Adding a New Student
1. Login as admin
2. Go to `/students/add/`
3. Fill in student details
4. System automatically creates user account

### Submitting a Thesis
1. Login as student
2. Go to `/students/dashboard/`
3. Click "Submit Thesis"
4. Upload thesis file
5. Track submission status

### Evaluating a Thesis
1. Login as professor
2. Go to `/supervisors/dashboard/`
3. Select assigned thesis
4. Click "Evaluate"
5. Enter marks and feedback

## 🎨 Customization

### Adding a New Feature

1. **Update Models** (`apps/app_name/models.py`)
```python
class NewModel(models.Model):
    field1 = models.CharField(max_length=100)
    # Add fields as needed
```

2. **Create Form** (`apps/app_name/forms.py`)
```python
class NewModelForm(forms.ModelForm):
    class Meta:
        model = NewModel
        fields = ['field1', ...]
```

3. **Add Views** (`apps/app_name/views.py`)
```python
@admin_required
def new_view(request):
    # Your view logic
```

4. **Add URLs** (`apps/app_name/urls.py`)
```python
path('route/', views.new_view, name='route_name'),
```

5. **Register in Admin** (`apps/app_name/admin.py`)
```python
@admin.register(NewModel)
class NewModelAdmin(admin.ModelAdmin):
    list_display = ('field1',)
```

6. **Run Migrations**
```bash
python manage.py makemigrations apps.app_name
python manage.py migrate
```

## 📊 Database Schema

The system uses SQLite with the following main models:

- **User** - Django built-in user authentication
- **UserProfile** - Extended user info with role
- **Department** - Academic departments
- **Student** - Student information
- **Supervisor** - Professor/supervisor info
- **Thesis** - Thesis topic and status
- **Evaluation** - Evaluation scores and feedback
- **Submission** - Thesis file submissions
- **CommitteeMember** - Evaluation committee members
- **ThesisCommittee** - Join table for thesis committees

## 🔒 Security Features

- ✅ CSRF protection on all forms
- ✅ SQL injection prevention via Django ORM
- ✅ Role-based access control with decorators
- ✅ Password hashing with Django's authentication system
- ✅ Form validation and input sanitization
- ✅ Session-based authentication

## ⚡ Performance

- Database indexes on frequently queried fields
- Optimized model relationships
- Ready for caching implementation
- Efficient query patterns established

## 📝 Documentation

Comprehensive documentation is available in the documentation folder:

- **REFACTORING_README.md** - Detailed architecture and usage guide
- **MIGRATION_GUIDE.md** - Step-by-step migration instructions
- **REFACTORING_SUMMARY.md** - Overview of changes and improvements
- **BEFORE_AFTER_COMPARISON.md** - Code examples showing improvements

## 🐛 Troubleshooting

### Import Errors
```
ModuleNotFoundError: No module named 'apps'
```
- Solution: Ensure `apps/__init__.py` exists and INSTALLED_APPS is updated

### Migration Conflicts
```bash
python manage.py showmigrations  # Check migration status
python manage.py migrate --check  # Verify migrations
```

### Database Lock
```bash
rm db.sqlite3  # Remove and recreate database
python manage.py migrate
python manage.py createsuperuser
```

### Port Already in Use
```bash
python manage.py runserver 8001  # Use different port
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Development Standards

- Follow Django conventions
- Use type hints where applicable
- Write docstrings for functions
- Maintain consistent code style
- Add tests for new features
- Update documentation

## 📞 Support & Issues

For issues, questions, or suggestions:
1. Check existing documentation
2. Review the troubleshooting section
3. Open an issue on GitHub
4. Check REFACTORING_README.md for detailed guidance

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Janak017** - Initial development and refactoring

## 🙏 Acknowledgments

- Django documentation and best practices
- Community contributions
- Academic thesis management standards

## 📅 Changelog

### Version 1.0 (Current)
- ✨ Refactored from monolithic to modular architecture
- ✨ 6 focused, domain-specific apps
- ✨ Improved code organization and maintainability
- ✨ Enhanced security and performance
- ✨ Comprehensive documentation
- ✨ Professional Django best practices implementation

---

**Status**: Production Ready  
**Last Updated**: July 25, 2026  
**Version**: 1.0
