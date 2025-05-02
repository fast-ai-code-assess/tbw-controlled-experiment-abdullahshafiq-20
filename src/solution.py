import re

def validate_email(email):
    """
    Validates an email address according to standard formatting rules.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if the email is valid, False otherwise
    """
    if not isinstance(email, str):
        return False
    
    # Regular expression for email validation
    # This pattern checks for:
    # 1. Local part: alphanumeric, dots, plus, minus, underscore (but dots can't be consecutive or at start/end)
    # 2. @ symbol
    # 3. Domain: alphanumeric, dots, hyphens (but can't start/end with hyphen or dot)
    # 4. TLD must be present (at least one character after the last dot)
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,}$'
    
    # Basic regex match
    if not re.match(pattern, email):
        return False
    
    # Additional checks for edge cases not easily handled by regex alone
    
    # Check for consecutive dots in local part or domain
    if '..' in email:
        return False
    
    # Split the email into local and domain parts
    local, domain = email.rsplit('@', 1)
    
    # Check if local part starts or ends with a dot
    if local.startswith('.') or local.endswith('.'):
        return False
    
    # Check if domain starts or ends with hyphen or dot
    if domain.startswith('.') or domain.startswith('-') or domain.endswith('-'):
        return False
    
    # Check for invalid characters in domain (underscores are not allowed)
    if '_' in domain:
        return False
    
    # Check for spaces in the email address
    if ' ' in email:
        return False
    
    # Special case for IP address domains
    if domain.startswith('[') and domain.endswith(']'):
        # Strip the brackets for IP validation
        ip = domain[1:-1]
        # Simple check for IPv4 format (more comprehensive validation could be added)
        ip_parts = ip.split('.')
        if len(ip_parts) != 4:
            return False
        for part in ip_parts:
            try:
                num = int(part)
                if num < 0 or num > 255:
                    return False
            except ValueError:
                return False
    
    return True