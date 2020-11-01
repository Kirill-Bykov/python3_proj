import numpy
import random

box_amnt = 5
razia_amnt = 5
boxes = []
razias = []


def check_size(raz, box):
    #Функция проверяет полезет ли рация в коробку
    raz.measures = sorted(raz.measures)
    box.measures = sorted(box.measures)
    for i in range(0, 3):
        if raz.measures[i] >= box.measures[i]:
            return False
        else:
            continue
    print(f"RaziaN{raz.num} measures:\nLength = {raz.len}\nWidth = {raz.wid}\nHeight = {raz.hei}")
    print(f"BoxN{box.num} measures:\nLength = {box.len}\nWidth = {box.wid}\nHeight = {box.hei}\n")
    return True


class Rect():
    def __init__(self, len, wid, hei):
        self.len = len
        self.wid = wid
        self.hei = hei
        self.measures = [len, wid, hei]


class Box(Rect):

    def __init__(self, num, len, wid, hei):
        super().__init__(len, wid, hei)
        self.num = num
        boxes.append(self)


class Razia(Rect):

    def __init__(self, num, len, wid, hei):
        super().__init__(len, wid, hei)
        self.num = num
        global razias
        razias.append(self)


def main():
    for i in range(box_amnt + 1):
        Box(i, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
    for i in range(razia_amnt + 1):
        Razia(i, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

    for box in boxes:
        for raz in razias:
            check_size(raz, box)


if __name__ == "__main__":
    main()
