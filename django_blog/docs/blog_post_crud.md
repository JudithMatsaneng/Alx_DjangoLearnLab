# Blog Post Management Features

## Overview
Users can create, view, update, and delete posts. Only authenticated users can create posts. Only authors can edit or delete their own posts.

## URLs
- List: `/` 
- Detail: `/posts/<id>/`
- Create: `/posts/new/`
- Update: `/posts/<id>/edit/`
- Delete: `/posts/<id>/delete/`

## Templates
- `post_list.html` → shows all posts
- `post_detail.html` → individual post
- `post_form.html` → create/edit post
- `post_confirm_delete.html` → delete confirmation

## Permissions
- `LoginRequiredMixin` → create/edit/delete requires login
- `UserPassesTestMixin` → only author can edit/delete
