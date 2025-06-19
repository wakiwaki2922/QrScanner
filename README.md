# 🔍 QR Scanner - Trình Quét Mã QR

Ứng dụng quét mã QR từ màn hình máy tính đơn giản và nhanh chóng.

## 📦 Tải về

Tải file `.exe` từ [Releases](../../releases) hoặc [Actions](../../actions) cho bản development.

## Tính năng chính

- Quét mã QR từ bất kỳ vùng nào trên màn hình
- Tự động sao chép nội dung mã QR vào clipboard
- Giao diện đơn giản, dễ sử dụng
- Hỗ trợ chọn vùng quét linh hoạt

## Build từ Source

### Yêu cầu
- Python 3.7+
- Windows 10/11

### Cách build
```bash
# Cài đặt dependencies
pip install -r requirements.txt
pip install pyinstaller

# Build
build.bat
# hoặc
pyinstaller QRScanner.spec --clean
```

File exe sẽ được tạo trong thư mục `dist/`

### Chạy từ source
```bash
python qr_scanner_app.py
``` 