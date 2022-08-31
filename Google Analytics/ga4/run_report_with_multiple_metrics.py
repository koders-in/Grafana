from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest

from run_report import print_run_report_response


def run_sample():
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "326137555"
    run_report_with_multiple_metrics(property_id)


def run_report_with_multiple_metrics(property_id="326137555"):
    """Runs a report of active users, new users and total revenue grouped by
    date dimension."""
    client = BetaAnalyticsDataClient()

    # Runs a report of active users grouped by three dimensions.
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="activeUsers")
        ],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    )
    response = client.run_report(request)
    listDate=[]
    listUsers=[]
    for row in response.rows:
        for dimension_value in row.dimension_values:
            listDate.append(str(dimension_value.value).strip())

        for metric_value in row.metric_values:
            listUsers.append(str(metric_value.value).strip())

    return listUsers,listDate
