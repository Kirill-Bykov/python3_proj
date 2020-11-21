#  первая программа для этого ноубтука
import random as rnd
import time
import msvcrt as m
import os
from threading import Thread

COLORS = ['01', '02', '03', '04', '05', '06', '07', '08', '09']

def rainbow(COLORS):
#Команда в командную строку на смену цвета символов в соответствии с массивом COLORS
    while True:
        for color in COLORS:
            os.system(f'color {color}')
            time.sleep(0.05)



# CLASSES

class Threader():
    def __init__(self):
        self.thread_opened: int = 0
        self.thread_started: int = 0
        self.thread_joined: int = 0
        self.threads_opened_dict = {}
        self.threads_started_dict = {}
        self.threads_joined_dict = {}

    def open_thread(self, target, *args):
        thread = Thread(target=target, args=args)
        self.thread_opened += 1
        self.threads_opened_dict[f"num{self.thread_opened}"] = thread
        return thread

    def start_thread(self, thread):
        self.thread_started += 1
        thread.start()
        self.threads_started_dict[f"num{self.thread_started}"] = thread

    def join_thread(self, thread):
        self.thread_joined += 1
        thread.join()
        self.threads_joined_dict[f"num{self.thread_joined}"] = thread

    def start_all_threads(self):
        for thread in self.threads_opened_dict:
            self.start_thread(thread)

    def join_all_threads(self):
        for thread in self.threads_started_dict:
            self.join_thread(thread)


class Timer():

    def __init__(self):
        self.lap_times = {}
        self.laps = 0
        self.time = 0

    def start(self):
        self.start_time = time.time()

    def lap(self):
        self.laps += 1
        self.lap_times[self.laps] = time.time()

    def stop(self):
        self.stop_time = time.time()

    def time_stamp(self):
        self.time = self.stop_time - self.start_time
        return self.time

    def avg_time(self):
        return (self.time_stamp() / self.laps)


class Star_field():
    def __init__(self, len, hei):
        self.len = len
        self.hei = hei
        self.field = [[b'*'] * len for i in range(hei)]

    def set_elem(self, x, y, elem):
        self.field[y][x] = elem

    def display(self):
        for row in self.field:
            for elem in row:
                m.putch(elem)
            m.putch(b'\n')

    def check_full(self):
        for y in range(0, self.hei):
            for x in range(0, self.len):
                if self.field[y][x] == b'*':
                    return False
            return True

    def check_in_pose(self, x, y, char):
        if char == self.field[y][x]:
            return True
        else:
            return False


class Getcher():
    def __init__(self, delay=0.1):
        self.delay = delay

    def getch(self):
        time.sleep(self.delay)
        inp = m.getch()
        return inp


def main():
    attempts = 0
    hits = 0
    misses = 0
    lenght = 50
    height = 25
    timer = Timer()
    field = Star_field(lenght, height)
    timer.start()
    os.system('cls')

    while True:
        rand_b_input = bytes(str(rnd.randint(1, 2)), encoding='utf-8')
        while True:
            rand_x, rand_y = rnd.randint(0, lenght - 1), rnd.randint(0, height - 1)
            if field.check_in_pose(rand_x, rand_y, b'*') or field.check_full():
                break
            else:
                continue
        field.set_elem(rand_x, rand_y, rand_b_input)
        field.display()
        b_inp = m.getch()
        timer.lap()
        if b_inp == b'\r' or field.check_full():
            break
        attempts += 1
        if b_inp == rand_b_input:
            hits += 1
            os.system('cls')
            continue
        else:
            misses += 1
            os.system('cls')
            continue
    timer.stop()
    os.system('cls')
    print("your accuracy:", round((hits / attempts), 2))
    print("Avarage time:", round(timer.avg_time(), 2))
    print("Attempts:", attempts)
    print("Hits:", hits)
    print("misses:", misses)
    if m.getch() == b'\x1b':
        exit()


if __name__ == "__main__":
    t_o = Threader()
    t1 = t_o.open_thread(rainbow,COLORS)
    t1.start()
    t2 = t_o.open_thread(main())
    t2.start()