import datetime
# User Story #35
"""
List all people in a GEDCOM file who were born in the last 30 days
"""
def us35_ppl_born_last_30days(ind):
    last_30days_born_list =[]
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"] != "NA"):
            present_date = datetime.datetime.now()
            status = us35_ppl_born_last_30days_check(ind[key]["BIRT_DATE"][0],present_date)
            if status == True:
                new_record = key+str(values)
                print(new_record)
                #    print(type(values))
                last_30days_born_list.append(new_record)
    for records in last_30days_born_list:
        print("List of individuals born in the last 30days:  ")
        print(records)
    


def us35_ppl_born_last_30days_check(birth_date,present_date):
    if(birth_date == "NA" or present_date =="NA"):
        return False
    else:
        birth_date = datetime.datetime.strptime(str(birth_date), '%Y-%m-%d')

        if present_date + datetime.timedelta(-30) < birth_date and  birth_date < present_date:
            return True 
        else:
            return False