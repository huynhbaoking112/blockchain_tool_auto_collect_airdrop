import pyautogui
import time
import keyboard  # Thư viện để theo dõi phím

# Đặt thời gian chờ trước khi thực hiện click
time.sleep(2)

# Vị trí click trên màn hình (x, y)
x, y = 1174, 574  # Cập nhật tọa độ phù hợp với màn hình của bạn

# Lặp lại hành động click trong một khoảng thời gian hoặc dừng khi nhấn phím "c"
click_count = 0
while click_count < 300:  # Số lần click tối đa
    if keyboard.is_pressed('c'):  # Kiểm tra nếu phím 'c' được nhấn
        print("Dừng click vì phím 'C' đã được nhấn.")
        break  # Dừng vòng lặp nếu nhấn phím 'c'
    
    # pyautogui.click(x, y)  # Click vào tọa độ (x, y)
    pyautogui.mouseDown(x=x, y=y)  # Mô phỏng nhấn chuột tại tọa độ (x, y)
    pyautogui.mouseUp(x=x, y=y)    # Mô phỏng thả chuột tại tọa độ (x, y)
    print(f"Đã click lần {click_count + 1}")
    click_count += 1
    time.sleep(0)  # Chờ 1 giây trước khi click lại

# import pyautogui
# import time

# # Lặp vô hạn để liên tục in ra vị trí chuột
# while True:
#     x, y = pyautogui.position()  # Lấy tọa độ (x, y) của chuột
#     print(f"Vị trí chuột hiện tại: ({x}, {y})", end='\r')  # In vị trí mà không xuống dòng mới
#     time.sleep(0.1)  # Chờ 0.1 giây để giảm bớt việc in liên tục