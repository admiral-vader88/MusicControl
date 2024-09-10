import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

def fingers_up(landmarks):
    # Thumb
    thumb_up = landmarks[4][0] > landmarks[3][0]
    # Other fingers
    fingers = [landmarks[i][1] < landmarks[i-2][1] for i in [8, 12, 16, 20]]
    return [thumb_up] + fingers

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip horizontally for natural (mirror-like) viewing
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            landmarks = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((cx, cy))
            
            if landmarks:
                # Volume Up: Thumb up
                if fingers_up(landmarks) == [True, False, False, False, False]:
                    pyautogui.press("volumeup")

                # Volume Down: Thumb down
                if landmarks[4][1] > landmarks[3][1] > landmarks[2][1]:
                    pyautogui.press("volumedown")
                
                # Play/Pause: Open hand
                if fingers_up(landmarks) == [True, True, True, True, True]:
                    pyautogui.press("playpause")

                # Next Track: Swipe right gesture (index and middle finger pointing)
                if fingers_up(landmarks) == [False, True, True, False, False]:
                    pyautogui.press("nexttrack")

                # Previous Track: Swipe left gesture (index and middle finger pointing)
                if fingers_up(landmarks) == [False, True, True, False, False]:
                    pyautogui.press("prevtrack")

    cv2.imshow("Hand Detection Music Controller", img)
    
    # Break loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
