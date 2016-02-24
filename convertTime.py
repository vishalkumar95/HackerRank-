import sys

'''This function takes a time in AM/PM format and converts it to military (24-hour) time'''
''' Sample input : 07:05:45PM'''
''' Sample Output : 19:05:45'''

def converttime():
    time = input('Enter the time in AM/PM format: ').strip()

    zone = time[8] + time[9]
    hour = time[0] + time[1]
    a = int(hour)
    if zone == 'AM' and str(a) == '12':
        a = '00'
        time = a + time[2:8]
        print (time)
        return
    elif zone == 'PM' and str(a) == '12':
        time = str(a) + time[2:8]
        print(time)
        return
    elif zone == 'PM':
        a = a + 12
        time = str(a) + time[2:8]
        print (time)
        return
    elif zone == 'AM':
        time = time[0:8]
        print (time)
        return

    
