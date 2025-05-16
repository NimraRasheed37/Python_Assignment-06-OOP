class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        print(f"Current count of object is: {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()
c6 = Counter()

c1.get_count()
