# Comment System for Django Blog

## Overview
Users can leave comments on blog posts. Only logged-in users can add, edit, or delete their own comments.

## URL Patterns
- Add comment: `/post/<post_id>/comments/new/`
- Edit comment: `/comment/<comment_id>/edit/`
- Delete comment: `/comment/<comment_id>/delete/`

## Permissions
- Only authenticated users can add comments.
- Only comment author can edit/delete.

## Templates
- `comment_form.html` → used for add/edit
- Comments are displayed in `post_detail.html` template.
