import json

with open('gsoc2018-projects-all.json', 'rb') as f:
    all_projects = json.load(f)

student_names = [row['student']['display_name'] for row in all_projects]

student_names = sorted(student_names)

for name in student_names: print(name)
