from datetime import date
from dateutil.relativedelta import relativedelta
from main import check


def graph():
    jsonContent = check()
    totalProfit = []

    for i in range(15):
        incomefor24m = 0
        expensefor24m = 0
        for check1, check2 in jsonContent.items():
            last12to24 = date.today() - relativedelta(months=+i + 1)
            for check3 in check2:

                for row1, row2 in check3.items():
                    if str(row1) == "operations":
                        for test1 in row2:
                            # Res = []
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

            totalProfit.append(incomefor24m - expensefor24m)
    finalProfitGraph = []
    finalProfitGraph.append(totalProfit[0])

    for i in range(15):
        if i != 0:
            finalProfitGraph.append(totalProfit[i] - totalProfit[i - 1])
    return finalProfitGraph


# graph()
