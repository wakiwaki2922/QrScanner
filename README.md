# QR Scanner - Trình Quét Mã QR

Ứng dụng quét mã QR từ màn hình máy tính với giao diện đồ họa đơn giản và thân thiện.

## Tính năng chính

- Quét mã QR từ bất kỳ vùng nào trên màn hình
- Tự động sao chép nội dung mã QR vào clipboard
- Giao diện đơn giản, dễ sử dụng
- Hỗ trợ chọn vùng quét linh hoạt

## Hướng dẫn Build từ Source Code

### Yêu cầu hệ thống

- Python 3.7 trở lên
- Windows 10/11 (khuyến nghị)

### Bước 1: Chuẩn bị môi trường

1. Clone hoặc tải source code về máy
2. Mở Command Prompt hoặc PowerShell trong thư mục dự án
3. Tạo môi trường ảo (khuyến nghị):
```bash
python -m venv venv
venv\Scripts\activate
```

### Bước 2: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### Bước 3: Cài đặt PyInstaller để build exe

```bash
pip install pyinstaller
```

### Bước 4: Build file exe

#### Tùy chọn 1: Build cơ bản (nhiều file)
```bash
pyinstaller --windowed qr_scanner_app.py
```

#### Tùy chọn 2: Build thành 1 file exe duy nhất (khuyến nghị)
```bash
pyinstaller --onefile --windowed --name "QRScanner" qr_scanner_app.py
```

#### Tùy chọn 3: Build với icon tùy chỉnh
```bash
pyinstaller --onefile --windowed --icon=icon.ico --name "QRScanner" qr_scanner_app.py
```

### Bước 5: Tìm file exe đã build

Sau khi build thành công, file exe sẽ được tạo trong thư mục:
- `dist/QRScanner.exe` (nếu dùng --onefile)
- `dist/qr_scanner_app/qr_scanner_app.exe` (nếu build cơ bản)

### Các tùy chọn PyInstaller hữu ích

| Tùy chọn | Mô tả |
|----------|--------|
| `--onefile` | Tạo file exe duy nhất thay vì thư mục chứa nhiều file |
| `--windowed` | Ẩn cửa sổ console (chỉ hiện GUI) |
| `--icon=icon.ico` | Thêm icon cho file exe |
| `--name "TenApp"` | Đặt tên cho file exe |
| `--add-data "file;."` | Thêm file/folder bổ sung vào exe |

### Lưu ý khi build

1. **Kích thước file**: Build với `--onefile` sẽ tạo file exe lớn hơn (~50-100MB) nhưng dễ phân phối
2. **Thời gian khởi động**: File exe có thể khởi động chậm hơn lần đầu do phải giải nén
3. **Antivirus**: Một số phần mềm diệt virus có thể báo false positive với file exe được build từ PyInstaller

### Khắc phục lỗi thường gặp

#### Lỗi: "Module not found"
```bash
# Cài đặt lại dependencies
pip install --upgrade -r requirements.txt
```

#### Lỗi: "Failed to execute script"
```bash
# Build không dùng --windowed để xem lỗi chi tiết
pyinstaller --onefile qr_scanner_app.py
```

#### Lỗi với PyQt5
```bash
# Cài đặt PyQt5 cụ thể cho Windows
pip uninstall PyQt5
pip install PyQt5==5.15.10
```

### Test ứng dụng

Trước khi build, hãy test ứng dụng bằng cách chạy:
```bash
python qr_scanner_app.py
```

Đảm bảo tất cả tính năng hoạt động bình thường trước khi build ra exe.

---

**Lưu ý**: File exe được build sẽ chỉ chạy trên hệ điều hành Windows. Để tạo file thực thi cho macOS hoặc Linux, bạn cần build trên hệ điều hành tương ứng. 