# Payment Integration

This document details the LemonSqueezy payment integration in the Anvil SaaS Boilerplate.

## Overview

The boilerplate includes a complete LemonSqueezy integration with:
- Webhook endpoint for payment events
- Automatic subscription management
- Customer portal access
- Production/Test environment handling
- User permission updates based on subscription status

## Webhook Events

The system handles the following webhook events:

### subscription_created
- Creates new subscription record
- Updates user permissions
- Activates premium features
- Sends welcome email

### subscription_updated
- Updates subscription status
- Adjusts user permissions
- Updates feature access
- Sends status notification

### subscription_payment_success
- Records payment
- Extends subscription period
- Updates billing status
- Sends receipt

## Environment Configuration

The system supports both production and test environments:

### Production
- LEMON_API: Production API key
- LEMON_SIGNING: Production webhook signing secret
- Live product IDs
- Production webhooks

### Test
- LEMON_API_TEST: Test environment API key
- LEMON_SIGNING_TEST: Test webhook signing secret
- Test product IDs
- Test webhooks

## Security Features

### Webhook Security
- Signature verification
- Request validation
- IP whitelisting
- Rate limiting

### Payment Security
- Secure token handling
- PCI compliance
- Data encryption
- Audit logging

## Implementation Details

### Webhook Handler
```python
@anvil.server.http_endpoint('/webhook/lemon')
def handle_webhook():
    # Verify webhook signature
    # Process webhook payload
    # Update subscription status
    # Trigger relevant actions
```

### Customer Portal
```python
@anvil.server.callable
def get_customer_portal_url(user_id):
    # Generate customer portal URL
    # Include return URL
    # Set session duration
    # Return portal URL
```

### Subscription Management
```python
def update_subscription_status(subscription_id, status):
    # Update subscription record
    # Adjust user permissions
    # Update feature access
    # Send notifications
```

## Integration Setup

1. Configure API Keys
   - Add production/test API keys to secrets
   - Set webhook signing secrets
   - Configure product IDs

2. Configure Webhooks
   - Set webhook endpoints
   - Configure event types
   - Set security options

3. Configure Customer Portal
   - Set return URLs
   - Configure branding
   - Set session options

4. Test Integration
   - Verify webhook handling
   - Test subscription flow
   - Validate customer portal
   - Check payment processing

## Best Practices

1. Security
   - Always verify webhook signatures
   - Validate request data
   - Secure API keys
   - Monitor for suspicious activity

2. Error Handling
   - Log all webhook errors
   - Implement retry logic
   - Handle edge cases
   - Monitor failed payments

3. Testing
   - Use test environment
   - Simulate all events
   - Verify error handling
   - Test edge cases

4. Monitoring
   - Log all events
   - Monitor webhook health
   - Track payment success
   - Monitor subscription status

## Troubleshooting

### Common Issues
1. Invalid webhook signatures
   - Check signing secret
   - Verify request headers
   - Check payload formatting

2. Failed payments
   - Check payment details
   - Verify customer info
   - Check subscription status

3. Subscription issues
   - Verify webhook delivery
   - Check subscription record
   - Verify user permissions

### Debug Tools
- Webhook logs
- Payment logs
- Subscription status
- Customer portal logs

## Support

For LemonSqueezy-specific issues:
- Support documentation
- API reference
- Developer forums
- Support tickets
