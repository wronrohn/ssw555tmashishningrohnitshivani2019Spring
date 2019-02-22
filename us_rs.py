class us_rs:
    # UserStory 15
    def siblingCount(family):
        if(type(family) is not (dict)):
            raise TypeError("Argument isn't an dict")
        validity = True
        for x, values in family.items():
            
            if values.__contains__("CHIL"):
                length = len(values["CHIL"])
            else:
                length = 0
            if length > 15:
                validity = False
                raise ValueError("ERROR: There are more than 15 siblings for family " + x)
            
        return validity

  


