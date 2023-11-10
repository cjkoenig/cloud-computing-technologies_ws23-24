from flask import Flask, render_template
from filelock import Timeout, FileLock
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.debug = False
app.logger.propagate = False # turn of logging to console

# define counter as global variable
counter = int()

@app.route('/')
def count():

    # open the file with a lock (=> concurrent processes...)
    lock = FileLock("counter.txt.lock")
    with lock:
        with open("counter.txt", "a+") as f:

            # set f pointer to begin of file (a+ sets it to the end)
            f.seek(0)
            line = f.readline()
            app.logger.info('readline: %s', line)

            # is there already a file? If, use it
            if(line != ""):
                counter = int(line)
                app.logger.info('counter1a: %s', counter)
            else:
                # No file, set counter to 0
                counter = 0
                app.logger.info('counter1b: %s', counter)
            
            # increment counter value
            counter = counter + 1
            
            # clear file and write new value as string to file (f is closed automatically)
            f.seek(0)
            f.truncate() 
            f.write(str(counter) + "\n")
    
    app.logger.info('counter2: %s', counter)

    return render_template("index.html", value=counter)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=False)
