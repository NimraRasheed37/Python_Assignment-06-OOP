class Logger:
    def __init__(self):
        print("Logger object is created.")
    
    def __del__(self):
        print("Logger object is destroyed.")

log1 = Logger()

del log1



