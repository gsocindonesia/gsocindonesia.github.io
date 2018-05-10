import json
from collections import OrderedDict

with open('gsoc2018-projects-all.json', 'rb') as f:
    all_projects = json.load(f)

org_counts = {}

for project in all_projects:
    orgname = project['organization']['name']
    if not orgname in org_counts:
        org_counts[orgname] = 0
    org_counts[orgname] = org_counts[orgname] + 1

org_counts = OrderedDict(sorted(org_counts.items(), key=lambda x: -x[1]))
print(json.dumps(org_counts, indent=1))
