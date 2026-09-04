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
📅 04/09/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 POSTE 1 : NÉGOCIATEUR SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_negociateur = [
    {
        "titre": "Négociateur Telecom - Sites GSM Radio H/F",
        "entreprise": "LTd",
        "lieu": "Éleu-Dit-Leauwette (62)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-telecom-sites-gsm-radio-h-f-at-ltd-3779231295"
    },
    {
        "titre": "Négociateur Foncier (H/F) — toutes offres",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/negociateur-foncier-(h-f)-emplois"
    },
    {
        "titre": "Négociateur foncier — 42 offres",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Glassdoor",
        "lien": "https://www.glassdoor.fr/Emploi/france-n%C3%A9gociateur-foncier-emplois-SRCH_IL.0,6_KO7,26.htm"
    },
    {
        "titre": "Négociateur foncier — Paris",
        "entreprise": "Multiples entreprises",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-foncier-ville_paris-75000.html"
    },
    {
        "titre": "Négociateur Télécom — 22 offres",
        "entreprise": "VINCI, Akinext, Eiffage, ND-Ingénierie...",
        "lieu": "France (Paris, Nantes, Saint-Herblain...)",
        "type": "CDI/CDD",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=N%C3%A9gociateur+T%C3%A9l%C3%A9com"
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
        "titre": "Toutes offres Négociateur Telecom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Négociateur sites GSM — toutes offres",
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
        "titre": "Chef de Projet Déploiement Radio – Secteur Télécom H/F",
        "entreprise": "ALTEN",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "LinkedIn / ALTEN",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-%E2%80%93-secteur-t%C3%A9l%C3%A9com-h-f-at-alten-3345041097"
    },
    {
        "titre": "Chef de projet déploiement radio H/F",
        "entreprise": "TIBCO Telecoms",
        "lieu": "Rennes (35)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-h-f-at-tibco-telecoms-3554707489"
    },
    {
        "titre": "Chef de projet déploiement Radio Télécom F/H",
        "entreprise": "AGH Consulting",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "TalentDetection",
        "lien": "https://www.talentdetection.com/agh-consulting/offre-57993-O0MGPh"
    },
    {
        "titre": "Chef de Projet Radio Bouygues Télécom H/F",
        "entreprise": "ACASS",
        "lieu": "Lyon (69)",
        "type": "CDI",
        "source": "ACASS",
        "lien": "https://www.acass.fr/details-offre+d+emploi+en+cdi+chef+de+projet+radio+bouygues+telecom+h+f+sur+lyon+69-14672.html"
    },
    {
        "titre": "Chef de projet Radio Télécom F/H",
        "entreprise": "Le Grand Paris des talents",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "Journal du Grand Paris",
        "lien": "https://emploi.lejournaldugrandparis.fr/poste/chef-de-projet-radio-telecom-f-h/"
    },
    {
        "titre": "Chef de projet Télécom / Radio — Île-de-France",
        "entreprise": "AGH Consulting",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "Free-Work",
        "lien": "https://www.free-work.com/fr/tech-it/responsable-telecom/job-mission/chef-de-projet-telecom-radio"
    },
    {
        "titre": "Chef de projet Radio Télécom — toutes offres",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=Chef+de+projet+Radio+T%C3%A9l%C3%A9com"
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
        "titre": "Chef Projet Radio — 200+ offres",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-chef-projet-radio-emplois.html"
    },
    {
        "titre": "Chef de projet télécom — 60+ offres",
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

send(f"""━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ <b>Envoi terminé !</b>

📊 <b>Récapitulatif :</b>
• {len(jobs_negociateur)} annonces Négociateur Site Radio
• {len(jobs_cdp)} annonces Chef de Projet Site Radio
• Sources : Indeed, LinkedIn, APEC, HelloWork, Jooble, Glassdoor, ALTEN, ACASS, TalentDetection, Free-Work

🔄 Relance ce script demain pour de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
