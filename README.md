<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
        🎓 Khoa Công nghệ Thông tin - Đại học Đại Nam
    </a>
</h2>

<h2 align="center">
    THÀNH PHỐ THÔNG MINH - NÔNG NGHIỆP THÔNG MINH
</h2>

<p align="center">
    <img src="dnu_logo.png" alt="DaiNam University Logo" width="200"/><br>
</p>

<p align="center">
  <a href="https://www.facebook.com/DNUAIoTLab">
    <img src="https://img.shields.io/badge/AIoTLab-green?style=for-the-badge" alt="AIoTLab" />
  </a>
  <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    <img src="https://img.shields.io/badge/Khoa%20Công%20nghệ%20Thông%20tin-blue?style=for-the-badge" alt="Khoa CNTT" />
  </a>
  <a href="https://dainam.edu.vn">
    <img src="https://img.shields.io/badge/Đại%20học%20Đại%20Nam-orange?style=for-the-badge" alt="Đại học Đại Nam" />
  </a>
</p>


---

## 📌 Giới thiệu chung

Dự án này nằm trong học phần **Nông nghiệp thông minh** theo định hướng **Thành phố thông minh (Smart City)**. Hệ thống được thiết kế nhằm **giám sát chất lượng nước** trong **mô hình thủy canh**, tập trung vào **độ pH** và **độ đục (NTU)**. Hệ thống có khả năng gửi thông báo email khi phát hiện thông số vượt ngưỡng, góp phần nâng cao hiệu quả canh tác và tự động hóa trong nông nghiệp.

---

## 🧭 Sơ đồ hệ thống & Chức năng

### 🛠 Chức năng chính:
- **Đọc dữ liệu cảm biến:** Thu thập giá trị pH và độ đục từ hệ thống trồng cây thủy canh.
- **Truyền dữ liệu:** Arduino gửi dữ liệu qua UART sang ESP32.
- **Hiển thị giao diện web:** Flask hiển thị dữ liệu dạng biểu đồ và thông số.
- **Gửi cảnh báo email:** Khi pH hoặc NTU vượt ngưỡng an toàn.
- **Lưu trữ dữ liệu:** Tự động lưu lại dữ liệu theo thời gian thực để thống kê.

### 🖼️ Ảnh giao diện
![Giao diện trang web](anh.jpg)

