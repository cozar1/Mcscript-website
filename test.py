number = 12323

views = ['','','','','','','',]

views[0] = str(number)[0]
views[1] = '.'
views[2] = str(number)[1]
views[3] = str(number)[2]

if len(str(number)) > 3 and len(str(number)) < 7:
    views[3] = 'K'

if len(str(number)) > 6 and len(str(number)) < 10:
    views[3] = 'M'

if len(str(number)) > 9 and len(str(number)) < 13:
    views[3] = 'B'


# Join elements into a single string
joined_string = ''.join(views)

# Strip any extra empty strings
cleaned_string = joined_string.strip()

# Format the string as desired
formatted_string = f"{cleaned_string.lower()}"

# Print the result
print(formatted_string)  # Output: 2.5m