import pytest
import sys
import os

# Add the parent directory to the path so we can import the solution module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solution import validate_email

class TestEmailValidator:
    
    def test_valid_emails(self):
        """Test cases with valid email addresses."""
        valid_emails = [
            "user@example.com",
            "user.name@example.com",
            "user+tag@example.com",
            "user-name@example.com",
            "user_name@example.com",
            "user123@example.com",
            "user@sub.domain.com",
            "user@domain-name.com",
            "a@b.c",  # Minimal valid email
            "user@[123.123.123.123]"  # IP address as domain
        ]
        
        for email in valid_emails:
            assert validate_email(email), f"Expected {email} to be valid"
    
    def test_invalid_emails(self):
        """Test cases with invalid email addresses."""
        invalid_emails = [
            "",  # Empty string
            "user",  # No domain
            "user@",  # No domain after @
            "@domain.com",  # No local part
            "user@.com",  # Domain starts with dot
            "user@domain.",  # Domain ends with dot
            "user@domain@com",  # Multiple @ symbols
            "user..name@domain.com",  # Consecutive dots in local part
            "user.@domain.com",  # Local part ends with dot
            ".user@domain.com",  # Local part starts with dot
            "user@domain..com",  # Consecutive dots in domain
            "user@-domain.com",  # Domain starts with hyphen
            "user@domain-.com",  # Domain part ends with hyphen
            "user@domain_name.com",  # Underscore in domain
            "user name@domain.com",  # Space in email
            "user@domain.c om",  # Space in domain
            123,  # Non-string input
            None,  # None input
            "user@domain"  # Missing TLD
        ]
        
        for email in invalid_emails:
            assert not validate_email(email), f"Expected {email} to be invalid"
    
    def test_edge_cases(self):
        """Test edge cases for email validation."""
        # Very long but valid email
        long_local = "a" * 64
        long_domain = "b" * 63
        long_email = f"{long_local}@{long_domain}.com"
        assert validate_email(long_email), f"Expected {long_email} to be valid"
        
        # Case insensitivity
        assert validate_email("UsEr@ExAmPlE.CoM"), "Expected case-insensitive validation"