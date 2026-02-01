
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
├── app.py              
├── processor.py        
├── requirements.txt    
└── README.md         

```

---

## 🚀 Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/ashfak99/Face-Blur-System.git
cd Face-Blur-System

```

### 2. Set up a Virtual Environment (Recommended)

Target Python Version: **3.11.9**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

Create a `requirements.txt` file with the contents below, then run the install command.

**requirements.txt content:**

```text
streamlit
opencv-python
mediapipe
numpy
Pillow
requests
streamlit-lottie

```

**Install command:**

```bash
pip install -r requirements.txt

```

### 4. Run the Application

```bash
streamlit run app.py

```

---

## 🧩 How to Use

1. **Launch** the app using the command above.
2. **Upload** an image (JPG, JPEG, PNG) from the sidebar.
3. **Adjust** the "Blur Intensity" slider (0 to 100).
4. Click the **"Process Image"** button.
5. Wait for the AI to detect faces.
6. **Preview** the result and click **"Download Image"** to save it.

---

## 👨‍💻 Developer

Created by **Ashfak Alam**

* [LinkedIn Profile](https://www.linkedin.com/in/ashfak-alam/)
* [GitHub Profile](https://github.com/ashfak99)

---

## 📜 License

This project is open-source and available for educational purposes.

