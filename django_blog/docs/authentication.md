# Django Blog Authentication System

## 1. Overview
This authentication system provides:
- User Registration (create new account)
- User Login (authenticate existing users)
- User Logout (securely end session)
- Profile Management (view and update user details)
- Security features (CSRF protection, password hashing)

---

## 2. URL Endpoints

| Path         | View                | Description                            |
|-------------|-------------------|----------------------------------------|
| `/register/` | `register_view`    | New user registration                   |
| `/login/`    | `login_view`       | User login                              |
| `/logout/`   | `logout_view`      | Logs out the user                       |
| `/profile/`  | `profile_view`     | View and update user profile (email)   |
| `/`          | `home`             | Homepage (can show posts later)        |

---

## 3. Templates

| Template File                     | Purpose                                  |
|----------------------------------|-----------------------------------------|
| `blog/templates/blog/register.html` | Registration form                        |
| `blog/templates/blog/login.html`    | Login form                               |
| `blog/templates/blog/profile.html`  | Profile view and edit form               |
| `blog/templates/blog/base.html`     | Base template used by all pages          |

Notes:
- All forms include `{% csrf_token %}` for CSRF protection.
- Django messages framework displays success/error messages.

---

## 4. Forms

- `CustomUserCreationForm` (`blog/forms.py`) extends `UserCreationForm` to include email.
- Fields: `username`, `email`, `password1`, `password2`.
- Automatically validates password matching and required fields.

---

## 5. Views

- **`register_view`** – handles GET/POST for registration, logs in user after successful signup.
- **`login_view`** – authenticates and logs in user; shows error if invalid.
- **`logout_view`** – logs out current user.
- **`profile_view`** – protected with `@login_required`; allows updating user email.

---

## 6. Security Features

- CSRF tokens on all forms
- Passwords hashed using Django's built-in hashers
- `@login_required` ensures profile page is only accessible to logged-in users
- Input validation handled by Django forms

---

## 7. Testing Instructions

1. **Start server:**

```bash
python manage.py runserver
