import datetime

def us42_tsk01_is_legit_date(dateString):
    try:
        dateSubject = datetime.datetime.strptime(dateString,'%d %b %Y')
        return True
    except ValueError:
        return False

def us42_legit_date(ind, family):
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"] == "Invalid"):
            print('Error US42: Birth date of', ind[key]["NAME"], '(', key ,') is illegitimate.')
        if (values.__contains__("DEAT_DATE") and ind[key]["DEAT_DATE"] == "Invalid"):
            print('Error US42: Death date of', ind[key]["NAME"], '(', key ,') is illegitimate.')

    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"] == "Invalid"):
            husID = family[key]["HUSB"]
            wifeID = family[key]["WIFE"]
            print('Error US42: Marriage date of ', ind[husID]["NAME"],'(', husID, ') and', ind[wifeID]["NAME"],'(', wifeID,') in Family (', key,') is illegitimate.')
        if (values.__contains__("DIV_DATE") and family[key]["DIV_DATE"] == "Invalid"):
            husID = family[key]["HUSB"]
            wifeID = family[key]["WIFE"]
            print('Error US42: Divorce date of ', ind[husID]["NAME"],'(', husID, ') and', ind[wifeID]["NAME"],'(', wifeID,') in Family (', key,') is illegitimate.')
