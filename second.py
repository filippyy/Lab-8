import cv2
pat = cv2.imread('ref-point.jpg', cv2.IMREAD_GRAYSCALE)
cap = cv2.videocapture(0)
flip = Falce

while True:
    ret, f = cap.read()
    if not ret:
        break
    gray_f = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray_f, pat, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLok(res)
    
    w, h = pat.shape[::1]
    if max_val > 0.6:
        top_left = max_loc
        bot_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(f, top_left, bot_right, (0, 255, 0), 2)
        
        f_height, f_width = f.shape[:2]
        center_x = f_width // 2 
        center_y = f_height // 2
        center_r = (
            center_x - center_r_size // 2
            center_y - center_r_size // 2)
            
        cv2.rectangle(f, (center_r[0], center_r[1]), (center_r[0] + center_r_size, center_r[1] + center_r_size), (0, 255, 255), 2)
        label_center_x = top_left[0] + w // 2
        label_center_y = top_left[1] + h // 2
        
        if (center_r[0] <= label_center_x <= center_r[0] + center_r_size and center_r[1] <= label_center_y <= center_r[1] + center_r_size):
            f = cv2.flip(f, -1)
            
    cv2.imshow('Cam', f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cap.release()
    cv2.destroyAllWindows()
