

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

