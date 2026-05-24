"""Example of clean, well-structured code"""
from typing import List


def calculate_sum(numbers: List[int]) -> int:
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers: List of integers to sum
        
    Returns:
        The sum of all numbers
    """
    return sum(numbers)


def validate_email(email: str) -> bool:
    """
    Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not email or '@' not in email:
        return False
    
    parts = email.split('@')
    return len(parts) == 2 and all(parts)


class DataProcessor:
    """Process and transform data safely"""
    
    def __init__(self, data: List[dict]):
        self.data = data
    
    def filter_by_key(self, key: str, value: any) -> List[dict]:
        """Filter data by key-value pair"""
        return [item for item in self.data if item.get(key) == value]
    
    def count_items(self) -> int:
        """Count total items"""
        return len(self.data)
