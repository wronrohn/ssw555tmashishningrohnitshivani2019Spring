import datetime


def us02_birth_before_marriage(ind, family):
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"] != "NA"):
            if (values.__contains__("FAMS") and ind[key]["FAMS"] != "NA"):
                # print("Family spouse   ",ind[key]["FAMS"])
                # print(type(ind[key]["FAMS"]))
                fam_list = ind[key]["FAMS"]
                # print(fam_list)
                for family_id in fam_list:
                    # print("family_id   ",family_id)
                    for key1, values1 in family.items():
                        # print("values:   ",values1)
                        if (key1 == family_id and values1.__contains__("MARR_DATE") and family[key1]["MARR_DATE"] != "NA"):
                            # print(family[key1]["MARR_DATE"])
                            isvalid = us02_birth_is_before_marriage(ind[key]["BIRT_DATE"],family[key1]["MARR_DATE"])
                            if (isvalid == False):
                                print('Error US02: Birth date of', ind[key]["NAME"], '(', key ,') occurs after the marriage date.')
                            break

       
def us02_birth_is_before_marriage(birth_date,marriage_date):
    if(birth_date == "NA" or marriage_date == "NA"):
        return True
    else:
        birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
        marriage_date = datetime.datetime.strptime(marriage_date, '%Y-%m-%d')

        # print("===================")
        # print(subjectDate)
        if(birth_date < marriage_date):
            return True
        else:
            return False

