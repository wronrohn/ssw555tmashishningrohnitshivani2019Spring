import datetime

class us_sp:

    # User Story #02
    """
    Birth should occur before marriage of an individual
    """
    def us02_birth_before_marriage(self,ind, family):
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
                                print("In us 02",ind[key]["BIRT_DATE"])
                                isvalid = self.us02_birth_is_before_marriage(ind[key]["BIRT_DATE"][0],family[key1]["MARR_DATE"][0])
                                if (isvalid == False):
                                    print('Error US02: Birth date of', ind[key]["NAME"], '(', key ,') occurs after the marriage date.')
                                break

        

    def us02_birth_is_before_marriage(self,birth_date,marriage_date):
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

    # User Story #35
    """
    List all people in a GEDCOM file who were born in the last 30 days
    """
    def us35_ppl_born_last_30days(self,ind):
        last_30days_born_list =[]
        for key, values in ind.items():
            if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"] != "NA"):
                present_date = datetime.datetime.now()
                status = self.us35_ppl_born_last_30days_check(ind[key]["BIRT_DATE"][0],present_date)
                if status == True:
                    new_record = key+str(values)
                    print(new_record)
                    #    print(type(values))
                    last_30days_born_list.append(new_record)
        for records in last_30days_born_list:
            print("List of individuals born in the last 30days:  ")
            print(records)
        


    def us35_ppl_born_last_30days_check(self,birth_date,present_date):
        if(birth_date == "NA" or present_date =="NA"):
            return False
        else:
            birth_date = datetime.datetime.strptime(str(birth_date), '%Y-%m-%d')

            if present_date + datetime.timedelta(-30) < birth_date and  birth_date < present_date:
                return True 
            else:
                return False

