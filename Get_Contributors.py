import json, requests
all_contributors = list()
page_count = 1
while True:
    contributors = requests.get("https://api.github.com/repos/sriankursri/test-repo/contributors?page=%d"%page_count)
    if contributors != None and contributors.status_code == 200 and len(contributors.json()) > 0:
        all_contributors = all_contributors + contributors.json()
    else:
        break
    page_count = page_count + 1
count=len(all_contributors)
print("-------------------%d" %count)
for contributor in all_contributors:
    print str(contributor['login'])