import datetime
# Parents must be at least 14 years old when married
def us10_marriage_after_14(ind, family):
    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"] != "NA"):
            husID = family[key]["HUSB"][0]
            wifeID = family[key]["WIFE"][0]
            # argument sequence: date of marriage, husband date of birth, wife date of birth
            isChildMarriage = us10_tsk01_is_child_marriage(family[key]["MARR_DATE"][0], ind[husID]["BIRT_DATE"][0], ind[wifeID]["BIRT_DATE"][0])
            if(isChildMarriage == False):
                print('Anomaly US10 in line', family[key]["MARR_DATE"][1],': Marriage of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,') occurs before both parents are 14 years old.')
# dom: date of marriage, DOB: date of birth
def us10_tsk01_is_child_marriage(domString, husDOBString, wifeDOBString):
    try:
        dom = datetime.datetime.strptime(domString, '%Y-%m-%d')
        husDOB = datetime.datetime.strptime(husDOBString, '%Y-%m-%d')
        wifeDOB = datetime.datetime.strptime(wifeDOBString, '%Y-%m-%d')
        # age to be refined
        husAgeByDOM = int((dom-husDOB).days/365)
        wifeAgeByDOM = int((dom-wifeDOB).days/365)
        # if age is negative, it may be related to US 02 and it is considered True
        if(husAgeByDOM < 0 or wifeAgeByDOM < 0):
            return True
        elif(husAgeByDOM < 14 or wifeAgeByDOM < 14):
            return False
        else:
            return True
    except ValueError:
        #if any input date is NA or invalid, it is considered as true
        return True