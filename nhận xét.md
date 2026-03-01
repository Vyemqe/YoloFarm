# Nhận xét ngày 1 tháng 3 – Bạn Nguyen Quan

## Nội dung nhận xét

**Publish (gửi dữ liệu cảm biến lên Adafruit IO) chưa được thực hiện.**

Trong toàn bộ mã nguồn hiện tại không có đoạn code nào gọi `publish` (hoặc API tương đương của Adafruit IO) để gửi dữ liệu cảm biến từ Gateway lên feed. README có mô tả phần "Sending data programming: from Gateway to Feed" nhưng chức năng này chưa được triển khai trong code. Cần bổ sung logic Publish (ví dụ: đọc dữ liệu cảm biến và gửi lên các feed tương ứng trên Adafruit IO) để hoàn thiện logic kết nối Gateway theo Chương 3 & 4.

---

# Nhận xét ngày 1 tháng 3 – Bạn Thanh Huy

## Nội dung nhận xét

**Nhiệm vụ: Xử lý logic tại Gateway và giả lập dữ liệu — chưa làm đủ.**

1. **Module xử lý logic "Vượt ngưỡng"**  
   Đã có kiểm tra ngưỡng (ví dụ `temp > 37` trong `temperature_handler.py`) nhưng chỉ ghi log cảnh báo, **chưa** tự động tạo và gửi lệnh điều khiển xuống thiết bị (ví dụ bật/tắt bơm qua MQTT khi vượt ngưỡng). Cần bổ sung bước: khi dữ liệu cảm biến vượt ngưỡng → publish lệnh điều khiển xuống feed thiết bị tương ứng.

2. **Script giả lập dữ liệu cảm biến**  
   Chưa có script nào sinh dữ liệu cảm biến giả và đẩy lên Server/Adafruit IO (trong lúc chờ thiết bị thật). Cần viết script giả lập (ví dụ nhiệt độ, độ ẩm) để người nhận thiết bị có dữ liệu đẩy lên Server và test luồng end-to-end.
