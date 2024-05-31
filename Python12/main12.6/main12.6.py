from  my_time import MyTime


if __name__ == "__main__":
    print(MyTime.counter)
    time1 = MyTime()
    time2 = MyTime(3, 4, 6)
    time3 = MyTime(20, 15, 55)
    time4 = MyTime(3, 44, 56)
    time5 = MyTime(3, 4, 6)
    print(MyTime.counter)

    str_time = MyTime.init_by_string('21-32-12')
    obj_time = MyTime.init_by_object(str_time)
    print(MyTime.counter)
