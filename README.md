
Markdown
# 🔒 Face Blur Privacy Tool

![Python](https://img.shields.io/badge/Python-3.11.9-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0099CC?style=for-the-badge)

A secure and user-friendly web application designed to protect privacy by detecting and blurring faces in images. Built with **Streamlit**, **OpenCV**, and **MediaPipe**, this tool allows users to upload images, adjust blur intensity, and download the processed results instantly.

---

## 📸 Features

-   **Automatic Face Detection:** Uses Google's MediaPipe for high-precision face detection.
-   **Adjustable Privacy Levels:** Control the pixelation/blur intensity using a simple slider.
-   **Real-time Preview:** View "Original" vs "Privacy Protected" images side-by-side.
-   **Secure Processing:** Images are processed in memory and not stored permanently.
-   **One-Click Download:** Easily download the sanitized image in PNG format.
-   **Responsive UI:** Clean interface with Lottie animations for a modern look.

---

## 🛠️ Tech Stack

-   **Frontend:** Streamlit
-   **Image Processing:** OpenCV (cv2), NumPy, Pillow (PIL)
-   **AI Model:** MediaPipe Face Detection
-   **Utilities:** Requests (for Lottie animations)

---

## 📂 Project Structure

Ensure your project folder is organized like this:

```text
Face-Blur-Tool/
│
├── app.py              # Main Streamlit application code
├── processor.py        # Logic for Face Detection and Blurring
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
🚀 Installation & Setup
Follow these steps to run the project locally.```

## 1. Clone the Repository
Bash
git clone [https://github.com/ashfak99/Face-Blur-Tool.git](https://github.com/ashfak99/Face-Blur-Tool.git)
cd Face-Blur-Tool
2. Set up a Virtual Environment (Recommended)
Target Python Version: 3.11.9

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Create a requirements.txt file with the contents below, then run the install command.

requirements.txt content:

Plaintext
streamlit
opencv-python
mediapipe
numpy
Pillow
requests
streamlit-lottie
Install command:

Bash
pip install -r requirements.txt
4. Run the Application
Bash
streamlit run app.py
🧩 How to Use
Launch the app using the command above.

Upload an image (JPG, JPEG, PNG) from the sidebar.

Adjust the "Blur Intensity" slider (0 to 100).

Click the "Process Image" button.

Wait for the AI to detect faces.

Preview the result and click "Download Image" to save it.

👨‍💻 Developer
Created by Ashfak Alam

LinkedIn Profile

GitHub Profile

📜 License
This project is open-source and available for educational purposes.


### Note for you (Developer):
Code structure ko sahi karne ke liye, ensure karein ki aapke paas folder mein 2 files alag-alag hon:

1.  **`app.py`**: Isme wo code dalein jo `import streamlit as slt` se shuru hota hai.
2.  **`processor.py`**: Isme wo code dalein jo `import cv2` aur `def detectAndBlur...` contain karta hai.

Agar aapne abhi tak files alag nahi ki hain, to `app.py` ke top par `from processor import detectAndBlur` line tabhi kaam karegi jab `processor.py` file same folder mein existing hogi.