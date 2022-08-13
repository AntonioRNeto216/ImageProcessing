import cv2 as cv
from typing import Tuple


class Application:
    """
    Application manage video capture and image processing.
    """

    def __init__(self) -> None:
        """
        Create face and eye cascade classifiers.
        """
        self._face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self._eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    
    def init_application(self, increase_brightness_value: int or None, gaussian_blur_kernel_size: Tuple or None, **kwargs) -> None:
        """
        Initializes the application and define values for attributes. 
        """
        video_path_kwargs_key = 'video_path'
        if len(kwargs) == 1 and video_path_kwargs_key in kwargs:
            self._video_capture = cv.VideoCapture(kwargs[video_path_kwargs_key])
        elif len(kwargs) == 1:
            raise self.ApplicationKwargsError('Missing \'video_path\' parameter')
        elif len(kwargs) == 0:
            self._video_capture = cv.VideoCapture(0)
        else:
            raise self.ApplicationKwargsError('Too much parameters')
            
        self._frame_modifiers = []

        if increase_brightness_value is not None:
            self._increase_brightness_value = increase_brightness_value
            self._frame_modifiers.append(self._increase_brightness)

        if gaussian_blur_kernel_size is not None:
            self._gaussian_blur_kernel = (gaussian_blur_kernel_size, gaussian_blur_kernel_size)
            self._frame_modifiers.append(self._gaussian_blur)

        self._verify_video_capture_is_opened()
        self._capture_frame()

    def _verify_video_capture_is_opened(self) -> None:
        """
        Verifies if Video Capture is opened.
        """
        if not self._video_capture.isOpened():
            print("Can not open video capture source. Exiting!")
            exit(1)

    def _capture_frame(self) -> None:
        """
        Stays in an infinite loop until the user press 'q' key.
        """
        while True:
            ret, self._source_frame = self._video_capture.read()
            
            if not ret:
                print("Can not receive frame. Exiting!")
                break
            
            height, width = self._source_frame.shape[:2]
            if height != 480 and width != 640:
                self._source_frame = cv.resize(self._source_frame, (640, 480))
            
            self._modified_frame = self._source_frame.copy()

            for frame_modifier in self._frame_modifiers:
                frame_modifier()
            self._face_detection()

            cv.imshow('Source frame', self._source_frame)
            cv.imshow('Modified frame', self._modified_frame)

            if cv.waitKey(1) == ord('q'):
                self._video_capture.release()
                cv.destroyAllWindows()
                break

    def _increase_brightness(self) -> None:
        """
        Increases the brightness using the attribute increase_brightness_value.
        """
        limit = 255 - self._increase_brightness_value
        self._modified_frame[self._modified_frame > limit] = 255
        self._modified_frame[self._modified_frame <= limit] += self._increase_brightness_value

    def _gaussian_blur(self) -> None:
        """
        Processes modified frame using gaussian blur.
        """
        self._modified_frame = cv.GaussianBlur(self._modified_frame, self._gaussian_blur_kernel, 0)

    def _face_detection(self) -> None:
        """
        Operations for face detection.\n
        Note: Instead of doing 'fy:fy+fh' in region of interest I've rounded 'fh/2' and added 'fy'. 
        In my opinion, this approach can minimize some classification mistakes.
        """
        face = self._face_cascade.detectMultiScale(self._modified_frame, 1.1, 6)
        for (fx, fy, fw, fh) in face:
            cv.rectangle(self._modified_frame, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 3)
            region_of_interest = self._modified_frame[fy:fy+round(fh/2), fx:fx+fw]
            eyes = self._eye_cascade.detectMultiScale(region_of_interest, 1.1, 6)
            for (ex, ey, ew, eh) in eyes:
                cv.rectangle(region_of_interest, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 3)

    class ApplicationKwargsError(Exception):
        """
        Excaption class for **kwargs errors
        """
        pass