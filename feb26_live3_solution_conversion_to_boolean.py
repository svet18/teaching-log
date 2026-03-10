# Dichotomous variables:
#   Yes/No
#   Graduate/Non-graduate
#   Veteran/Non-veteran
#   Before/After
#   0/1


# If not converted, Python sees it as a String:
tired = "No"
print(type(tired))

# Need to convert for filtering, counting, analyses
tired_r = tired == "No"
print(type(tired_r))


