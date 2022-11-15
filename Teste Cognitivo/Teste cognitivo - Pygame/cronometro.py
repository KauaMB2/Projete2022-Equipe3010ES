from threading import Timer
def setInterval(function, interval, *params, **kwparams):
    def setTimer(wrapper):
        wrapper.timer = Timer(interval, wrapper)
        wrapper.timer.start()
    def wrapper():
        function(*params, **kwparams)
        setTimer(wrapper)
    setTimer(wrapper)
    return wrapper
def clearInterval(wrapper):
    wrapper.timer.cancel()