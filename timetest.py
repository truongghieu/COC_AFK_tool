from datetime import datetime, timedelta

current_time = datetime.now()
delta = timedelta(minutes=15)

next_time = current_time + delta    
print(next_time.hour, next_time.minute)