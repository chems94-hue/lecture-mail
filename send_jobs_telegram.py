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
📅 04/07/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 POSTE 1 : NÉGOCIATEUR SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_negociateur = [
    {
        "titre": "Négociateur Radio H/F",
        "entreprise": "Extia Ingénierie",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emplois/80692692.html"
    },
    {
        "titre": "Négociateur Telecom - Sites GSM Radio H/F",
        "entreprise": "LTd",
        "lieu": "Éleu-Dit-Leauwette (62)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-telecom-sites-gsm-radio-h-f-at-ltd-3779231295"
    },
    {
        "titre": "Négociateur Telecom - Sites GSM Radio H/F",
        "entreprise": "LTd",
        "lieu": "Le Havre (76)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-telecom-sites-gsm-radio-h-f-at-ltd-3779233332"
    },
    {
        "titre": "Négociateur de Sites Radio H/F",
        "entreprise": "VPI Telecom",
        "lieu": "Paris, Île-de-France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-de-sites-radio-h-f-at-vpi-telecom-3329554722"
    },
    {
        "titre": "Toutes offres — Négociateur Radio H/F (84 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/n%C3%A9gociateur-radio-h-f-emplois"
    },
    {
        "titre": "Toutes offres — Négociateur de Site Télécom (9 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/n%C3%A9gociateur-de-site-t%C3%A9l%C3%A9com-(h-f)-emplois"
    },
    {
        "titre": "Toutes offres — Négociateur de Sites Télécoms",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Option Carrière",
        "lien": "https://www.optioncarriere.com/emploi-negociateur-de-sites-telecoms.html"
    },
    {
        "titre": "Toutes offres — Négociateur de Site Radio",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=N%C3%89GOCIATEUR+DE+SITE+RADIO"
    },
    {
        "titre": "Toutes offres — Négociateur Télécom (22 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Toutes offres — Négociateur Sites Telecom Mobile",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-negociateur-sites-telecom-mobile-emplois.html"
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
        "titre": "Chef de Projet Déploiement H/F/NB",
        "entreprise": "NRJ AUDIO",
        "lieu": "Vénissieux (69)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aa2rmn4l96cl"
    },
    {
        "titre": "Responsable Adjoint Travaux Sud Ouest H/F",
        "entreprise": "NRJ AUDIO",
        "lieu": "Toulouse (31)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aa6pzmpdtwrb"
    },
    {
        "titre": "Conducteur de Travaux Radio H/F",
        "entreprise": "ENSIO",
        "lieu": "Flins-sur-Seine (78)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aagkbltrxcx9"
    },
    {
        "titre": "Ingénieur Senior en Telecommunication - Projet EPC Oil & Gas H/F",
        "entreprise": "NEO2",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aak7brmjy9lp"
    },
    {
        "titre": "Chef de Projet Déploiement Radio – Secteur Télécom H/F",
        "entreprise": "ALTEN",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-%E2%80%93-secteur-t%C3%A9l%C3%A9com-h-f-at-alten-3302661556/"
    },
    {
        "titre": "Chef de Projet Déploiement Radio Télécom F/H",
        "entreprise": "AGH Consulting",
        "lieu": "France",
        "type": "CDI",
        "source": "Talentdetection",
        "lien": "https://www.talentdetection.com/agh-consulting/offre-57993-O0MGPh"
    },
    {
        "titre": "Chef de Projet Infrastructure Réseaux Télécom F/H",
        "entreprise": "Ministère de l'Europe et des Affaires Étrangères",
        "lieu": "France",
        "type": "CDI",
        "source": "Diplomatie.gouv.fr",
        "lien": "https://emplois.diplomatie.gouv.fr/nos-offres/28f1624f-0c91-47a6-9faa-6c5bf57e714c"
    },
    {
        "titre": "Toutes offres — Chef de Projet Radio Télécom",
        "entreprise": "Diverses entreprises",
        "lieu": "France",
        "type": "CDI",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=Chef+de+projet+Radio+T%C3%A9l%C3%A9com"
    },
    {
        "titre": "Toutes offres — Chef Projet Telecom (800+ offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-chef-projet-telecom-emplois.html"
    },
    {
        "titre": "Toutes offres — Chef de Projet Telecom F/H",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/chef-de-projet-telecom-f-h-emplois"
    },
    {
        "titre": "Chef Projet Déploiement Telecom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Jooble",
        "lien": "https://fr.jooble.org/emploi-chef-projet-deploiement-telecom"
    },
    {
        "titre": "Chef de projet télécom — +70 offres",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_chef-de-projet-telecoms.html"
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
• 10 annonces Négociateur Site Radio
• 11 annonces Chef de Projet Site Radio
• Sources : Indeed, LinkedIn, APEC, HelloWork, Jooble, Option Carrière, Talentdetection, Diplomatie.gouv.fr

🔄 Relance ce script demain pour de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
