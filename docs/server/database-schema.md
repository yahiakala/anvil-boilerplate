# Database Schema

This document outlines the database schema used in the application.

## Overview

The database schema defines the structure and relationships of the data stored in the application. All tables have server-side "full" access and client-side "none" access for security.

## Tables

### Users

| Column Name | Type | Description | Admin UI Width |
|------------|------|-------------|----------------|
| email | string | User's email address | 200 |
| enabled | bool | Account status flag | 200 |
| last_login | datetime | Last login timestamp | 200 |
| password_hash | string | Hashed password | 200 |
| n_password_failures | number | Count of password failures | 200 |
| confirmed_email | bool | Email confirmation status | 200 |
| remembered_logins | simpleObject | Stored login information | 200 |
| mfa | simpleObject | Multi-factor authentication data | 200 |
| signed_up | datetime | Account creation timestamp | 200 |
| roles | link_multiple | Links to roles table | 200 |
| email_confirmation_key | string | Email confirmation token | 200 |

### Roles

| Column Name | Type | Description | Admin UI Width |
|------------|------|-------------|----------------|
| name | string | Role name | 200 |
| permissions | link_multiple | Links to permissions table | 200 |
| tenant | link_single | Link to tenants table | 200 |
| can_edit | bool | Edit permission flag | 200 |

### Permissions

| Column Name | Type | Description | Admin UI Width |
|------------|------|-------------|----------------|
| name | string | Permission name | 200 |
| description | string | Permission description | 200 |

### Tenants

| Column Name | Type | Description | Admin UI Width |
|------------|------|-------------|----------------|
| name | string | Tenant name | 200 |
| new_roles | simpleObject | Tenant role configuration | 200 |

### UserTenant

| Column Name | Type | Description | Admin UI Width |
|------------|------|-------------|----------------|
| user | link_single | Link to users table | 200 |
| tenant | link_single | Link to tenants table | 200 |
| roles | link_multiple | Links to roles table | 200 |

## Relationships

- Users can have multiple Roles (many-to-many through roles column)
- Roles can have multiple Permissions (many-to-many through permissions column)
- Roles belong to a Tenant (many-to-one through tenant column)
- Users can belong to multiple Tenants through UserTenant table (many-to-many)
- UserTenant links Users to Tenants and assigns Roles within that context
