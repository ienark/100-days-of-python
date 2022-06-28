def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False



def days_in_month(picked_year, picked_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if picked_month > 12 or picked_month <1:
      return "Invalid month"
  if is_leap(picked_year) == True and picked_month == 2:
      return month_days[picked_month-1]+1
  elif is_leap(picked_year) == False:
      return month_days[picked_month-1]
        
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












