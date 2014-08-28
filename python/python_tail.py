import time
def follow(thefile):
    # go to the send of the file
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue

        yield time
