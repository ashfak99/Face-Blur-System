import cv2
import mediapipe as mp

# Setup MediaPipe
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# 1. Image path specify karein
IMAGE_PATH = '14ash.jpg' 

# 2. Image ko load karein
image = cv2.imread(IMAGE_PATH)

# Check karein agar image sahi se load hui
if image is None:
    print("Error: Image nahi mili! Path check karein.")
else:
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        
        # BGR ko RGB mein convert karein
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 3. Model se face detect karwayein
        results = face_detection.process(image_rgb)

        # 4. Agar face mila, toh uspar drawing karein
        if results.detections:
            print(f"Total {len(results.detections)} face(s) mile!")
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
        
        # --- NEW CODE: IMAGE RESIZE (Taaki screen par fit aaye) ---
        
        # Image ki current height aur width nikalein
        h, w, c = image.shape
        
        # Agar image ki choudai (width) 1000 pixel se zyada hai, tabhi chhota karein
        if w > 1000:
            new_width = 500  # Hum width ko 1000 fix kar dete hain
            aspect_ratio = 1000 / float(w)
            new_height = int(h * aspect_ratio) # Height apne aap adjust hogi
            image = cv2.resize(image, (new_width, new_height))
        
        # ----------------------------------------------------------

        # Output dikhayein
        cv2.imshow('Face Detection Result', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()