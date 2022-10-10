total_count_pages = int(input())
pages_for_hour = int(input())
days = int(input())
total_hours = total_count_pages // pages_for_hour
hours_per_day = total_hours // days
print (hours_per_day)

