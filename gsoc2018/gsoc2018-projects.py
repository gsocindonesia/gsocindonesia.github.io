# curl "https://summerofcode.withgoogle.com/api/program/current/project/?page=1&page_size=200" --compressed -H "accept: application/json" -o gsoc2018-projects-1.json
# curl "https://summerofcode.withgoogle.com/api/program/current/project/?page=2&page_size=200" --compressed -H "accept: application/json" -o gsoc2018-projects-2.json
# curl "https://summerofcode.withgoogle.com/api/program/current/project/?page=3&page_size=200" --compressed -H "accept: application/json" -o gsoc2018-projects-3.json
# curl "https://summerofcode.withgoogle.com/api/program/current/project/?page=4&page_size=200" --compressed -H "accept: application/json" -o gsoc2018-projects-4.json
# curl "https://summerofcode.withgoogle.com/api/program/current/project/?page=5&page_size=200" --compressed -H "accept: application/json" -o gsoc2018-projects-5.json
# curl "https://summerofcode.withgoogle.com/api/program/current/project/?page=6&page_size=200" --compressed -H "accept: application/json" -o gsoc2018-projects-6.json
# curl "https://summerofcode.withgoogle.com/api/program/current/project/?page=7&page_size=200" --compressed -H "accept: application/json" -o gsoc2018-projects-7.json

import json

all_projects = []
for i in range(1, 8):
    fn = 'gsoc2018-projects-%d.json' % i
    print('Reading %s ...' % fn)
    with open(fn, 'rb') as f:
        data = json.load(f)
        all_projects.extend(data['results'])

print('Projects: %d' % len(all_projects))

fn_out = 'gsoc2018-projects-all.json'
print('Writing %s' % fn_out)
with open(fn_out, 'w') as f:
    json.dump(all_projects, f, indent=1)
