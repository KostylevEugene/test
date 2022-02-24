import math
import time

start_time = time.time()
end_time = time.time()
duration = 0.004673957824707031
# rounded_duration = math.ceil(duration*10000)/10000
rounded_duration = round(duration, 4)
print(rounded_duration)