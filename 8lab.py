'''
Требуется написать объектно-ориентированную программу с графическим интерфейсом в соответствии со своим вариантом.
В программе должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
Ввод данных из файла с контролем правильности ввода.
Базы данных использовать нельзя. При необходимости сохранять информацию в виде файлов, разделяя значения запятыми или пробелами.
Для GUI использовать библиотеку tkinter.

Вариант 30
Объекты – отрезки
Функции:	сегментация
визуализация
раскраска
перемещение на плоскости
'''



import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

class Segment:
    def __init__(self, start_x, start_y, end_x, end_y, color='black'):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.color = color

    def draw(self, canvas):
        canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y, fill=self.color, width=2)

def load_segments_from_file(filepath, canvas, segments):
    try:
        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    start_x, start_y, end_x, end_y, color = parts
                    segment = Segment(int(start_x), int(start_y), int(end_x), int(end_y), color.strip())
                    segments.append(segment)
                    segment.draw(canvas)
    except Exception as e:
        messagebox.showerror("Ошибка загрузки", f"Не удалось загрузить файл:\n{e}")

def change_color(segment, canvas, segments):
    color = colorchooser.askcolor()[1]
    if color:
        segment.color = color
        canvas.delete("all")
        for s in segments:
            s.draw(canvas)

def change_position(segment, canvas, segments):
    def save_position():
        try:
            segment.start_x = int(entry_start_x.get())
            segment.start_y = int(entry_start_y.get())
            segment.end_x = int(entry_end_x.get())
            segment.end_y = int(entry_end_y.get())
            canvas.delete("all")
            for s in segments:
                s.draw(canvas)
        except ValueError:
            messagebox.showerror("Ошибка", "Неправильный формат координат")

    top = tk.Toplevel()
    tk.Label(top, text="Начало X").grid(row=0, column=0)
    tk.Label(top, text="Начало Y").grid(row=1, column=0)
    tk.Label(top, text="Конец X").grid(row=2, column=0)
    tk.Label(top, text="Конец Y").grid(row=3, column=0)
    entry_start_x = tk.Entry(top)
    entry_start_x.insert(0, str(segment.start_x))
    entry_start_x.grid(row=0, column=1)
    entry_start_y = tk.Entry(top)
    entry_start_y.insert(0, str(segment.start_y))
    entry_start_y.grid(row=1, column=1)
    entry_end_x = tk.Entry(top)
    entry_end_x.insert(0, str(segment.end_x))
    entry_end_x.grid(row=2, column=1)
    entry_end_y = tk.Entry(top)
    entry_end_y.insert(0, str(segment.end_y))
    entry_end_y.grid(row=3, column=1)
    tk.Button(top, text="Сохранить", command=save_position).grid(row=4, column=0, columnspan=2)

def add_segment(canvas, segments):
    def save_segment():
        try:
            start_x = int(entry_start_x.get())
            start_y = int(entry_start_y.get())
            end_x = int(entry_end_x.get())
            end_y = int(entry_end_y.get())
            color = colorchooser.askcolor()[1]
            segment = Segment(start_x, start_y, end_x, end_y, color)
            segments.append(segment)
            canvas.delete("all")
            for s in segments:
                s.draw(canvas)
        except ValueError:
            messagebox.showerror("Ошибка", "Неправильный формат координат")

    top = tk.Toplevel()
    tk.Label(top, text="Начало X").grid(row=0, column=0)
    tk.Label(top, text="Начало Y").grid(row=1, column=0)
    tk.Label(top, text="Конец X").grid(row=2, column=0)
    tk.Label(top, text="Конец Y").grid(row=3, column=0)
    entry_start_x = tk.Entry(top)
    entry_start_x.grid(row=0, column=1)
    entry_start_y = tk.Entry(top)
    entry_start_y.grid(row=1, column=1)
    entry_end_x = tk.Entry(top)
    entry_end_x.grid(row=2, column=1)
    entry_end_y = tk.Entry(top)
    entry_end_y.grid(row=3, column=1)
    tk.Button(top, text="Сохранить", command=save_segment).grid(row=4, column=0, columnspan=2)

def main():
    global segments
    root = tk.Tk()
    root.title("Визуализатор отрезков")

    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    segments = []

    def open_file():
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        canvas.delete("all")
        segments.clear()
        load_segments_from_file(filepath, canvas, segments)

    def show_segments():
        top = tk.Toplevel()
        for i, segment in enumerate(segments):
            frame = tk.Frame(top)
            frame.pack(fill=tk.X)
            tk.Label(frame, text=f"Сегмент {i+1}").pack(side=tk.LEFT)
            tk.Button(frame, text="Изменить цвет", command=lambda segment=segment: change_color(segment, canvas, segments)).pack(side=tk.LEFT)
            tk.Button(frame, text="Изменить положение", command=lambda segment=segment: change_position(segment, canvas, segments)).pack(side=tk.LEFT)

    frame = tk.Frame(root)
    frame.pack(side=tk.BOTTOM, fill=tk.X)
    tk.Button(frame, text="Загрузить файл", command=open_file).pack(side=tk.LEFT, fill=tk.X, expand=True)
    tk.Button(frame, text="Показать отрезки", command=show_segments).pack(side=tk.LEFT, fill=tk.X, expand=True)
    tk.Button(frame, text="Добавить отрезок", command=lambda: add_segment(canvas, segments)).pack(side=tk.LEFT, fill=tk.X, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()

