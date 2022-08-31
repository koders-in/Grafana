import datetime
import math
from datetime import date
from dateutil.relativedelta import relativedelta
from graph import graph
import graph
from main import check


def func():
    jsonContent = check()
    incomefor24m = 0
    expensefor24m = 0
    overallProfit = 0
    overallIncome = 0
    overallExpense = 0
    incomeFor18Months = 0
    expenseFor18Months = 0
    incomeFor15Months = 0
    expenseFor15Months = 0
    profitFortwelveMonths = 0
    incomeFortwelveMonths = 0
    expenseFortwelveMonths = 0
    incomeForNineMonths = 0
    expenseForNineMonths = 0
    incomeForSixMonths = 0
    expenseForSixMonths = 0
    profitForthreeMonths = 0
    incomeForthreeMonths = 0
    expenseForthreeMonths = 0
    incomeForoneMonths = 0
    expenseForoneMonths = 0
    monthlymisllaneous = 0
    monthlysalary = 0
    monthlyOfficeDetails = 0
    quartelymisllaneous = 0
    quarterlysalary = 0
    quarterlyOfficeDetails = 0
    yearlymisllaneous = 0
    yearlysalary = 0
    yearlyOfficeDetails = 0
    oneMonthProfitGraph = []

    for check1, check2 in jsonContent.items():

        for check3 in check2:

            lasttwelveMonthsDate = date.today() - relativedelta(months=+12)

            last12to24 = date.today() - relativedelta(months=+24)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:

                        ifIncome = 0
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(
                                    details2[:10]) and str(last12to24) <= str(details2[:10]):
                                ifDateExist = 1

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                incomefor24m = incomefor24m + float(details2)

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                expensefor24m = expensefor24m + float(details2)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:
                        ifIncome = 0

                        for details1, details2 in test1.items():

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifIncome == 1 and str(details1) == "amount":
                                overallIncome = overallIncome + float(details2)

                            elif ifIncome == 0 and str(details1) == "amount":
                                overallExpense = overallExpense + float(details2)

            overallProfit = overallIncome - overallExpense

            last18MonthsDate = date.today() - relativedelta(months=+18)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:
                        ifIncome = 0
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(
                                    details2[:10]) and str(last18MonthsDate) <= str(details2[:10]):
                                ifDateExist = 1

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                incomeFor18Months = incomeFor18Months + float(details2)

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                expenseFor18Months = expenseFor18Months + float(details2)

            last15MonthsDate = date.today() - relativedelta(months=+15)
            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:
                        ifIncome = 0
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(
                                    details2[:10]) and str(last15MonthsDate) <= str(details2[:10]):
                                ifDateExist = 1

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                incomeFor15Months = incomeFor15Months + float(details2)

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                expenseFor15Months = expenseFor15Months + float(details2)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:

                        ifIncome = 0
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lasttwelveMonthsDate):
                                ifDateExist = 1

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                incomeFortwelveMonths = incomeFortwelveMonths + float(details2)

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                expenseFortwelveMonths = expenseFortwelveMonths + float(details2)

            profitFortwelveMonths = incomeFortwelveMonths - expenseFortwelveMonths

            lastNineMonthsDate = date.today() - relativedelta(months=+9)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:

                        ifIncome = 0
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lastNineMonthsDate):
                                ifDateExist = 1

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                incomeForNineMonths = incomeForNineMonths + float(details2)

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                expenseForNineMonths = expenseForNineMonths + float(details2)

            lastSixMonthsDate = date.today() - relativedelta(months=+6)
            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:

                        ifIncome = 0
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lastSixMonthsDate):
                                ifDateExist = 1

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                incomeForSixMonths = incomeForSixMonths + float(details2)

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                expenseForSixMonths = expenseForSixMonths + float(details2)

            lastthreeMonthsDate = date.today() - relativedelta(months=+3)
            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:

                        ifIncome = 0
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lastthreeMonthsDate):
                                ifDateExist = 1

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                incomeForthreeMonths = incomeForthreeMonths + float(details2)

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                expenseForthreeMonths = expenseForthreeMonths + float(details2)

            profitForthreeMonths = incomeForthreeMonths - expenseForthreeMonths

            lastoneMonthsDate = date.today() - relativedelta(months=+1)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:

                        ifIncome = 0
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lastoneMonthsDate):
                                ifDateExist = 1

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                incomeForoneMonths = incomeForoneMonths + float(details2)

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                expenseForoneMonths = expenseForoneMonths + float(details2)

            # for expense pie chart

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lastoneMonthsDate):
                                ifDateExist = 1

                        miss = 0
                        sal = 0
                        office = 0
                        for details1, details2 in test1.items():

                            if ifDateExist == 1 and str(details1) == "category":
                                for category, categoryData in details2.items():

                                    if category == "full_name" and categoryData == "misllaneous":
                                        miss = 1

                                    elif category == "full_name" and categoryData == "salary":
                                        sal = 1
                                    elif category == "full_name" and categoryData == "office maintenance":
                                        office = 1
                        for details1, details2 in test1.items():
                            if miss == 1 and str(details1) == "amount":
                                monthlymisllaneous = monthlymisllaneous + float(details2)

                            elif sal == 1 and str(details1) == "amount":
                                monthlysalary = monthlysalary + float(details2)

                            elif office == 1 and str(details1) == "amount":
                                monthlyOfficeDetails = monthlyOfficeDetails + float(details2)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lastthreeMonthsDate):
                                ifDateExist = 1

                        miss = 0
                        sal = 0
                        office = 0
                        for details1, details2 in test1.items():

                            if ifDateExist == 1 and str(details1) == "category":
                                for category, categoryData in details2.items():

                                    if category == "full_name" and categoryData == "misllaneous":
                                        miss = 1

                                    elif category == "full_name" and categoryData == "salary":
                                        sal = 1
                                    elif category == "full_name" and categoryData == "office maintenance":
                                        office = 1

                        for details1, details2 in test1.items():
                            if miss == 1 and str(details1) == "amount":
                                quartelymisllaneous = quartelymisllaneous + float(details2)

                            elif sal == 1 and str(details1) == "amount":
                                quarterlysalary = quarterlysalary + float(details2)

                            elif office == 1 and str(details1) == "amount":
                                quarterlyOfficeDetails = quarterlyOfficeDetails + float(details2)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:
                        ifDateExist = 0
                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lasttwelveMonthsDate):
                                ifDateExist = 1

                        miss = 0
                        sal = 0
                        office = 0
                        for details1, details2 in test1.items():

                            if ifDateExist == 1 and str(details1) == "category":
                                for category, categoryData in details2.items():

                                    if category == "full_name" and categoryData == "misllaneous":
                                        miss = 1

                                    elif category == "full_name" and categoryData == "salary":
                                        sal = 1

                                    elif category == "full_name" and categoryData == "office maintenance":
                                        office = 1
                        for details1, details2 in test1.items():
                            if miss == 1 and str(details1) == "amount":
                                yearlymisllaneous = yearlymisllaneous + float(details2)

                            elif sal == 1 and str(details1) == "amount":
                                yearlysalary = yearlysalary + float(details2)

                            elif office == 1 and str(details1) == "amount":
                                yearlyOfficeDetails = yearlyOfficeDetails + float(details2)

            for row1, row2 in check3.items():
                if str(row1) == "operations":
                    for test1 in row2:

                        ifIncome = 0
                        ifDateExist = 0
                        issuedDate = ""

                        for details1, details2 in test1.items():
                            if str(details1) == "operation_date" and str(date.today()) >= str(details2[:10]) >= str(
                                    lastoneMonthsDate):
                                ifDateExist = 1
                                issuedDate = str(details2[:10])

                            if str(details1) == "is_income" and details2 == 1:
                                ifIncome = 1

                            elif str(details1) == "is_income" and details2 == 0:
                                ifIncome = 0

                        for details1, details2 in test1.items():
                            if ifDateExist == 1 and ifIncome == 1 and str(details1) == "amount":
                                oneMonthProfitGraph.append(
                                    {
                                        "date": issuedDate,
                                        "value": float(details2),
                                    },
                                )

                            elif ifDateExist == 1 and ifIncome == 0 and str(details1) == "amount":
                                oneMonthProfitGraph.append(
                                    {
                                        "date": issuedDate,
                                        "value": 0 - float(details2),
                                    },
                                )
    oneMonthProfitGraph.reverse()
    # runway
    totalMoney = incomeFortwelveMonths - expenseFortwelveMonths
    avgExpense = expenseFortwelveMonths / 12
    runway = math.floor(totalMoney / avgExpense)
    spendingCapabilitesmonthly = 0.2 * (incomeForoneMonths - expenseForoneMonths)
    spendingCapabilitesquarterly = 0.2 * (incomeForthreeMonths - expenseForthreeMonths)
    spendingCapabilitesyearly = 0.2 * (incomeFortwelveMonths - expenseFortwelveMonths)

    totalBalance1to3 = incomeForthreeMonths - expenseForthreeMonths
    totalBalance3to6 = (incomeForSixMonths - expenseForSixMonths) - (incomeForthreeMonths - expenseForthreeMonths)
    totalBalance6to9 = (incomeForNineMonths - expenseForNineMonths) - (incomeForSixMonths - expenseForSixMonths)
    totalBalance9to12 = (incomeFortwelveMonths - expenseFortwelveMonths) - (incomeForNineMonths - expenseForNineMonths)
    totalBalance12to15 = (incomeFor15Months - expenseFor15Months) - (incomeFortwelveMonths - expenseFortwelveMonths)
    totalBalance18to15 = (incomeFor18Months - expenseFor18Months) - (incomeFor15Months - expenseFor15Months)
    presentFor18to15 = totalBalance18to15
    present15to12 = totalBalance12to15
    present12to9 = totalBalance9to12
    present9to6 = totalBalance6to9
    present6to3 = totalBalance3to6
    present3to1 = totalBalance1to3

    growthGraph = []
    try:
        growthFrom15to12 = ((present15to12 - presentFor18to15) / math.fabs(presentFor18to15)) * 100
        growthFrom12to9 = ((present12to9 - present15to12) / math.fabs(present15to12)) * 100
        growthFrom9to6 = ((present9to6 - present12to9) / math.fabs(present12to9)) * 100
        growthFrom6to3 = ((present6to3 - present9to6) / math.fabs(present9to6)) * 100
        growthFrom3to1 = ((present3to1 - present6to3) / math.fabs(present6to3)) * 100

        growthGraph.append({
            '15to12': growthFrom15to12,
            '12to9': growthFrom12to9,
            '9to6': growthFrom9to6,
            '6to3': growthFrom6to3,
            '3to0': growthFrom3to1,
        })
    except:
        print("divided by 0")

    profitGraphFunc = graph.graph()

    x = 0
    yearProfitList = []

    for i in range(12):
        yearProfitList.append(
            {
                "date": str(datetime.datetime.now() - relativedelta(months=+i))[:19],
                "value": profitGraphFunc[i]
            },
        )
        x = x + 1

    yearProfitList.reverse()

    x = 0
    yearGrowthList = []
    for i in range(13):
        if i != 0:
            yearGrowthList.append(
                {
                    "date": str(datetime.datetime.now() - relativedelta(months=+x - 1))[:19],
                    "value": ((profitGraphFunc[i - 1] - profitGraphFunc[i]) / math.fabs(profitGraphFunc[i])) * 100,
                },
            )
        x = x + 1
    yearGrowthList.reverse()

    #

    x = 0
    quarterProfitList = []

    for i in range(3):
        quarterProfitList.append(
            {
                "date": str(datetime.datetime.now() - relativedelta(months=+i))[:19],
                "value": profitGraphFunc[i]
            },
        )
        x = x + 1

    quarterProfitList.reverse()

    x = 0
    quarterGrowthList = []
    for i in range(4):
        if i != 0:
            quarterGrowthList.append(
                {
                    "date": str(datetime.datetime.now() - relativedelta(months=+x - 1))[:19],
                    "value": ((profitGraphFunc[i - 1] - profitGraphFunc[i]) / math.fabs(profitGraphFunc[i])) * 100,
                },
            )
        x = x + 1
    quarterGrowthList.reverse()
    colorMonthly = "red"
    if expenseForoneMonths <= spendingCapabilitesmonthly:
        colorMonthly = "green"
    elif expenseForoneMonths < 1.5 * spendingCapabilitesmonthly:
        colorMonthly = "yellow"

    colorQuarterly = "red"
    if expenseForthreeMonths <= spendingCapabilitesquarterly:
        colorQuarterly = "green"
    elif expenseForthreeMonths < 1.5 * spendingCapabilitesquarterly:
        colorQuarterly = "yellow"

    colorYearly = "red"
    if expenseFortwelveMonths <= spendingCapabilitesyearly:
        colorYearly = "green"
    elif expenseFortwelveMonths < 1.5 * spendingCapabilitesyearly:
        colorYearly = "yellow"
    print(profitGraphFunc[0])
    return {
        'expenseMonthly': {

            'monthlyProfit': expenseForoneMonths,
            'colorMonthly': colorMonthly
        },

        'expenseQuarterly': {

            'quarterlyProfit': expenseForthreeMonths,
            'colorQuarterly': colorQuarterly
        },

        'expenseYear': {

            'yearProfit': expenseFortwelveMonths,
            'colorYear': colorYearly
        },

        'quarter':
            {
                'quaterProfit': expenseForthreeMonths,
                'colorQuarterly': colorQuarterly
            },
        'yearly':
            {
                'yearlyProfit': expenseFortwelveMonths,
                'colorYearly': colorYearly
            },

        'total': {
            'totalIncomeForLastYear': incomeFortwelveMonths,
            'totalExpenseForLastYear': expenseFortwelveMonths,
            'totalIncomeForLastQuarter': incomeForthreeMonths,
            'totalExpenseForLastQuarter': expenseForthreeMonths,
            'totalIncomeForLastMonth': incomeForoneMonths,
            'totalExpenseForLastMonth': expenseForoneMonths
        },
        'Profit': {
            'monthlyProfit': incomeForoneMonths - expenseForoneMonths,
            'quarterlyProfit': profitForthreeMonths,
            'yearlyProfit': profitFortwelveMonths,
            'overallProfit': overallProfit,
        },

        'runway': {'runway': runway},
        'SpendingCapability': {
            'spendingCapabilitesMonthly': spendingCapabilitesmonthly,
            'spendingCapabilitesQuarterly': spendingCapabilitesquarterly,
            'spendingCapabilitesYearly': spendingCapabilitesyearly
        },

        'monthpie': {
            'monthlymisllaneous': monthlymisllaneous,
            'monthlysalary': monthlysalary,
            'monthlyOffice': monthlyOfficeDetails
        },
        'quaterpie': {
            'quartelymisllaneous': quartelymisllaneous,
            'quarterlysalary': quarterlysalary,
            'quarterlyOffice': quarterlyOfficeDetails
        },
        'yearpie': {
            'yearlymisllaneous': yearlymisllaneous,
            'yearlysalary': yearlysalary,
            'yearlyOffice': yearlyOfficeDetails
        },

        'profitGraph': yearProfitList,
        'newGrowthGraph': yearGrowthList,
        'oneMonthProfitGraph': oneMonthProfitGraph,
        'profitGraphForQuarter': quarterProfitList,
        'growthGraphForQuarter': quarterGrowthList,

        'lastMonthProfitPercent': {
            'lastMonthProfitPercent': ((profitGraphFunc[0] - profitGraphFunc[1]) / math.fabs(profitGraphFunc[1])) * 100,
        },

    }

# func()
