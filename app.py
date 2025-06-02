from flask import Flask, request, render_template, redirect, url_for, send_file
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# Biến lưu dữ liệu cảm biến mới nhất
latest_data = {
    "timestamp": "",
    "ph": "N/A",
    "turb": "N/A"
}

# Cấu hình email
GMAIL_USER = "phungdanghau8@gmail.com"
GMAIL_PASS = "lnyn bttn foqm lcge"
RECEIVER_EMAIL = "phungdanghau10@gmail.com"

# Hàm gửi email
def send_email_report(ph, turb, timestamp):
    msg = EmailMessage()
    msg['Subject'] = '📊 Báo cáo cảm biến từ ESP32 - Đại Nam'
    msg['From'] = GMAIL_USER
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(f"""\nDữ liệu mới từ hệ thống cảm biến Đại Nam:

- pH: {ph}
- Độ đục: {turb}
- Thời gian: {timestamp}
""")
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_USER, GMAIL_PASS)
        server.send_message(msg)
        server.quit()
        print("✅ Đã gửi email báo cáo.")
    except Exception as e:
        print("❌ Lỗi gửi email:", e)

# ESP32 gửi dữ liệu → chỉ ghi log
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    raw = data.get('sensor_data', '')

    try:
        parts = raw.split(',')
        ph = parts[0].split(':')[1]
        turb = parts[1].split(':')[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        latest_data['ph'] = ph
        latest_data['turb'] = turb
        latest_data['timestamp'] = timestamp

        with open('log.txt', 'a') as f:
            f.write(f"{timestamp},PH:{ph},TURB:{turb}\n")

        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Trang chính
@app.route('/')
def index():
    return render_template('index.html', data=latest_data)

# Trang dữ liệu bảng
@app.route('/data-page')
def data_page():
    data_rows = []
    if os.path.exists('log.txt'):
        try:
            with open('log.txt', 'r') as f:
                for line in f.readlines()[-20:]:
                    parts = line.strip().split(',')
                    timestamp = parts[0]
                    ph = parts[1].split(':')[1]
                    turb = parts[2].split(':')[1]
                    data_rows.append({
                        "timestamp": timestamp,
                        "ph": ph,
                        "turb": turb
                    })
        except Exception as e:
            print("❌ Lỗi đọc log.txt:", e)
    return render_template('data.html', data_rows=data_rows)

# Trang báo cáo
@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/download-log')
def download_log():
    if os.path.exists("log.txt"):
        return send_file('log.txt', as_attachment=True)
    return "Không có file log.txt để tải về."

# Trang liên hệ
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Chỉ gửi email khi người dùng ấn nút
@app.route('/send-email', methods=['POST'])
def send_email():
    send_email_report(latest_data['ph'], latest_data['turb'], latest_data['timestamp'])
    return redirect(url_for('index'))

# Chạy app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
