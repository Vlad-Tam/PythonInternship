from  my_time import MyTime


if __name__ == "__main__":
    time1 = MyTime()
    time2 = MyTime(3, 4, 6)
    time3 = MyTime(20, 15, 55)
    time4 = MyTime(3, 44, 56)
    time5 = MyTime(3, 4, 6)

    print(time1, time2, time3, sep=", ")
    print(time2 == time5)
    print(time2 != time5)
    print(time3 != time1)
    print(time1)

    print(time3+time2)
    print(time3-time4)

    str_time = MyTime.init_by_string('21-32-12')
    obj_time = MyTime.init_by_object(str_time)
    print(str_time)
    print(obj_time)
