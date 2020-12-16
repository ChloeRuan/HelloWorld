# condition and logical  operator, multiple conditions
# if both conditions are satisfied, then eligible for loan
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

# logical "or"
has_high_income = True
has_good_credit = False
if has_good_credit or has_good_credit:
    print("Eligible for loan")

# And: both. or: at least one is true. And not

# if applicant has good credit but doesnt have criminal record
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
