filing_status = input("Enter your filing status (Single, Married Filing Jointly, Married Filing Separately, Head of Household): ").lower()
income = float(input("Enter your taxable income: "))

if filing_status == "single":
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 835 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 4675 + (income - 33950) * 0.25
    elif income <= 171550:
        tax = 16725 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 41775 + (income - 171550) * 0.33
    else:
        tax = 108216 + (income - 372950) * 0.35
elif filing_status == "married filing jointly":
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 1670 + (income - 16700) * 0.15
    elif income <= 137050:
        tax = 10125 + (income - 67900) * 0.25
    elif income <= 208850:
        tax = 26625 + (income - 137050) * 0.28
    elif income <= 372950:
        tax = 46675 + (income - 208850) * 0.33
    else:
        tax = 102576 + (income - 372950) * 0.35
elif filing_status == "married filing separately":
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 835 + (income - 8350) * 0.15
    elif income <= 68525:
        tax = 5062.50 + (income - 33950) * 0.25
    elif income <= 104425:
        tax = 13312.50 + (income - 68525) * 0.28
    elif income <= 186475:
        tax = 23337.50 + (income - 104425) * 0.33
    else:
        tax = 51312 + (income - 186475) * 0.35
elif filing_status == "head of household":
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 1195 + (income - 11950) * 0.15
    elif income <= 117450:
        tax = 6425 + (income - 45500) * 0.25
    elif income <= 190200:
        tax = 24375 + (income - 117450) * 0.28
    elif income <= 372950:
        tax = 42175 + (income - 190200) * 0.33
    else:
        tax = 106043 + (income - 372950) * 0.35
else:
    tax = "Invalid filing status entered"

print(f"Tax due: {tax}")
