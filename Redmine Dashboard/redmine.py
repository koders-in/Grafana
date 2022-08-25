import datetime
import time
import os
from sys import exit
from prometheus_client import start_http_server, Summary
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from redminelib import Redmine
from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup

load_dotenv()

COLLECTION_TIME = Summary('redmine_collector_collect_seconds', 'Time spent to collect metrics from Redmine')
final_ids = []


class RedmineCollector(object):
    apimetrics = ["redmine_project_open_issues_total_count", "redmine_project_closed_issues_total_count",
                  "redmine_project_resolved_issues_total_count", "redmine_project_onhold_issues_total_count",
                  "redmine_project_inprogress_issues_total_count", "redmine_project_feedback_issues_total_count",
                  "redmine_project_activeusers_count", "redmine_project_issue_due_date",
                  "redmine_project_open_issues_color_total_count",
                  "redmine_project_open_meeting_total_count","redmine_project_issue_spenttime_last_week_hours"
                  ]

    def __init__(self, target, api):
        self._target = target.rstrip("/")
        self.api = api

    def collect(self):
        start = time.time()
        self._setup_empty_prometheus_metrics()
        # Request data from Redmine
        jobs = self._request_data()

        for status in self.apimetrics:
            for metric in self._prometheus_metrics.values():
                yield metric

        duration = time.time() - start

        COLLECTION_TIME.observe(duration)

    def _request_data(self):
        # Request exactly the information we need from Redmine
        redmine = Redmine(self._target, key=self.api)

        # Watchers field infromation




        for project in redmine.project.all():

            count = len(redmine.issue.filter(tracker_id=4))

            for issue in redmine.issue.filter(tracker_id=4):

                if (issue.tracker.name == 'meeting'):
                    watching = []
                    for watcher in issue.watchers:
                        watching.append(str(watcher))

                    ids = issue.id

                    # Date and Time field infromation used BeautifulSoup for web scraping

                    api_endpoint = os.getenv('URL')+"issues/" + str(ids)
                    CAT_API_KEY = os.getenv('API')

                    headers = {
                        "X-Redmine-API-Key": CAT_API_KEY
                    }
                    response = requests.get(
                        api_endpoint,
                        headers=headers
                    )

                    htmlContent = response.content

                    soup = BeautifulSoup(htmlContent, 'html.parser')

                    list1 = soup.find('div', class_="attributes")

                    list2 = list1.find('div', class_="meeting-date attribute")
                    list3 = list2.find('div', class_="value").text

                    s = str(list3)
                    s1 = s.replace("\n", " ")
                    s2 = s1.strip()
                    s3 = s2.replace("     ", "")
                    check = 0
                    ans = ""
                    for itr in s3:
                        if (itr == ' '):
                            check = 1
                        if (check == 1):
                            ans += itr
                    final_date = ""
                    for itr2 in s3:
                        if (itr2 == ' '):
                            break
                        final_date += itr2
                    # Meeting issue for today and upcoming meeting
                    today_date = str(datetime.datetime.now().date())
                    today_date1 = today_date.replace("-", "/")

                    year = ""
                    month = ""
                    day = ""
                    year_count = 4
                    month_count = 7
                    count = 0
                    for itr in today_date1:
                        if count < year_count:
                            year += itr
                        if count > year_count and count < month_count:
                            month += itr
                        if count > month_count:
                            day += itr
                        count = count + 1

                    today_date_final = month + "/" + day + "/" + year
                    final_time = ans.replace(" ", "")
                    if today_date_final <= final_date:
                        self._prometheus_metrics['meeting'].add_metric(
                            [issue.status.name, str(watching), str(issue.subject), final_time, final_date], count)

            _date = datetime.datetime.now().date()
            _datetimestamp = time.mktime(_date.timetuple())
            self._prometheus_metrics['todaydate'].add_metric([_date.strftime("%m/%d/%Y")], _datetimestamp)

            user = len(redmine.user.all())
            self._prometheus_metrics['activeusers'].add_metric(['activeusers'], user)

            count = len(redmine.issue.filter(status_id='open', project_id=project.id))
            self._prometheus_metrics['openissues'].add_metric([project.name], count)
            color = 'green'

            if count < user * 2:
                color = 'green'
            elif count >= user * 2 and count < user * 3:
                color = 'yellow'
            elif count >= user * 3:
                color = 'red'
            for issue in redmine.issue.all(itr=count):
                self._prometheus_metrics['issuecolor'].add_metric([issue.project.name, color], count)
                break
            count = len(redmine.issue.filter(status_id=3, project_id=project.id))
            self._prometheus_metrics['resolvedissues'].add_metric([project.name], count)
            count = len(redmine.issue.filter(status_id='closed', project_id=project.id))
            self._prometheus_metrics['closedissues'].add_metric([project.name], count)
            count = len(redmine.issue.filter(status_id=10, project_id=project.id))
            self._prometheus_metrics['onholdissues'].add_metric([project.name], count)
            count = len(redmine.issue.filter(status_id=2, project_id=project.id))
            self._prometheus_metrics['inprogressissues'].add_metric([project.name], count)
            count = len(redmine.issue.filter(status_id=4, project_id=project.id))
            self._prometheus_metrics['feedbackissues'].add_metric([project.name], count)

            for issue in redmine.issue.all(due_date=_date):
                self._prometheus_metrics['duedate'].add_metric(
                    [issue.project.name, str(issue.id), issue.status.name, issue.tracker.name, issue.priority.name,
                    _date.strftime('%d/%m/%Y'), issue.author.name, issue.assigned_to.name], _datetimestamp)
            # spent time start
            week = []
            for i in range(0, 7):
                week.append(((datetime.datetime.now() - datetime.timedelta(days=i)).date()))

            mp = {}
            for day in week:
                time_entries = redmine.time_entry.filter(spent_on=day)

                users_name=[]

                for entries in time_entries:
                    if entries.user.name not in users_name:
                        users_name.append(entries.user.name)
                users_name_length=len(users_name)

                for entries in time_entries:

                    if entries.user.name in mp:
                        mp[entries.user.name] += entries.hours

                    else:
                        mp[entries.user.name]=entries.hours

            for itr in mp:
                self._prometheus_metrics['spent7days'].add_metric([itr], str(mp[itr]))

            # spent time end

    def _setup_empty_prometheus_metrics(self):
        # The metrics we want to export.
        self._prometheus_metrics = {}

        # snake_case = re.sub('([A-Z])', '_\\1', status).lower()
        self._prometheus_metrics['activeusers'] = GaugeMetricFamily('active_users',
                                                                    'Shows total active users',
                                                                    labels=["users"])

        self._prometheus_metrics['todaydate'] = GaugeMetricFamily('redmine_today_date',
                                                                  'Shows todays date',
                                                                  labels=["date"])
        self._prometheus_metrics['openissues'] = GaugeMetricFamily('redmine_project_open_issues_total_count',
                                                                   'Redmine Project Open Issues Count',
                                                                   labels=["projectname"])
        self._prometheus_metrics['resolvedissues'] = GaugeMetricFamily('redmine_project_resolved_issues_total_count',
                                                                       'Redmine Project Resolved Issues Count',
                                                                       labels=["projectname"])
        self._prometheus_metrics['onholdissues'] = GaugeMetricFamily('redmine_project_onhold_issues_total_count',
                                                                     'Redmine Project On hold Issues Count',
                                                                     labels=["projectname"])
        self._prometheus_metrics['feedbackissues'] = GaugeMetricFamily('redmine_project_feedback_issues_total_count',
                                                                       'Redmine Project Feedback Issues Count',
                                                                       labels=["projectname"])
        self._prometheus_metrics['inprogressissues'] = GaugeMetricFamily(
            'redmine_project_inprogress_issues_total_count',
            'Redmine Project In-Progress Issues Count',
            labels=["projectname"])
        self._prometheus_metrics['closedissues'] = GaugeMetricFamily('redmine_project_closed_issues_total_count',
                                                                     'Redmine Project Closed Issues Count',
                                                                     labels=["projectname"])
        self._prometheus_metrics['duedate'] = GaugeMetricFamily('redmine_project_issue_due_date',
                                                                'Redmine Due by Today',
                                                                labels=["projectname", "issueid", "status", "tracker",
                                                                        "priority", "duedate", "author", "user"])

        self._prometheus_metrics['issuecolor'] = GaugeMetricFamily('redmine_project_open_issues_color_total_count',
                                                                   'Redmine Project Open Issues Count color',
                                                                   labels=["projectname", "color"])
        self._prometheus_metrics['meeting'] = GaugeMetricFamily('redmine_project_open_meeting_total_count',
                                                                'Redmine Project Open meeting count',
                                                                labels=["status", "watchers", "subject", "time",
                                                                        "date"])
        self._prometheus_metrics['spent7days'] = GaugeMetricFamily('redmine_project_issue_spenttime_last_week_hours',
                                                                   'Redmine Project SpentTime Duration Hours Of Last Week',
                                                                   labels=["user"])


def main():
    try:
        redmine = os.getenv('URL')
        api = os.getenv('API')
        port = int(os.getenv('PORT'))
        REGISTRY.register(RedmineCollector(redmine, api))
        start_http_server(port)
        print("Polling {}. Serving at port: {}".format(redmine, port))
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(" Interrupted")
        exit(0)


if __name__ == "__main__":
    main()
