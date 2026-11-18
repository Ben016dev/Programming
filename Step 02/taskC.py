name = input("Name: ")
wage = float(input("Wage (hourly): "))
hours_worked = float(input("Hours worked: "))
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52

gross_pay = wage * hours_worked

federal_tax = int(gross_pay * FEDERAL_TAX_RATE * 100) / 100
state_tax = int(gross_pay * STATE_TAX_RATE * 100) / 100
social_security_rate = int(gross_pay * SOCIAL_SECURITY_RATE * 100) / 100
medicare_rate = int(gross_pay * MEDICARE_RATE * 100) / 100

total_tax = federal_tax + state_tax + social_security_rate + medicare_rate

net_pay = gross_pay - total_tax
percent_kept = net_pay / gross_pay * 100
yearly_gross = gross_pay * WEEKS_PER_YEAR
yearly_net = net_pay * WEEKS_PER_YEAR

print("=" * 32)
print("PAY STUB: " + name)
print("=" * 32)
print("Hours worked:      " + str(hours_worked))
print("Hourly rate:       " + str(wage))
print("Gross pay:         " + str(gross_pay))
print("-" * 32)
print("Federal tax (" + str(FEDERAL_TAX_RATE * 100) + "%): $" + str(federal_tax))
print("State tax (" + str(int(STATE_TAX_RATE * 1000) / 10) + "%):    $" + str(state_tax))
print("Social Security:     $" + str(social_security_rate))
print("Medicare:            $" + str(medicare_rate))
print("Total taken out:     $" + str(total_tax))
print("-" * 32)
print("NET PAY:           " + str(net_pay))
print("=" * 32)
print("You keep " + str(percent_kept) + "% of what you earn.")
print("Yearly gross: " + str(yearly_gross))
print("Yearly net: " + str(yearly_net))
