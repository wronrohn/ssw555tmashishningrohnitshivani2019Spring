import datetime

def us34_list_big_age_diff(ind, family):
    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"] != "NA"):
            husID = family[key]["HUSB"][0]
            wifeID = family[key]["WIFE"][0]
            # argument sequence: date of marriage, husband date of birth, wife date of birth
            isBigGap = us34_tsk01_is_big_age_gap(family[key]["MARR_DATE"][0], ind[husID]["BIRT_DATE"][0], ind[wifeID]["BIRT_DATE"][0])
            if(isBigGap):
                msgSuffix = 'occurs when older spouse is more than twice as old as younger one.'
                print('Anomaly US34 in line', family[key]["MARR_DATE"][1],': Marriage of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,')', msgSuffix)

def us34_tsk01_is_big_age_gap(domString, husDOBString, wifeDOBString):
    try:
        dom = datetime.datetime.strptime(domString, '%Y-%m-%d')
        husDOB = datetime.datetime.strptime(husDOBString, '%Y-%m-%d')
        wifeDOB = datetime.datetime.strptime(wifeDOBString, '%Y-%m-%d')
        # age to be refined
        husAgeByDOM = int((dom-husDOB).days/365)
        wifeAgeByDOM = int((dom-wifeDOB).days/365)
        # if age is negative, it may be related to US 02 and it is considered False
        if(husAgeByDOM < 0 or wifeAgeByDOM < 0):
            return False
        elif(husAgeByDOM > (wifeAgeByDOM * 2) or wifeAgeByDOM > (husAgeByDOM * 2)):
            return True
        else:
            return False
    except ValueError:
        #if any input date is NA or invalid, it is considered as false
        return False