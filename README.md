# AI Hand Gesture Music Controller
This Python script uses OpenCV, MediaPipe, and PyAutoGUI to create a hand gesture-based music controller, enabling users to control media playback and volume by performing hand gestures detected through a webcam.

Key Components:
MediaPipe Hands Detection:

Utilizes MediaPipe's hand-tracking solution to detect and track a single hand in real-time with a minimum detection confidence of 0.7.
Detects hand landmarks (positions of key points on the hand) and draws the connections between them using mp.solutions.drawing_utils.
Hand Gesture Recognition:

A function fingers_up(landmarks) determines which fingers are extended based on the positions of landmarks.
The script recognizes several hand gestures based on the orientation of the thumb and fingers:
Volume Up: Thumb up (thumb pointing right in the image).
Volume Down: Thumb down (thumb pointing downwards).
Play/Pause: All fingers open (full hand open).
Next Track: Swipe right gesture (index and middle fingers extended).
Previous Track: Swipe left gesture (index and middle fingers extended).
PyAutoGUI:

Controls media playback by sending system keyboard commands (volumeup, volumedown, playpause, nexttrack, prevtrack) based on the recognized hand gestures.
Webcam Input:

Captures video from the default webcam using cv2.VideoCapture(0), flips it horizontally for a natural mirror effect, and processes each frame in real-time.
Main Loop:

The loop runs continuously, capturing and processing frames until the user presses the 'q' key to exit.
This script provides an intuitive and interactive way to control media using hand gestures, making it hands-free and user-friendly.






