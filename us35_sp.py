
def us35_ppl_born_last_30days(ind, family):
    last_30days_born_list =[]
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"] != "NA"):
           status = us35_ppl_born_last_30days_check(ind[key]["BIRT_DATE"])
           if status == True:
               new_record = key+str(values)
               print(new_record)
            #    print(type(values))
               last_30days_born_list.append(new_record)
    for records in last_30days_born_list:
        print("List of individuals born in the last 30days:  ")
        print(records)


def us35_ppl_born_last_30days_check(birth_date):
    birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
    present_date = datetime.datetime.now()

    if present_date + datetime.timedelta(-30) < birth_date and  birth_date < present_date:
        return True 
    else:
        return False