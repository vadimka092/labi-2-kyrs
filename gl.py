'''
Требуется написать объектно-ориентированную программу с графическим интерфейсом в соответствии со своим вариантом.
В программе должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
Ввод данных из файла с контролем правильности ввода.
Базы данных использовать нельзя. При необходимости сохранять информацию в виде файлов, разделяя значения запятыми или пробелами.
Для GUI использовать библиотеку tkinter.

Вариант 20
Объекты – отрезки
Функции:	сегментация
визуализация
раскраска
перемещение на плоскости
'''


import tkinter as tk
from tkinter import filedialog
from random import randint

class Segment:
    def __init__(self, canvas, start_x, start_y, end_x, end_y, color="black"):
        self.canvas = canvas
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.color = color
        self.segment_id = canvas.create_line(start_x, start_y, end_x, end_y, fill=color)

    def segmentate(self, segments_count):
        """Разбивает отрезок на указанное количество сегментов."""
        segment_length_x = (self.end_x - self.start_x) / segments_count
        segment_length_y = (self.end_y - self.start_y) / segments_count
        segments = []
        for i in range(segments_count):
            start_x = self.start_x + i * segment_length_x
            start_y = self.start_y + i * segment_length_y
            end_x = start_x + segment_length_x
            end_y = start_y + segment_length_y
            segments.append(Segment(self.canvas, start_x, start_y, end_x, end_y, self.color))
        return segments

    def visualize(self):
        """Визуализирует отрезок на холсте."""
        self.canvas.coords(self.segment_id, self.start_x, self.start_y, self.end_x, self.end_y)
        self.canvas.itemconfig(self.segment_id, fill=self.color)

    def recolor(self, color):
        """Изменяет цвет отрезка."""
        self.color = color
        self.canvas.itemconfig(self.segment_id, fill=color)

    def move(self, delta_x, delta_y):
        """Перемещает отрезок на указанные значения по x и y."""
        self.start_x += delta_x
        self.end_x += delta_x
        self.start_y += delta_y
        self.end_y += delta_y
        self.visualize()

def load_segments_from_file(canvas):
    filepath = filedialog.askopenfilename()
    if not filepath:
        return []
    with open(filepath, "r") as file:
        segments = []
        for line in file:
            parts = line.split(',')
            if len(parts) == 4:
                try:
                    start_x, start_y, end_x, end_y = map(int, parts)
                    segments.append(Segment(canvas, start_x, start_y, end_x, end_y))
                except ValueError:
                    pass
        return segments

root = tk.Tk()
root.title("Segment Visualizer")


canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()


load_button = tk.Button(root, text="Load Segments", command=lambda: load_segments_from_file(canvas))
load_button.pack()


root.mainloop()