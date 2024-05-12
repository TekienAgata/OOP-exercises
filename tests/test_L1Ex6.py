from L1Ex6 import Time


def test_time_init_incorrect_hour_value(capsys):
    t1 = Time(42)
    out, err = capsys.readouterr()
    assert t1.hour == 0
    assert t1.minute == 0
    assert t1.second == 0
    assert out.strip() == (
        "Provided hour is outside of allowed values (0-23)\n" "Setting hour to 0"
    )


def test_time_init_incorrect_minute_correct_hour(capsys):
    t1 = Time(1, 333)
    out, err = capsys.readouterr()
    assert t1.hour == 1
    assert t1.minute == 0
    assert t1.second == 0
    assert out.strip() == (
        "Provided minute is outside of allowed values (0-59)\n" "Setting minute to 0"
    )


def test_time_init_hour_incorrect_minute_correct_second_incorrect(capsys):
    t1 = Time(33, 59, 60)
    out, err = capsys.readouterr()
    assert t1.hour == 0
    assert t1.minute == 59
    # assert t1.second == 0
    assert out.strip() == (
        "Provided hour is outside of allowed values (0-23)\n"
        "Setting hour to 0\n"
        "Provided second is outside of allowed values (0-59)\n"
        "Setting second to 0"
    )


def test_time_incorrect_init_incorrect_set_time_correct_set_time(capsys):
    t1 = Time(-1, -1, -1)
    t1.set_time(-2, -2, -2)
    t1.set_time(16, 26, 3)
    out, err = capsys.readouterr()
    assert out.strip() == (
        "Provided hour is outside of allowed values (0-23)\n"
        "Setting hour to 0\n"
        "Provided minute is outside of allowed values (0-59)\n"
        "Setting minute to 0\n"
        "Provided second is outside of allowed values (0-59)\n"
        "Setting second to 0\n"
        "Provided hour is outside of allowed values (0-23)\n"
        "Setting hour to 0\n"
        "Provided minute is outside of allowed values (0-59)\n"
        "Setting minute to 0\n"
        "Provided second is outside of allowed values (0-59)\n"
        "Setting second to 0"
    )
    assert t1.hour == 16
    assert t1.minute == 26
    assert t1.second == 3


def test_time_repr():
    t1 = Time(8, 3, 26)
    t2 = eval(repr(t1))
    assert t1.hour == t2.hour
    assert t1.minute == t2.minute
    assert t1.second == t2.second


def test_time_str(capsys):
    t1 = Time(14, 15, 33)
    print(str(t1))
    out, err = capsys.readouterr()
    assert out.strip() == "2:15:33 PM"
