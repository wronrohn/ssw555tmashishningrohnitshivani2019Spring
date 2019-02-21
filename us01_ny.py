import datetime

def us01_date_b4_now(ind, family):
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"] != "NA"):
            isB4Now = us01_tsk01_is_b4_now(ind[key]["BIRT_DATE"])
            if (isB4Now == False):
                print('Error US01: Birth date of', ind[key]["NAME"], '(', key ,') occurs after current date.')
        if (values.__contains__("DEAT_DATE") and ind[key]["DEAT_DATE"] != "NA"):
            isB4Now = us01_tsk01_is_b4_now(ind[key]["DEAT_DATE"])
            if (isB4Now == False):
                print('Error US01: Death date of', ind[key]["NAME"], '(', key ,') occurs after current date.')

    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"] != "NA"):
            isB4Now = us01_tsk01_is_b4_now(family[key]["MARR_DATE"])
            if (isB4Now == False):
                husID = family[key]["HUSB"]
                wifeID = family[key]["WIFE"]
                print('Error US01: Marriage date of ', ind[husID]["NAME"],'(', husID, ') and', ind[wifeID]["NAME"],'(', wifeID,') in Family (', key,') occurs after current date.')
        if (values.__contains__("DIV_DATE") and family[key]["DIV_DATE"] != "NA"):
            isB4Now = us01_tsk01_is_b4_now(family[key]["DIV_DATE"])
            if (isB4Now == False):
                husID = family[key]["HUSB"]
                wifeID = family[key]["WIFE"]
                print('Error US01: Divorce date of ', ind[husID]["NAME"],'(', husID, ') and', ind[wifeID]["NAME"],'(', wifeID,') in Family (', key,') occurs after current date.')

def us01_tsk01_is_b4_now(dateString):
    try:
        nowDate = datetime.datetime.now()
        subjectDate = datetime.datetime.strptime(dateString, '%Y-%m-%d')
        if(subjectDate < nowDate):
            return True
        else:
            return False
    except ValueError:
        #if input date is NA or invalid, it is considered as true
        return True

