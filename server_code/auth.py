import anvil.server
from anvil.tables import app_tables
import anvil.users
import anvil.email

import hashlib
import requests
import secrets
import base64

@anvil.server.callable
def login_with_email_mfa(email, password):
    """Try to log user in without MFA. Return exception if user has MFA configured."""
    import bcrypt
    user = app_tables.users.get(email=email)
    if user:
        if user['n_password_failures'] is not None and user['n_password_failures'] >= 10:
            raise anvil.users.TooManyPasswordFailures('You have reached your limit of password attempts. Please reset your password.')
        elif user['mfa'] is not None:
            raise anvil.users.MFARequired('User needs to enter MFA credentials.')
        elif user['confirmed_email'] != True:
            raise anvil.users.EmailNotConfirmed('Please confirm your email before logging in.')
        elif bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            anvil.users.force_login(user, remember=True)
            user['n_password_failures'] = 0
            return user
        else:
            user['n_password_failures'] += 1
            raise anvil.users.AuthenticationFailed('Email or password is incorrect.')
    else:
        raise anvil.users.AuthenticationFailed('Email or password is incorrect.')


def is_password_pwned(password):
    """Check if a password has been leaked using the "Have I Been Pwned" API."""
    # Compute the SHA-1 hash of the password
    sha1sum = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    first5_chars = sha1sum[:5]
    url = f"https://api.pwnedpasswords.com/range/{first5_chars}"
    response = anvil.http.request(url, method="GET", headers={"User-Agent": "Anvil"})
    response_text = response.get_bytes().decode('utf-8')
    
    # Parse the API response
    hashes = (line.split(':') for line in response_text.splitlines())
    
    # Check if the rest of our hash is in the response
    tail = sha1sum[5:]
    for hash_tail, count in hashes:
        if hash_tail == tail:
            return True
    
    return False


def generate_confirmation_key(length=10):
    """Generate a secure random byte string of adequate length."""
    # The length needs to be adjusted because base64 encoding increases the size
    # Here, we aim for approximately the same number of URL-safe characters as the desired length
    random_bytes = secrets.token_bytes(length)
    # Encode the bytes in base64 and ensure URL safety (replace '+' with '-', '/' with '_')
    # Also, strip off the '==' padding for a cleaner URL part
    confirmation_key = base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')
    # Return the confirmation key with the desired length
    return confirmation_key[:length]


def create_new_user(email, password, confirm_email=False, require_mfa=False, mfa_method=None, remember=False):
    """Create a new user."""
    import bcrypt
    # Hash the password with bcrypt
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Prepare the user data dictionary
    user_data = {
        'email': email,
        'password_hash': password_hash,
    }
    
    if confirm_email:
        confirmation_key = generate_confirmation_key()
        user_data['confirmed_email'] = False
        user_data['email_confirmation_key'] = confirmation_key
    
    if require_mfa:
        user_data['mfa'] = [mfa_method]
    
    new_user_row = app_tables.users.add_row(**user_data)

    if remember and not confirm_email:
        new_user_row = anvil.users.force_login(new_user_row, remember=True)

    return new_user_row


def generate_confirmation_url(email, confirmation_key):
    """Generate confirmation email."""
    import urrllib.parse
    # URL-encode the email and confirmation key
    encoded_email = urllib.parse.quote(email)
    encoded_confirmation_key = urllib.parse.quote(confirmation_key)
    # Format the confirmation URL
    confirm_url = f"{anvil.server.get_app_origin()}/_/email-confirm/{encoded_email}/{encoded_confirmation_key}"
    return confirm_url


@anvil.server.callable
def send_confirmation_email(email, confirmation_key, confirm_email):
    # Check if we need to send a confirmation email
    if confirm_email:
        # Generate the confirmation URL
        confirm_url = generate_confirmation_url(email, confirmation_key)
        
        # Define the email properties
        subject = "Please confirm your email address"
        body = f"""Hello,

Please click on the link below to confirm your email address:

{confirm_url}

Thank you."""

        # Send the email
        anvil.email.send(to=email, subject=subject, text=body)
    # Optionally, you could return a value or message indicating success or next steps
    return "Confirmation email sent" if confirm_email else "No confirmation needed"
