from datetime import datetime, timedelta

class Event:
    def __init__(self, name: str, start_time: str, end_time: str, time_format: str, priority: bool = False):
        self.start_time = datetime.strptime(start_time, time_format)
        self.end_time = datetime.strptime(end_time, time_format)
        assert self.start_time <= self.end_time, f"Attempted to create event where end time ({str(self.end_time)}) preceded start time ({str(self.start_time)})"
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"{self.name}: {str(self.start_time)} to {str(self.end_time)}"

def fillSchedule(events):
    events.sort(key=lambda x: x.end_time)

    displacements = sorted([(
            x.start_time - events[0].start_time,
            x.end_time - events[0].start_time,
            x.priority,
            idx) for idx, x in enumerate(events)],
        key=lambda x: x[1])

    chosen_events = set()

    for i in displacements:
        if i[2]: chosen_events.add(i[3])

    for idx, dp in enumerate(displacements):
        if dp[2]:
            i = idx-1
            while i >= 0:
                if displacements[i][1] > dp[0]:
                    assert displacements[i][3] not in chosen_events, f"Attempted to prioritize two conflicting events in the schedule: 1. {str(events[idx].start_time)} - {str(events[idx].end_time)}); 2. {str(events[i].start_time)} {str(events[i].end_time)}"
                    displacements.pop(i)
                    i -= 1
                else: break
            i = idx+1
            while i < len(displacements):
                if displacements[i][1] < dp[0]:
                    assert displacements[i][3] not in chosen_events, f"Attempted to prioritize two conflicting events in the schedule: 1. {str(events[idx].start_time)} - {str(events[idx].end_time)}); 2. {str(events[i].start_time)} {str(events[i].end_time)}"
                    displacements.pop(i)
                else: break

    end = -1
    for idx, time in enumerate(displacements):
        if end <= time[0].seconds:
            end = time[1].seconds
            chosen_events.add(time[3])
    return [events[i] for i in range(len(events)) if i in chosen_events]


format = "%Y-%m-%d %H:%M:%S"
today = datetime.today().strftime('%Y-%m-%d')
events = [
    Event("Event ABC", f"{today} 9:00:00", f"{today} 10:00:00", format),
    Event("Event DEF", f"{today} 8:00:00", f"{today} 9:00:00", format),
    Event("Event GHI", f"{today} 4:00:00", f"{today} 6:00:00", format),
    Event("Event JKL", f"{today} 7:00:00", f"{today} 11:00:00", format),
]
schedule = fillSchedule(events)
for i in schedule:
    print(i)

"""
        1   2   3   4   5   6   7   8   9   10  11  12
_ABC                                    *--*
*DEF                                *--*
_GHI                *------*
_JKL                            *--------------*
"""
# event = Event("Event ABC", f"{today} 9:00:00", f"{today} 10:00:00", format)
# speak_output = f"From {event.start_time.strftime('%H:%M')} to {event.start_time.strftime('%H:%M')}"

"""
open greedy scheduler
add dentist appointment from 9 AM to 10 AM
add soccer game from 8 AM to 9 AM
add watch Loki show from 4 AM to 6 AM
add birthday party from 7 AM to 11 AM
tell me the events I have today
"""