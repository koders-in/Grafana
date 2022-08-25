import json
from github import Github
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GRAFANA_API = os.getenv('GRAFANA_API')

ORG_NAME = "koders-in"
dataSource = "grafana-github-datasource"
uid = "zhq35I1nz"
owner = "koders-in"
headers = {
  'Authorization': GRAFANA_API,
  'Content-Type': 'application/json'
}
server = "https://grafana.koders.in"


def generate():
    for i in range(65, 91):
        for j in range(65, 91):
            for k in range(65, 91):
                yield chr(i) + chr(j) + chr(k)


def create_commit_panel():
    ref_ids = list(generate())
    g = Github(GITHUB_TOKEN)
    org = g.get_organization(ORG_NAME)
    repos = org.get_repos()
    counter = 0
    open('commits.json', 'w').close()
    open('total_pull.json', 'w').close()
    open('active_pull.json', 'w').close()
    open('total_issues.json', 'w').close()
    open('active_issues.json', 'w').close()
    open('contributors.json', 'w').close()

    for repo in repos:
        total_issues_dict = {
            "datasource": {
                "type": dataSource,
                "uid": uid
            },
            "hide": False,
            "options": {
                "query": "",
            },
            "owner": "koders-in",
            "queryType": "Issues",
            "refId": ref_ids[counter],
            "repository": repo.name
        }

        temp_dict = json.dumps(total_issues_dict, indent=4)
        print(temp_dict)
        try:
            with open('total_issues.json', 'r') as fin:
                try:
                    data = json.load(fin)
                except json.decoder.JSONDecodeError:
                    data = []
        except FileNotFoundError as exc:
            pass
        data.append(total_issues_dict)
        with open('total_issues.json', 'w') as fout:
            json.dump(data, fout)
        # except UnboundLocalError as exc:
        #     with open('commits.json', 'w') as fout:
        #         json.dump(data, fout

        active_issues_dict = {
            "datasource": {
                "type": dataSource,
                "uid": uid
            },
            "hide": False,
            "options": {
                "query": "is:open",
            },
            "owner": "koders-in",
            "queryType": "Issues",
            "refId": ref_ids[counter],
            "repository": repo.name
        }

        temp_dict = json.dumps(active_issues_dict, indent=4)
        print(temp_dict)
        try:
            with open('active_issues.json', 'r') as fin:
                try:
                    data = json.load(fin)
                except json.decoder.JSONDecodeError:
                    data = []
        except FileNotFoundError as exc:
            pass
        data.append(active_issues_dict)
        with open('active_issues.json', 'w') as fout:
            json.dump(data, fout)
        # except UnboundLocalError as exc:
        #     with open('commits.json', 'w') as fout:
        #         json.dump(data, fout

        contributor_dict = {
            "datasource": {
                "type": dataSource,
                "uid": uid
            },
            "hide": False,
            "options": {
                "query": "",
            },
            "owner": "koders-in",
            "queryType": "Contributors",
            "refId": ref_ids[counter],
            "repository": repo.name
        }

        temp_dict = json.dumps(contributor_dict, indent=4)
        print(temp_dict)
        try:
            with open('contributors.json', 'r') as fin:
                try:
                    data = json.load(fin)
                except json.decoder.JSONDecodeError:
                    data = []
        except FileNotFoundError as exc:
            pass
        data.append(contributor_dict)
        with open('contributors.json', 'w') as fout:
            json.dump(data, fout)
        # except UnboundLocalError as exc:
        #     with open('commits.json', 'w') as fout:
        #         json.dump(data, fout



        total_pull_request_dict = {
                "datasource": {
                    "type": dataSource,
                    "uid": uid
                },
                "hide": False,
                "options": {
                    "query": "",
                    "timeField": 1
                },
                "owner": "koders-in",
                "queryType": "Pull_Requests",
                "refId": ref_ids[counter],
                "repository": repo.name
                }

        temp_dict = json.dumps(total_pull_request_dict, indent=4)
        print(temp_dict)
        try:
            with open('total_pull.json', 'r') as fin:
                try:
                    data = json.load(fin)
                except json.decoder.JSONDecodeError:
                    data = []
        except FileNotFoundError as exc:
            pass
        data.append(total_pull_request_dict)
        with open('total_pull.json', 'w') as fout:
            json.dump(data, fout)
        # except UnboundLocalError as exc:
        #     with open('commits.json', 'w') as fout:
        #         json.dump(data, fout)


        active_pull_request_dict = {
            "datasource": {
                "type": dataSource,
                "uid": uid
            },
            "hide": False,
            "options": {
                "query": "is:open",
                "timeField": 3
            },
            "owner": "koders-in",
            "queryType": "Pull_Requests",
            "refId": ref_ids[counter],
            "repository": repo.name
        }

        temp_dict = json.dumps(active_pull_request_dict, indent=4)
        print(temp_dict)
        try:
            with open('active_pull.json', 'r') as fin:
                try:
                    data = json.load(fin)
                except json.decoder.JSONDecodeError:
                    data = []
        except FileNotFoundError as exc:
            pass
        data.append(active_pull_request_dict)
        with open('active_pull.json', 'w') as fout:
            json.dump(data, fout)
        # except UnboundLocalError as exc:
        #     with open('commits.json', 'w') as fout:
        #         json.dump(data, fout)


        for branch in repo.get_branches():
            counter = counter + 1
            commit_dict = {
                "refID": ref_ids[counter],
                "datssource": {
                    "type:": dataSource,
                    "uid": uid
                },
                "queryType": "Commits",
                "repository": repo.name,
                "owner": "koders-in",
                "options": {
                    "gitRef": branch.name
                },
                "hide": False
            }
            temp_dict = json.dumps(commit_dict, indent=4)
            print(temp_dict)
            try:
                with open('commits.json', 'r') as fin:
                    try:
                        data = json.load(fin)
                    except json.decoder.JSONDecodeError:
                        data = []
            except FileNotFoundError as exc:
                pass
            data.append(commit_dict)
            with open('commits.json', 'w') as fout:
                json.dump(data, fout)
            # except UnboundLocalError as exc:
            #     with open('commits.json', 'w') as fout:
            #         json.dump(data, fout)


