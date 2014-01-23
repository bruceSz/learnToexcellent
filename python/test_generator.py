from time import sleep

event_listeners = {}

def fire_event(name):
    event_listeners[name]()

def use_event(func):
    def call(*args,**kwargs):
        generator = func(*args,**kwargs)

        event_name = next(generator)

        def resume():
            try:
                next(generator)
            except StopIteration:
                pass
        event_listeners[event_name] = resume
    return call

@use_event
def test_work():
    print("="*50)
    print("waiting click")
    yield "click"
    print("clicked !!")

def simplest_yield():
    print "begin yield"
    yield "yielded!"
    print "end yield"

def test_yield():
    generator = simplest_yield() 
    next(generator)
    #next(generator)
if __name__ == '__main__':
    test_work()
    sleep(3)
    fire_event("click")
#    test_yield()


