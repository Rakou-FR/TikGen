import cv2

def zoom_9_16(chemin_entree, chemin_sortie):
    try:
        # Charger la vidéo
        cap = cv2.VideoCapture(chemin_entree)

        # Récupérer les dimensions originales de la vidéo
        largeur_orig = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        hauteur_orig = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Calculer les nouvelles dimensions pour le format 9:16
        nouvelle_hauteur = hauteur_orig
        nouvelle_largeur = int(9 / 16 * hauteur_orig)

        # Déterminer les coordonnées de la région à zoomer
        x1 = (largeur_orig - nouvelle_largeur) // 2
        y1 = 0
        x2 = x1 + nouvelle_largeur
        y2 = hauteur_orig

        # Créer un objet VideoWriter pour sauvegarder la vidéo zoomée
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(chemin_sortie, fourcc, 30.0, (nouvelle_largeur, nouvelle_hauteur))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Recadrer et redimensionner le frame
            frame_zoom = frame[y1:y2, x1:x2]
            frame_zoom = cv2.resize(frame_zoom, (nouvelle_largeur, nouvelle_hauteur))

            # Écrire le frame dans la nouvelle vidéo
            out.write(frame_zoom)

        # Libérer les ressources
        cap.release()
        out.release()
        return True
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False
    

zoom_9_16("test.mp4", "testt.mp4")
