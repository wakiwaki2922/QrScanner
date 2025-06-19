# 🔍 QR Scanner Pro - Trình Quét Mã QR

Ứng dụng quét mã QR từ màn hình máy tính với giao diện đồ họa đơn giản và thân thiện.

## 📦 Tải về

### 🔗 Bản chính thức (Signed)
Tải file `.exe` mới nhất từ [Releases](../../releases)
- ✅ Đã được ký số để giảm false positive
- ✅ Bao gồm checksums để verify tính toàn vẹn  
- ✅ Metadata đầy đủ và mô tả chi tiết
- ✅ Build tối ưu với kích thước nhỏ (~25MB)

### 🧪 Bản thử nghiệm (Development)
- Tự động build khi có code mới
- Tải từ [Actions tab](../../actions)
- ⚠️ Chưa được ký số - có thể có antivirus warnings

### 🛡️ Xử lý False Positive
Nếu antivirus báo virus, xem [ANTIVIRUS_GUIDE.md](ANTIVIRUS_GUIDE.md) để biết cách xử lý.

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

#### ⭐ Tùy chọn khuyến nghị (Build tối ưu)
```bash
# Sử dụng script tự động
build.bat
```

#### 🔧 Build manual với spec file
```bash
pyinstaller QRScanner.spec --clean
```

#### 🛡️ Build + Self-signing (giảm false positive)
```bash
build.bat
sign_exe.bat
```

#### 🏗️ Build cơ bản (deprecated)
```bash
pyinstaller --onefile --windowed --name "QRScanner" qr_scanner_app.py
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

1. **Kích thước file**: Build tối ưu sẽ tạo file ~25MB (giảm 40% so với trước)
2. **Thời gian khởi động**: Build đã được tối ưu để khởi động nhanh hơn
3. **Antivirus**: 
   - ✅ **Signed version**: Rất ít false positive
   - ⚠️ **Unsigned version**: Có thể bị báo false positive (bình thường với PyInstaller)
   - 📋 **Xử lý**: Xem [ANTIVIRUS_GUIDE.md](ANTIVIRUS_GUIDE.md)

### 🤖 GitHub Actions CI/CD

Project này có 2 workflows tự động:

#### 🚀 Production Build (`build-release.yml`)
- **Trigger**: Khi tạo Release mới
- **Features**:
  - ✅ Build tối ưu với spec file
  - ✅ Tự động ký số (self-signed)
  - ✅ Tạo checksums cho verification
  - ✅ Upload file + metadata đầy đủ
  - ✅ Enhanced release notes

#### 🧪 Development Build (`build-test.yml`)  
- **Trigger**: Push vào main hoặc tạo PR
- **Features**:
  - ✅ Lint code quality check
  - ✅ Build test executable
  - ✅ Upload artifact cho testing
  - ✅ Auto comment PR với build info

### 📋 Workflow Usage

#### Tạo release mới:
```bash
git tag v1.0.1
git push origin v1.0.1
# Tạo release trên GitHub → tự động build & upload
```

#### Test build:
```bash
git push origin main
# Tự động build và upload artifact
```

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