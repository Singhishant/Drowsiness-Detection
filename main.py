import cv2
import mediapipe as mp
import numpy as np
import pygame
from utils import eye_aspect_ratio, mouth_aspect_ratio

# Initialize alarm
pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")

# Thresholds
EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.7
FRAME_THRESHOLD = 20

COUNTER = 0

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Landmark indexes
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [78, 81, 13, 311, 308, 402, 14, 178, 88, 95, 185, 40]

# Start webcam
cap = cv2.VideoCapture(0)

def get_landmarks(face_landmarks, indexes, w, h):
    points = []
    for i in indexes:
        x = int(face_landmarks.landmark[i].x * w)
        y = int(face_landmarks.landmark[i].y * h)
        points.append((x, y))
    return np.array(points)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            left_eye = get_landmarks(face_landmarks, LEFT_EYE, w, h)
            right_eye = get_landmarks(face_landmarks, RIGHT_EYE, w, h)
            mouth = get_landmarks(face_landmarks, MOUTH, w, h)

            leftEAR = eye_aspect_ratio(left_eye)
            rightEAR = eye_aspect_ratio(right_eye)
            ear = (leftEAR + rightEAR) / 2.0

            mar = mouth_aspect_ratio(mouth)

            # Draw contours
            cv2.polylines(frame, [left_eye], True, (0,255,0), 1)
            cv2.polylines(frame, [right_eye], True, (0,255,0), 1)
            cv2.polylines(frame, [mouth], True, (255,0,0), 1)

            # Drowsiness detection
            if ear < EAR_THRESHOLD:
                COUNTER += 1

                if COUNTER >= FRAME_THRESHOLD:
                    cv2.putText(frame, "DROWSINESS ALERT!", (50,100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play()

            else:
                COUNTER = 0
                pygame.mixer.music.stop()

            # Yawning detection
            if mar > MAR_THRESHOLD:
                cv2.putText(frame, "YAWNING!", (50,150),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)

            # Display EAR & MAR
            cv2.putText(frame, f"EAR: {ear:.2f}", (450,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
            cv2.putText(frame, f"MAR: {mar:.2f}", (450,60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()