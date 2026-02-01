import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def detectAndBlur(uploaded_file,intensity):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes,1)

    if image is None:
        print("Error: Image nahi mili! Path check karein.")
        return
    
    h, w, c = image.shape

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        results = face_detection.process(image_rgb)

        if results.detections:
            faceCount=len(results.detections)
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                
                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                width = int(bbox.width * w)
                height = int(bbox.height * h)

                x = max(0, x)
                y = max(0, y)
                width = min(width, w - x)
                height = min(height, h - y)

                face_roi = image[y : y+height, x : x+width]

                pixelSize=max(5,100-intensity-40)

                try:
                    small = cv2.resize(face_roi, (pixelSize, pixelSize), interpolation=cv2.INTER_LINEAR)
                    pixelated = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)
                    image[y:y+height, x:x+width] = pixelated
                except Exception as e:
                    print(f"Error: {e}")
                
            return image,faceCount
        else:
            return image,0
        
        # if w > 1000:
        #     new_width = 500
        #     aspect_ratio = new_width / float(w)
        #     new_height = int(h * aspect_ratio)
        #     image = cv2.resize(image, (new_width, new_height))
