import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtMultimediaWidgets import QCameraViewfinder

class CameraWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aperçu caméra (sans OpenCV)")
        self.setGeometry(100, 100, 800, 600)

        # Mise en page
        layout = QVBoxLayout()
        self.viewfinder = QCameraViewfinder()
        layout.addWidget(self.viewfinder)
        self.setLayout(layout)

        # Sélection de la caméra disponible
        available_cameras = QCameraInfo.availableCameras()
        if not available_cameras:
            raise RuntimeError("Aucune caméra détectée.")

        # Utiliser la première caméra
        self.camera = QCamera(available_cameras[0])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CameraWindow()
    win.show()
    sys.exit(app.exec_())
