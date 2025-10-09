#!/usr/bin/env python
"""
Quick script to reset the database for demo purposes
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'machine_test_project.settings')
django.setup()

from django.core.management import execute_from_command_line

def reset_database():
    """Reset database to empty state for demo"""
    print("🔄 Resetting database for demo...")
    
    # Delete database file
    db_file = 'db.sqlite3'
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"✅ Deleted {db_file}")
    
    # Run migrations to create fresh database
    execute_from_command_line(['manage.py', 'migrate'])
    print("✅ Created fresh database with migrations")
    
    print("🎯 Database is now empty and ready for live demo!")
    print("🚀 Start your server: python manage.py runserver")

if __name__ == '__main__':
    reset_database()
