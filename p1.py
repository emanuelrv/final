def credit_card_penalty(late_days, credit_card_balance):
    if late_days<15:
        return.05*credit_card_balance
    elif late_days<30 and late_days >=15:
        return .10* credit_card_balance
    elif late_days<60 and late_days >31:
        return .15*credit_card_balance
    else:
        return .2*credit_card_balance

print "penalty1: ", credit_card_penalty(15000,18)
print "penalty2: ", credit_card_penalty(7000,31)
print "penalty3: ", credit_card_penalty(300,70)
print "penalty4: ", credit_card_penalty(1000,3)
