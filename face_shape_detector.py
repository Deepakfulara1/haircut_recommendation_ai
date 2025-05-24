import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)
mp_drawing = mp.solutions.drawing_utils

def get_face_shape(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    results = face_mesh.process(rgb_image)

    if not results.multi_face_landmarks:
        print("No face detected.")
        return None

    landmarks = results.multi_face_landmarks[0].landmark
    points = [(int(lm.x * width), int(lm.y * height)) for lm in landmarks]

    # Key landmarks for face shape estimation
    forehead = points[10]
    chin = points[152]
    left_cheek = points[234]
    right_cheek = points[454]
    jaw_left = points[130]
    jaw_right = points[359]

    # Distances
    face_length = np.linalg.norm(np.array(forehead) - np.array(chin))
    face_width = np.linalg.norm(np.array(left_cheek) - np.array(right_cheek))
    jaw_width = np.linalg.norm(np.array(jaw_left) - np.array(jaw_right))

    # Ratio-based face shape determination (simplified)
    if face_width / face_length > 0.9:
        return "Round"
    elif face_length > face_width * 1.3:
        return "Oval"
    elif jaw_width > face_width * 0.95:
        return "Square"
    else:
        return "Heart"

# For testing: capture image from webcam and run shape detection
if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    print("Capturing photo. Press 's' to save.")
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("Press 's' to capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_path = "captured_face.jpg"
            cv2.imwrite(img_path, frame)
            cam.release()
            cv2.destroyAllWindows()
            shape = get_face_shape(img_path)
            print(f"Detected Face Shape: {shape}")
            break
