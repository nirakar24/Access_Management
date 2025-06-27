# Access Management App

A Django web application for group-based access control with user-friendly navigation and modern styling.

## Features
- User registration (sign up) with group selection
- User login/logout
- Group-based access to three protected views (View 1, View 2, View 3)
- Homepage with navigation
- Dashboard showing user info, group(s), and navigation buttons
- Modern, responsive UI with custom CSS

## Setup Instructions

1. **Clone the repository** (if not already in your workspace):
   ```bash
   git clone <repo-url>
   cd Access_management_app
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Create Groups**
   - Go to `/admin/` and log in as the superuser.
   - Under "Groups", create three groups: `Group 1`, `Group 2`, and `Group 3`.

## Usage

- **Homepage** (`/`):
  - If not logged in, shows Login and Sign Up buttons.
  - If logged in, shows Dashboard and Logout buttons.

- **Sign Up** (`/signup/`):
  - Register a new user and select a group to join.

- **Login** (`/login/`):
  - Log in with your username and password.
  - After login, you are redirected to the homepage.

- **Dashboard** (`/dashboard/`):
  - Shows your username and group(s).
  - Navigation buttons for View 1, View 2, and View 3.
  - Buttons are disabled for views you cannot access.

- **Protected Views** (`/view1/`, `/view2/`, `/view3/`):
  - Only accessible to users in the corresponding group.
  - Unauthorized access returns a 403 Forbidden message.

- **Logout** (`/logout/`):
  - Logs you out and returns you to the homepage.

## Customization
- Update CSS in `main/static/main/style.css` for branding or layout changes.
- Edit templates in `main/templates/` for custom UI/UX.
- Add more groups or views as needed via Django admin.

## Notes
- Passwords have no restrictions for sign up (for demo/testing purposes).
- Make sure to create the three groups in the admin before user registration.

---

**Enjoy using your group-based access management platform!** 