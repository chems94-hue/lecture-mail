import os
import sys

import requests

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    sys.exit(
        "Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID environment variables before running this script."
    )

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send(text):
    requests.post(BASE_URL, json={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    })

# ─── NÉGOCIATEUR SITE RADIO TELECOM ───────────────────────────────────────────

send("""🔍 <b>RECHERCHE EMPLOI — RÉSULTATS DU JOUR</b>
📅 11/11/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 POSTE 1 : NÉGOCIATEUR SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_negociateur = [
    {
        "titre": "Négociateur Radio Télécom F/H",
        "entreprise": "Commercial (H/F)",
        "lieu": "Boulogne-Billancourt (92)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5654081"
    },
    {
        "titre": "Négociateur de sites télécoms Radio DI F/H",
        "entreprise": "Commercial (H/F)",
        "lieu": "Versailles (78)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5651471"
    },
    {
        "titre": "Négociateur de Sites Radio F/H",
        "entreprise": "Commercial (H/F)",
        "lieu": "Lyon 01 (69)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5700239"
    },
    {
        "titre": "Négociateur Télécom H/F",
        "entreprise": "Commercial (H/F)",
        "lieu": "Vénissieux (69)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5783435"
    },
    {
        "titre": "Négociateur Telecom H/F",
        "entreprise": "Commercial (H/F)",
        "lieu": "Saint-Herblain (44)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5177606"
    },
    {
        "titre": "Négociateur Télécom Radio (Sites neufs) F/H",
        "entreprise": "Commercial (H/F)",
        "lieu": "Nantes (44)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5228620"
    },
    {
        "titre": "Negociateur Telecom F/H",
        "entreprise": "Commercial (H/F)",
        "lieu": "Nice (06)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5651598"
    },
    {
        "titre": "Chargé d'Affaires GSM / Radio H/F",
        "entreprise": "LTd",
        "lieu": "France",
        "type": "CDI",
        "source": "Engagement Jeunes",
        "lien": "https://www.engagement-jeunes.com/fr/detail-offre/38566153/cdi-ltd-charge-d-affaires-gsm-radio-h-f.html"
    },
]

for i, job in enumerate(jobs_negociateur, 1):
    send(f"""📌 <b>{i}. {job['titre']}</b>
🏢 {job['entreprise']}
📍 {job['lieu']}
📄 {job['type']} — {job['source']}
🔗 <a href="{job['lien']}">Voir l'offre</a>""")

# ─── CHEF DE PROJET SITE RADIO TELECOM ────────────────────────────────────────

send("""━━━━━━━━━━━━━━━━━━━━━━━━━━
🔵 POSTE 2 : CHEF DE PROJET SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_cdp = [
    {
        "titre": "Chef/Cheffe de projet GSM H/F",
        "entreprise": "Diverses entreprises",
        "lieu": "Juvisy-sur-Orge (91)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/6105608"
    },
    {
        "titre": "Chef de Projet Radio H/F",
        "entreprise": "Diverses entreprises",
        "lieu": "Saint-Denis (93)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5331639"
    },
    {
        "titre": "Chef de projet Radio F/H",
        "entreprise": "Diverses entreprises",
        "lieu": "Cuincy (59)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5647665"
    },
    {
        "titre": "Chef/cheffe de projet Fibre RADIO H/F",
        "entreprise": "Diverses entreprises",
        "lieu": "Saint-Germain-en-Laye (78)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5627738"
    },
    {
        "titre": "Chef/cheffe de projet Fibre RADIO H/F",
        "entreprise": "Diverses entreprises",
        "lieu": "Chelles (77)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5627914"
    },
    {
        "titre": "Chef de Projet Radio H/F",
        "entreprise": "Diverses entreprises",
        "lieu": "Vitrolles (13)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/5661603"
    },
    {
        "titre": "Chef de Projet Télécom Radio (sites mobiles)",
        "entreprise": "AGH Consulting",
        "lieu": "Clermont-Ferrand (63)",
        "type": "Freelance",
        "source": "Free-Work",
        "lien": "https://www.free-work.com/fr/tech-it/job-mission/responsable-telecom/chef-de-projet-telecom-radio-1"
    },
    {
        "titre": "Consultant Chef de Projet Déploiement Réseaux Mobiles Indoor F/H",
        "entreprise": "Orange SA",
        "lieu": "France",
        "type": "CDI",
        "source": "Engagement Jeunes",
        "lien": "https://www.engagement-jeunes.com/fr/detail-offre/39405511/cdi-orange-sa-consultant-chef-de-projet-deploiement-de-reseaux-mobiles-indoor-f-h.html"
    },
]

for i, job in enumerate(jobs_cdp, 1):
    send(f"""📌 <b>{i}. {job['titre']}</b>
🏢 {job['entreprise']}
📍 {job['lieu']}
📄 {job['type']} — {job['source']}
🔗 <a href="{job['lien']}">Voir l'offre</a>""")

# ─── MESSAGE DE FIN ────────────────────────────────────────────────────────────

send("""━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ <b>Envoi terminé !</b>

📊 <b>Récapitulatif :</b>
• 8 annonces Négociateur Site Radio
• 8 annonces Chef de Projet Site Radio
• Sources : France Travail, Free-Work, Engagement Jeunes

🔄 Relance ce script demain pour de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
