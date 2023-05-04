def converter(number):
    abbr_dict = {'k':10**3,'M':10**6,'B':10**9}
    try:
        num = int(number[-1])
        return number
    except:  
        abr = number[-1]
        if abr not in abbr_dict.keys():
            raise Exception("Invalid abr")
        ## Everything in number string except the last letter * multiplier
        return float(number[:-1])*abbr_dict[abr]