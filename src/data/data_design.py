"""
Data schema and design logic for Career Compass.
"""

def define_schema():
    schema = {
        "job_id": "string",
        "role_title": "string",
        "required_skills": "list[string]",
        "preferred_skills": "list[string]",
        "experience_level": "string",
        "responsibilities": "string",
        "salary_range": "string",
        "location": "string",
        "role_family": "string"
    }
    return schema