def get_panel_uid():
    uid = "iVcSTeyGzk"
    url = server + "/api/dashboards/uid/" + uid
    r = requests.get(url=url, headers=headers, verify=False)
    dash_data = r.json()
    panel_uid = dash_data['dashboard']['panels'][1]['targets'][0]['datasource']['uid']
    return panel_uid


def get_dashboard_data(uid):
    url = server + "/api/dashboards/uid/" + uid
    r = requests.get(url=url, headers=headers, verify=False)
    return r.json()


create_commit_panel()
commits = open('commits.json').read()
commits = json.loads(commits)
total_pull = open('total_pull.json').read()
total_pull = json.loads(total_pull)
active_pull = open('active_pull.json').read()
active_pull = json.loads(active_pull)
total_issues = open('total_issues.json').read()
total_issues = json.loads(total_issues)
active_issues = open('active_issues.json').read()
active_issues = json.loads(active_issues)
contributors = open('contributors.json').read()
contributors = json.loads(contributors)

dash_data = get_dashboard_data('iVcSTeyGzk')
dash_data['dashboard']['panels'][0]['targets'] = commits
dash_data['dashboard']['panels'][1]['targets'] = total_issues
dash_data['dashboard']['panels'][2]['targets'] = total_pull
dash_data['dashboard']['panels'][3]['targets'] = total_pull
dash_data['dashboard']['panels'][4]['targets'] = active_pull
dash_data['dashboard']['panels'][6]['targets'] = active_issues
dash_data['dashboard']['panels'][7]['targets'] = active_pull
dash_data['dashboard']['panels'][8]['targets'] = total_pull
dash_data['dashboard']['panels'][9]['targets'] = commits
dash_data['dashboard']['panels'][10]['targets'] = active_issues
dash_data['dashboard']['panels'][11]['targets'] = contributors
print(json.dumps(dash_data['dashboard']['panels']))
new_dashboard = dash_data
new_dashboard = json.dumps(new_dashboard)
print(new_dashboard)
url = server + "/api/dashboards/db"
r = requests.post(url=url, headers=headers, data=new_dashboard, verify=False)
print(r.json())




