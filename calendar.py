import calendar
y=int(input("enter the year:"))
m=1
cal=calendar.Textcalendar(calendar.sunday)
i=1
while i<=12:
    cal.prmonth(y,i)
    i+=1