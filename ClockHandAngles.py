#Find the angles between clock hour and minute hands

def hands_angle(hrs, mins):
    hour_place = (360/12) * (hrs % 12)
    mins_place = (360/60) * mins
    ans = abs((hour_place - mins_place) % 180)
    return ans
