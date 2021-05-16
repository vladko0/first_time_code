time_first = int(input())  # първи
time_two = int(input())  # втори
time_third = int(input())  # трети

total_time = time_first + time_two + time_third
#  макс време => 3 - 150 сек.
#  минути:секунди

minutes = total_time // 60
seconds = total_time % 60  # mod деление.

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
