# Image Processing
Image Processing project using:
- Python: https://www.python.org/
- OpenCV: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- Tkinter: https://docs.python.org/3/library/tkinter.html
- Matplotlib: https://matplotlib.org/

## 📎 Motivation
The project purpose was to improve my knowledge in Python and, in addition, get experience on OpenCV, Tkinter and Matplotlib.

## 📋 Features
- User interface.

![Captura de tela de 2022-08-15 17-49-41](https://user-images.githubusercontent.com/56635452/184771949-fc9cefe1-3c8c-402c-8661-559b5b9048d4.png)

- Source frame and processed frame side by side.

![Captura de tela de 2022-08-15 17-51-56](https://user-images.githubusercontent.com/56635452/184772381-7d081338-e123-4d16-9baa-c2e8e8318db0.png)

- Visualization in graphs of the number of eyes and faces detected.

![2022-08-15 17:44:32 918204](https://user-images.githubusercontent.com/56635452/184772752-3fbe5cfd-7254-4295-9512-1b747ee2d1a0.png)

## 📈 Note about face detection (Region of interest)
The region of interest (ROI) is where the eye cascade classifier needs to look for a pair of eyes, because ROI is a region returned by face cascade classifier.

My first approach to calculate ROI was setting up y axis as:
```
fy:fy+fh
```
Output plot using Example2.mp4 (Click in the image to see plot video):
<div align="left">
      <a href="https://www.youtube.com/watch?v=dsKG1f1Ugzo">
         <img src="https://user-images.githubusercontent.com/56635452/184773947-de59bb42-08d2-4fad-b55e-fcdd9a920fd8.png" style="width:50%;">
      </a>
</div>

But in the video there is only one face and two eyes so I decided to change how y axis is defined to minimize some classification mistakes. In the approach below, the ROI is only a half of face region.
```
fy:fy+round(fh/2)
```
Output plot using Example2.mp4 (Click in the image to see plot video):
<div align="left">
      <a href="https://www.youtube.com/watch?v=ne12vNbTR3Q">
         <img src="https://user-images.githubusercontent.com/56635452/184779395-d15f666c-1269-4f63-80e7-d49b9aaf1323.png" style="width:50%;">
      </a>
</div>
