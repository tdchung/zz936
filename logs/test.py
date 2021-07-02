
def mytest():
    from util_log import log3, log2, log, logw, loge, logc, logr
    log3("debug2")
    log2("debug")
    log("info")
    logw("warning")
    loge("error")
    logc("critical")

    try:
        a = 1 / 0
    except Exception as e:
        logr("error", e)
        loge("Catcch"), e



############################################################################
if __name__ == "__main__":
    mytest()


"""
03.07.21 00:06:55|DEBUG   |   __main__    |    mytest     |  5|debug
03.07.21 00:06:55|INFO    |   __main__    |    mytest     |  6|info
03.07.21 00:06:55|WARNING |   __main__    |    mytest     |  7|warning
03.07.21 00:06:55|ERROR   |   __main__    |    mytest     |  8|error
NoneType: None
03.07.21 00:06:55|CRITICAL|   __main__    |    mytest     |  9|critical
03.07.21 00:06:55|ERROR   |   __main__    |    mytest     | 14|error,division by zero
03.07.21 00:06:55|ERROR   |   __main__    |    mytest     | 15|Catcch
Traceback (most recent call last):

  File "D:/_devs/Python01/gitdev/arepo/zz936/logs\test.py", line 21, in <module>
    mytest()
    └ <function mytest at 0x000001835D132EA0>

> File "D:/_devs/Python01/gitdev/arepo/zz936/logs\test.py", line 12, in mytest
    a = 1 / 0

ZeroDivisionError: division by zero

Process finished with exit code 0


"""
