class Time:
    def __init__(self, hours, minutes):
        self.hours = hours % 24  # Ensure hours are within 0-23
        self.minutes = minutes % 60  # Ensure minutes are within 0-59

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

    def tick(self):
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
            if self.hours == 24:
                self.hours = 0

    def __sub__(self, other):
        total_minutes_self = self.hours * 60 + self.minutes
        total_minutes_other = other.hours * 60 + other.minutes
        diff_minutes = total_minutes_self - total_minutes_other
        hours_diff = diff_minutes // 60
        minutes_diff = diff_minutes % 60
        return f"{abs(hours_diff)} hours and {abs(minutes_diff)} minutes"

    def getTime(self):
        return (self.hours, self.minutes)

    def setTime(self, hours, minutes):
        self.hours = hours % 24
        self.minutes = minutes % 60

    def __lt__(self, other):
        return (self.hours, self.minutes) < (other.hours, other.minutes)

    def __len__(self):
        return self.hours * 60 + self.minutes

# Example usage
time1 = Time(12, 30)
time2 = Time(13, 45)

print(time1)  # Output: 12:30
print(time2)  # Output: 13:45

time1.tick()
print(time1)  # Output: 12:31

print(f"\033[1m{time2 - time1}\033[0m")  # Output: bold

print(time1.getTime())  # Output: (12, 31)
time1.setTime(14, 0)
print(time1.getTime())  # Output: (14, 0)

print(time1 < time2)  # Output: True

print(f"\033[1m{len(time1)}\033[0m")  # Output: bold
