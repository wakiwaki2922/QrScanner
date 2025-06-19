import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt, QRect, pyqtSignal, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QFont
import mss
import pyperclip
from PIL import Image
from pyzbar import pyzbar

# --- Cửa sổ Overlay để chọn vùng màn hình ---
class SelectionOverlay(QWidget):
    """
    Đây là một cửa sổ trong suốt, toàn màn hình, cho phép người dùng
    vẽ một hình chữ nhật để chọn vùng cần quét.
    """
    # Tín hiệu được phát ra khi người dùng đã chọn xong một vùng
    region_selected = pyqtSignal(QRect)

    def __init__(self):
        super().__init__()
        # Lấy kích thước màn hình
        screen_geometry = QDesktopWidget().screenGeometry()
        self.setGeometry(screen_geometry)

        # Thiết lập cờ cho cửa sổ: không có viền, luôn ở trên cùng
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # Thiết lập thuộc tính để làm cho nền cửa sổ có thể trong suốt
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Bật theo dõi chuột ngay cả khi không nhấn nút
        self.setMouseTracking(True)
        self.setCursor(Qt.CrossCursor)

        self.begin_pos = None
        self.end_pos = None
        self.is_selecting = False

    def paintEvent(self, event):
        """Vẽ lớp phủ và vùng được chọn."""
        painter = QPainter(self)
        # Vẽ một lớp phủ màu đen bán trong suốt lên toàn màn hình
        overlay_color = QColor(0, 0, 0, 100)
        painter.fillRect(self.rect(), overlay_color)

        if self.is_selecting and self.begin_pos and self.end_pos:
            # Vùng được chọn sẽ được làm trong suốt hoàn toàn
            selection_rect = QRect(self.begin_pos, self.end_pos).normalized()
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillRect(selection_rect, Qt.transparent)
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            
            # Vẽ một đường viền quanh vùng chọn để dễ nhìn
            pen = QPen(QColor("#42a5f5"), 2, Qt.SolidLine) # Màu xanh dương
            painter.setPen(pen)
            painter.drawRect(selection_rect)

    def mousePressEvent(self, event):
        """Bắt đầu chọn khi nhấn chuột trái."""
        if event.button() == Qt.LeftButton:
            self.begin_pos = event.pos()
            self.end_pos = event.pos()
            self.is_selecting = True
            self.update()

    def mouseMoveEvent(self, event):
        """Cập nhật vùng chọn khi di chuyển chuột."""
        if self.is_selecting:
            self.end_pos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        """Hoàn tất chọn khi thả chuột trái."""
        if event.button() == Qt.LeftButton and self.is_selecting:
            self.is_selecting = False
            selection_rect = QRect(self.begin_pos, self.end_pos).normalized()
            # Phát tín hiệu chứa thông tin về vùng đã chọn
            self.region_selected.emit(selection_rect)
            self.close()

# --- Cửa sổ chính của ứng dụng ---
class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.selection_overlay = None
        self.init_ui()

    def init_ui(self):
        """Khởi tạo giao diện người dùng."""
        self.setWindowTitle("Trình quét mã QR")
        self.setFixedSize(350, 200)
        self.setStyleSheet("""
            QWidget {
                background-color: #263238; /* Nền xám đen */
                color: #ECEFF1; /* Chữ trắng ngà */
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QPushButton {
                background-color: #42a5f5; /* Xanh dương */
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1e88e5; /* Xanh dương đậm hơn */
            }
            QPushButton:pressed {
                background-color: #0d47a1; /* Xanh dương rất đậm */
            }
            QLabel {
                font-size: 14px;
                color: #90A4AE; /* Xám nhạt */
                qproperty-alignment: 'AlignCenter';
            }
        """)

        # Layout chính
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Nút để bắt đầu quét
        self.scan_button = QPushButton("Quét mã QR từ màn hình")
        self.scan_button.setCursor(Qt.PointingHandCursor)
        self.scan_button.clicked.connect(self.start_selection)

        # Nhãn hiển thị trạng thái/kết quả
        self.status_label = QLabel("Nhấn nút để bắt đầu chọn vùng quét.")
        self.status_label.setWordWrap(True)

        layout.addWidget(self.scan_button)
        layout.addWidget(self.status_label)
        layout.addStretch()

        self.setLayout(layout)
        self.center_window()
        self.show()

    def center_window(self):
        """Canh giữa cửa sổ ứng dụng trên màn hình."""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start_selection(self):
        """Bắt đầu quá trình chọn vùng màn hình."""
        self.hide() # Ẩn cửa sổ chính
        # Thêm một độ trễ nhỏ để đảm bảo cửa sổ chính đã ẩn hoàn toàn
        QTimer.singleShot(150, self.show_overlay)

    def show_overlay(self):
        """Hiển thị lớp phủ để chọn vùng."""
        self.selection_overlay = SelectionOverlay()
        self.selection_overlay.region_selected.connect(self.process_region)
        self.selection_overlay.show()

    def process_region(self, region):
        """Chụp ảnh, quét mã QR và xử lý kết quả."""
        try:
            # Sử dụng mss để chụp ảnh vùng đã chọn
            with mss.mss() as sct:
                monitor = {
                    "top": region.top(),
                    "left": region.left(),
                    "width": region.width(),
                    "height": region.height()
                }
                sct_img = sct.grab(monitor)
                # Chuyển đổi ảnh sang định dạng mà pyzbar có thể đọc
                pil_img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

            # Sử dụng pyzbar để giải mã QR code
            decoded_objects = pyzbar.decode(pil_img)

            if decoded_objects:
                # Lấy dữ liệu từ mã QR đầu tiên tìm thấy
                qr_data = decoded_objects[0].data.decode("utf-8")
                pyperclip.copy(qr_data)
                
                # Cắt bớt nội dung nếu quá dài để hiển thị
                display_text = (qr_data[:60] + '...') if len(qr_data) > 60 else qr_data
                self.status_label.setText(f"<font color='#4CAF50'><b>Thành công!</b></font><br>Đã sao chép vào clipboard:<br><i>{display_text}</i>")
            else:
                self.status_label.setText("<font color='#F44336'><b>Không tìm thấy mã QR.</b></font><br>Vui lòng thử lại với vùng chọn rõ ràng hơn.")

        except Exception as e:
            self.status_label.setText(f"<font color='#F44336'><b>Đã xảy ra lỗi:</b></font><br>{str(e)}")
        finally:
            # Hiển thị lại cửa sổ chính sau khi xử lý xong
            self.show()
            self.activateWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Bạn có thể đặt icon cho ứng dụng tại đây
    # app.setWindowIcon(QIcon('path/to/your/icon.png'))
    ex = MainApp()
    sys.exit(app.exec_())
