from my_time import MyTime

if __name__ == "__main__":
    time1 = MyTime()
    time2 = MyTime(3, 4, 6)
    time3 = MyTime(20, 15, 55)
    time4 = MyTime(3, 44, 56)
    time5 = MyTime(3, 4, 6)
    time6 = MyTime(10, 232, 67)

    print(time1, time2, time3, time4, time5, time6, sep=", ")

    print(f'{time2} == {time5}: {time2 == time5}')
    print(f'{time2} != {time5}: {time2 != time5}')
    print(f'{time3} != {time1}: {time3 != time1}')

    print(f'{time3} > {time1}: {time3 != time1}')
    print(f'{time2} >= {time5}: {time2 >= time5}')
    print(f'{time4} <= {time5}: {time4 <= time5}')

    print(f'{time2} * 3: {time2 * 3}')
    print(f'{time3} * 4: {time3 * 4}')
    print(f'{time3} + {time2}: {time3 + time2}')
    print(f'{time3} - {time4}: {time3 - time4}')

    str_time = MyTime.init_by_string('21-32-12')
    obj_time = MyTime.init_by_object(str_time)
    print(str_time)
    print(obj_time)
