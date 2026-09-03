import requests

BOT_TOKEN = "7487820475:AAHl1heNbkQAoHiTgedn8x2oQuZpKX6aMK0"
CHAT_ID = "968964130"
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
📅 03/09/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 POSTE 1 : NÉGOCIATEUR SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_negociateur = [
    {
        "titre": "Négociateur de Sites Télécom",
        "entreprise": "AGH Consulting",
        "lieu": "Lyon (69)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emplois/69883370.html"
    },
    {
        "titre": "Négociateur de Sites Télécoms Radio",
        "entreprise": "AGH Consulting",
        "lieu": "Bordeaux (33)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emplois/70774660.html"
    },
    {
        "titre": "Négociateur de Sites Télécom Radio",
        "entreprise": "AGH Consulting",
        "lieu": "Lyon 3e (69)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emplois/51736014.html"
    },
    {
        "titre": "Toutes offres Négociateur Sites Télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-n%C3%A9gociateur-sites-t%C3%A9l%C3%A9com-emplois.html"
    },
    {
        "titre": "Toutes offres Négociateur de Site Radio",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=N%C3%89GOCIATEUR+DE+SITE+RADIO"
    },
    {
        "titre": "22 offres — Négociateur Télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Jobintree",
        "lien": "https://www.jobintree.com/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "12 offres — Négociateur Télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Toutes offres Négociateur Sites GSM",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Jooble",
        "lien": "https://fr.jooble.org/emploi-n%C3%A9gociateur-sites-gsm"
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
        "titre": "Chef de projet Télécom / Radio",
        "entreprise": "AGH Consulting",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "Free-Work",
        "lien": "https://www.free-work.com/fr/tech-it/responsable-telecom/job-mission/chef-de-projet-telecom-radio"
    },
    {
        "titre": "Chef de projet déploiement Radio Télécom F/H",
        "entreprise": "AGH Consulting",
        "lieu": "France",
        "type": "CDI",
        "source": "TalentDetection",
        "lien": "https://talentdetection.com/agh-consulting/offre-57993-O0MGPh"
    },
    {
        "titre": "Chef de Projet Déploiement Radio – Secteur Télécom (F/H)",
        "entreprise": "ALTEN France",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "ALTEN",
        "lien": "https://www.alten.fr/jobs/744000038876518-chef-de-projet-deploiement-radio-secteur-telecom-f-h/"
    },
    {
        "titre": "Chef de projet Radio Télécom F/H",
        "entreprise": "Grand Paris des Talents",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "Le Journal du Grand Paris",
        "lien": "https://emploi.lejournaldugrandparis.fr/poste/chef-de-projet-radio-telecom-f-h/"
    },
    {
        "titre": "Chef de projet radio télécoms H/F",
        "entreprise": "Mercato de l'Emploi",
        "lieu": "France",
        "type": "CDI",
        "source": "Mercato de l'Emploi",
        "lien": "https://mercato-emploi.com/annonce/chef-de-projet-radio-telecoms-h-f/"
    },
    {
        "titre": "Chef de Projet Déploiement Télécom RADIO (H/F)",
        "entreprise": "Ad-Vantage",
        "lieu": "France",
        "type": "CDI",
        "source": "Ad-Vantage",
        "lien": "https://www.ad-vantage.fr/recrutement/chef-de-projet-deploiement-telecom-radio-hf/"
    },
    {
        "titre": "206 offres — Chef Projet Radio",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-chef-projet-radio-emplois.html"
    },
    {
        "titre": "43 offres — Chef de Projet Déploiement Radio",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/chef-de-projet-deploiement-radio-emplois/"
    },
    {
        "titre": "60+ offres — Chef de projet télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_chef-de-projet-teleoms.html"
    },
    {
        "titre": "Chef projet déploiement télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Jooble",
        "lien": "https://fr.jooble.org/emploi-chef-projet-deploiement-telecom"
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
• 10 annonces Chef de Projet Site Radio
• Sources : Indeed, LinkedIn, APEC, HelloWork, Jooble, Free-Work, ALTEN, Mercato, Ad-Vantage, Jobintree

🔄 Relance ce script demain pour de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
