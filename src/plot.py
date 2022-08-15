import os
import datetime
import matplotlib.pyplot as plt


class Plot:
    def __init__(self) -> None:
        self._x_values = []
        self._y_eyes_values = []
        self._y_face_values = []
        self._max_value_y_eyes = 2
        self._max_value_y_face = 2

    def init_plot_config(self):
        plt.ion()

        self._figure, (self._ax_eyes, self._ax_face) = plt.subplots(nrows=2, figsize=(5,4), sharex=True)

        self._line_eyes, = self._ax_eyes.plot(self._x_values, self._y_eyes_values, color='red', marker='o', linewidth=0.2, markersize=2)
        self._line_face, = self._ax_face.plot(self._x_values, self._y_face_values, color='blue', marker='o', linewidth=0.2, markersize=2)

        self._ax_eyes.set_title('Dynamic Plot of Eyes Detection', fontsize=12)
        self._ax_eyes.set_ylabel('Number of Eyes Detected', fontsize=8)

        self._ax_face.set_title('Dynamic Plot of Face Detection', fontsize=12)
        self._ax_face.set_ylabel('Number of Faces Detected', fontsize=8)
        self._ax_face.set_xlabel('Number of Iterations', fontsize=8)
        

    def draw(self, new_y_eyes_value: int, new_y_face_value: int):
        self._x_values.append(len(self._x_values))
        self._y_eyes_values.append(new_y_eyes_value)
        self._y_face_values.append(new_y_face_value)
        
        if new_y_eyes_value > self._max_value_y_eyes:
            self._max_value_y_eyes = new_y_eyes_value
        
        if new_y_face_value > self._max_value_y_face:
            self._max_value_y_face = new_y_face_value

        self._ax_eyes.set_xlim(0, len(self._x_values))
        self._ax_eyes.set_ylim(0, self._max_value_y_eyes + 1)
        
        self._ax_face.set_xlim(0, len(self._x_values))
        self._ax_face.set_ylim(0, self._max_value_y_face + 1)
        
        self._line_eyes.set_xdata(self._x_values)
        self._line_eyes.set_ydata(self._y_eyes_values)

        self._line_face.set_xdata(self._x_values)
        self._line_face.set_ydata(self._y_face_values)
        
        self._figure.canvas.draw()
        self._figure.canvas.flush_events()

    def end_plot(self):
        plt.savefig(f'{os.getcwd()}/plots/{datetime.datetime.now()}.png')
        plt.close('all')