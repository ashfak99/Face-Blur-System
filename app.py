import streamlit as slt
from PIL import Image, ImageFilter
import io
import requests
from streamlit_lottie import st_lottie

slt.set_page_config(page_title="Face Blur Tool", layout="centered", page_icon="🔒")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_face_scan = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_VruVbv.json")

if "upload_clicked" not in slt.session_state:
    slt.session_state["upload_clicked"] = False

slt.markdown("""
    <h1 style='text-align: center; color: #E74C3C;'>🔒 Face Blur Privacy Tool</h1>
    <p style='text-align: center; color: #AAB7B8; font-size: 18px;'>
        Securely blur faces in your images before sharing them online.
    </p>
    <hr style='border: 1px solid #333;'>
    """, unsafe_allow_html=True)

slt.sidebar.title("⚙️ Configuration")
imageUser = slt.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
intensity = slt.sidebar.slider("Blur Intensity", 0, 100, 50)

if imageUser is not None:
    if slt.sidebar.button("Process Image", type="primary"):
        slt.session_state["upload_clicked"] = True

    if slt.session_state["upload_clicked"]:
        image = Image.open(imageUser)

        col1, col2 = slt.columns(2)

        with col1:
            slt.subheader("Original")
            slt.image(image, caption="Original Image", width="stretch")

        with col2:
            slt.subheader("Blurred Result")
            blur_radius = intensity / 5
            blurred_image = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
            
            slt.image(blurred_image, caption="Privacy Protected", width="stretch")

            buf = io.BytesIO()
            blurred_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            slt.download_button(
                label="📥 Download Image",
                data=byte_im,
                file_name="blurred_image.png",
                mime="image/png",
                use_container_width=True
            )
else:
    slt.session_state["upload_clicked"] = False
    
    c1, c2, c3 = slt.columns([1, 3, 1])
    
    with c2:
        if lottie_face_scan:
            st_lottie(lottie_face_scan, height=250, key="face_scan")
    
    slt.markdown("""
    <h3 style='text-align: center; color: #FDFEFE;'>👈 Ready to Secure?</h3>
    <p style='text-align: center; color: #BDC3C7;'>
        Upload an image from the sidebar to start the face blurring process.
    </p>
    """, unsafe_allow_html=True)

slt.sidebar.divider()
slt.sidebar.header("About Developer")

linkedin = '<a href="https://www.linkedin.com/in/ashfak-alam/" target="_blank" style="color: #E74C3C; text-decoration: none; font-weight: bold;">ASHFAK ALAM</a>'
slt.sidebar.markdown(f"Created by: {linkedin}", unsafe_allow_html=True)

link = '<a href="https://github.com/ashfak99" target="_blank" style="color: #E74C3C; text-decoration: none; font-weight: bold;">GITHUB</a>'
slt.sidebar.markdown(link, unsafe_allow_html=True)