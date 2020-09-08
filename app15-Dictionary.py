#Dictionary

monthConversions = {
    "jan" : "January",
    "feb" : "February",
    "mar" : "March",
    "apr" : "April",
    "may" : "May",
    "jun" : "June",
    "jul" : "July",
    "aug" : "August",
    "sep" : "September",
    "oct" : "October",
    "nov" : "November",
    "dec" : "December"
}

hold_Month = input("Month: ").lower()


if monthConversions.get(hold_Month,"Invalid") != "Invalid":
    print("[]: " + monthConversions[hold_Month])
    print("get(): " + monthConversions.get(hold_Month,"Not a valid Key"))
else:
    print("Invalid Key!")

