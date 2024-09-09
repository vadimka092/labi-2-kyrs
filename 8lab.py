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
from tkinter import filedialog, messagebox

class Segment:
    def __init__(self, start_x, start_y, end_x, end_y, color="black"):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.color = color

    def draw(self, canvas):
        canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y, fill=self.color)

    def change_color(self, new_color):
        self.color = new_color

    def move(self, delta_x, delta_y):
        self.start_x += delta_x
        self.start_y += delta_y
        self.end_x += delta_x
        self.end_y += delta_y

def load_segments_from_file(filepath):
    segments = []
    with open(filepath, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                try:
                    segments.append(Segment(int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])))
                except ValueError:
                    messagebox.showerror("Error", "Invalid file format")
                    return []
            else:
                messagebox.showerror("Error", "Invalid file format")
                return []
    return segments

def visualize_segments(segments, canvas):
    for segment in segments:
        segment.draw(canvas)

def main():
    root = tk.Tk()
    root.title("Segment Visualizer")

    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    def open_file():
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        segments = load_segments_from_file(filepath)
        canvas.delete("all")
        visualize_segments(segments, canvas)

    open_button = tk.Button(root, text="Open File", command=open_file)
    open_button.pack(side=tk.LEFT)

    close_button = tk.Button(root, text="Close", command=root.quit)
    close_button.pack(side=tk.RIGHT)

    root.mainloop()

if __name__ == "__main__":
    main()
