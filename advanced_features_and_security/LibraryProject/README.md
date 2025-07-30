

# LibraryProject - Django Setup

# Role-Based Access Control (RBAC) in Django

## 📌 Model Permissions

Custom permissions added to the `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## 👥 Groups Created

| Group    | Permissions                         |
|----------|--------------------------------------|
| Viewers  | can_view                             |
| Editors  | can_view, can_create, can_edit       |
| Admins   | All permissions                      |

## 🛡️ View Restrictions

Permission checks applied to all book views using `@permission_required`.

## 🧪 Testing

Tested by assigning users to each group and logging in to verify view access and restrictions.

## 📁 File Locations

- Models: `relationship_app/models.py`
- Views: `relationship_app/views.py`
- Admin: `bookshelf/admin.py`
- Docs: `advanced_features_and_security/README.md`

# Django Security Measures

## HTTPS and Secure Redirects
- Enforced `SECURE_SSL_REDIRECT = True` to ensure all traffic is encrypted.
- Configured HSTS for 1 year with preload and subdomain inclusion.

## Secure Cookies
- Set `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` to True.

## Headers
- Enabled:
  - `X_FRAME_OPTIONS = DENY`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `SECURE_BROWSER_XSS_FILTER = True`

## Deployment
- SSL certificate installed via Nginx for HTTPS support.


