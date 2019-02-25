import datetime

def us42_tsk01_is_legit_date(dateString):
    try:
        dateSubject = datetime.datetime.strptime(dateString,'%d %b %Y')
        return True
    except ValueError:
        return False

def us42_legit_date(ind, family):
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"][0] == "Invalid"):
            print('Error US42 in line',ind[key]["BIRT_DATE"][1],': Birth date of', ind[key]["NAME"], '(', key ,') is illegitimate.')
        if (values.__contains__("DEAT_DATE") and ind[key]["DEAT_DATE"][0] == "Invalid"):
            print('Error US42 in line',ind[key]["DEAT_DATE"][1],': Death date of', ind[key]["NAME"], '(', key ,') is illegitimate.')

    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"][0] == "Invalid"):
            husID = family[key]["HUSB"][0]
            wifeID = family[key]["WIFE"][0]
            print('Error US42 in line',family[key]["MARR_DATE"][1],': Marriage date of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,') is illegitimate.')
        if (values.__contains__("DIV_DATE") and family[key]["DIV_DATE"][0] == "Invalid"):
            husID = family[key]["HUSB"][0]
            wifeID = family[key]["WIFE"][0]
            print('Error US42 in line', family[key]["DIV_DATE"][1],': Divorce date of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,') is illegitimate.')
