import streamlit as st
import cv2
import numpy as np

st.title("📷 Affichage de la caméra en direct")

# Démarrer la capture vidéo (0 = caméra par défaut)
cap = cv2.VideoCapture(0)

# Créer un bouton pour démarrer l'affichage
start = st.button("Démarrer la caméra")

# Zone pour afficher la vidéo
frame_placeholder = st.empty()

# Boucle d'affichage si bouton activé
if start:
    st.info("Appuyez sur 'Stop' pour arrêter la caméra")
    stop = st.button("Stop")

    while cap.isOpened() and not stop:
        ret, frame = cap.read()
        if not ret:
            st.warning("Impossible de lire la vidéo.")
            break

        # Convertir l'image de BGR (OpenCV) à RGB (Streamlit)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Afficher l'image dans Streamlit
        frame_placeholder.image(frame, channels="RGB")

    cap.release()
    st.success("Caméra arrêtée.")

