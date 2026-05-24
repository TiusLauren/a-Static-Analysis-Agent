"""Example of code with various issues for testing the analyzer"""
import os
import pickle

# Security issue: hardcoded password
PASSWORD = "admin123"

def complex_function(a, b, c, d, e):
    """Function with high cyclomatic complexity"""
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        return a + b + c + d + e
                    else:
                        return a + b + c + d
                else:
                    return a + b + c
            else:
                return a + b
        else:
            return a
    else:
        return 0

def unsafe_pickle(data):
    """Security issue: unsafe deserialization"""
    return pickle.loads(data)

def sql_injection(user_input):
    """Security issue: SQL injection vulnerability"""
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query

# Style issues
def badNaming( x,y ):
    """Poor naming and spacing"""
    z=x+y
    return z

# Unused import
import sys
