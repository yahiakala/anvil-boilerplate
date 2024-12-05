# Anvil SaaS Boilerplate Documentation

This is a comprehensive boilerplate for building SaaS (Software as a Service) applications using Anvil. It provides a robust foundation with built-in features commonly needed in modern SaaS applications.

## Key Features

### Multi-Tenant Architecture
- Built-in support for multiple tenants
- Tenant-specific role management
- Isolated data access per tenant
- Flexible tenant configuration options

### Advanced Authentication System
- Multi-factor authentication (MFA) support
- Email confirmation for new signups
- Remember me functionality
- Secure password requirements
- Google authentication integration
- Token-based authentication support

### Role-Based Access Control (RBAC)
- Granular permission system
- Role-based access management
- Tenant-specific roles
- User-role mapping functionality

### Payment Integration
- LemonSqueezy integration for handling payments
- Webhook support for payment events
- Automatic subscription management
- Customer portal integration
- Test/Production environment switching

## Setup Instructions

1. Clone the repository in your Anvil account
2. Configure your LemonSqueezy API keys in Secrets:
    - LEMON_API: Your LemonSqueezy API key
    - LEMON_SIGNING: Your webhook signing secret
    - (Test versions also supported: LEMON_API_TEST, LEMON_SIGNING_TEST)
3. Configure authentication settings in the Users service:
    - Enable/disable signup features
    - Configure MFA settings
    - Set password requirements
    - Configure email confirmation settings

## Directory Structure

```
├── client_code/           # Client-side application code
│   ├── App/              # Main application components
│   ├── Auth/             # Authentication forms
│   ├── Templates/        # Reusable templates
│   └── Website/          # Public website components
├── server_code/          # Server-side application code
│   └── payments/         # Payment integration
└── theme/                # Application theming
```

