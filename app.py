import streamlit as st
import cv2
import os
import tempfile
from face_shape_detector import get_face_shape
from recommender import recommend_haircuts

st.title("💇 AI Haircut Recommendation System")

st.write("Upload a photo or take one with your webcam to get started.")

# Upload or capture image
upload_option = st.radio("Choose image input method:", ("Upload Image", "Use Webcam"))

def capture_image_from_webcam():
    cam = cv2.VideoCapture(0)
    st.info("Press 's' to capture your photo.")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Press 's' to capture photo", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_path = "captured_face.jpg"
            cv2.imwrite(img_path, frame)
            cam.release()
            cv2.destroyAllWindows()
            return img_path

if upload_option == "Upload Image":
    uploaded = st.file_uploader("Upload a face photo", type=['jpg', 'png', 'jpeg'])
    if uploaded:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded.read())
            img_path = tmp.name
else:
    if st.button("Start Webcam"):
        img_path = capture_image_from_webcam()

# If we have an image, detect face shape
if 'img_path' in locals():
    st.image(img_path, caption="Your photo", use_column_width=True)
    shape = get_face_shape(img_path)

    if shape:
        st.success(f"Detected Face Shape: **{shape}**")

        # Collect user preferences
        st.header("🧑 Personalize Your Style")

        gender = st.selectbox("Gender", ["male", "female"])
        hair_type = st.selectbox("Hair Type", ["straight", "wavy", "curly"])
        style_pref = st.selectbox("Preferred Style", ["professional", "casual", "edgy"])
        short_hair_ok = st.radio("Okay with short hair?", ["yes", "no"]) == "yes"

        if st.button("Get Haircut Suggestions"):
            prefs = {
                "gender": gender,
                "hair_type": hair_type,
                "style_pref": style_pref,
                "short_hair_ok": short_hair_ok
            }
            results = recommend_haircuts(shape, prefs)

            st.subheader("✂️ Recommended Haircuts:")
            for r in results:
                st.markdown(f"- {r}")
    else:
        st.error("No face detected in the photo. Please try another image.")
