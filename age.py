
dob= input('enter ur date of birth(yyyy-mm-dd):')
date_parts= dob.split('-')
[year,month,day]=date_parts

dob_timestamp=float(year)+float(month)/12+float(day)/365

[today_year,today_month,today_day]=['2017','03','17']
today_timestamp=float(today_year)+float(today_month)/12+float(day)/365

years=today_timestamp - dob_timestamp
months= (years - int(years)) * 12
print('your age is %d years %d months' % (years,months))




