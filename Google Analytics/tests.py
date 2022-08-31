import os
from ga4 import GA4RealTimeReport
from ga4 import run_report_with_multiple_metrics


def check():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'koders-358507-92048c21110b.json'

    property_id = '326137555'

    testing=run_report_with_multiple_metrics()
    ans=[]


    n=len(testing[0])
    for i in range(n):
        s=""
        count=0
        for itr in testing[1][i]:
            if count==4 or count==6:
                s=s+"/"
            s=s+itr
            count=count+1
        # print(s)
        ans.append({
            'date': s,
            'users': testing[0][i]
        })

    # ans.append(testing[0])
    # ans.append(testing[1])
    # print(testing)
    lst_dimension = ['country', 'deviceCategory', 'minutesAgo', 'countryId']
    lst_metrics = ['activeUsers', 'screenPageViews']
    ga4_realtime = GA4RealTimeReport(property_id)
    response = ga4_realtime.query_report(
        lst_dimension, lst_metrics, 30, True
    )

    # print(response)

    x = response.get("rows")

    count=[]
    Res = []
    countDesktop = 0
    countMobile = 0
    for row in x:
        if row[1] == "desktop":
            countDesktop = countDesktop + 1
        elif row[1] == "mobile":
            countMobile = countMobile + 1

        Res.append({
            'country': row[0],
            'device': row[1],
            'minutesAgo': row[2],
            'countryid': row[3],
            'activeUsers': row[4],
            'screenPageViews': row[5]
        })
    count.append({'mobile': countMobile,'desktop': countDesktop})
    return {
        'val': Res,
        'count': count,
        'result':ans
    }
    # return Res
