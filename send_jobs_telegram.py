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
📅 20/09/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 POSTE 1 : NÉGOCIATEUR SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_negociateur = [
    {
        "titre": "Négociateur Telecom - Sites GSM Radio H/F",
        "entreprise": "LTd",
        "lieu": "Le Havre (76)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-telecom-sites-gsm-radio-h-f-at-ltd-3779233332"
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
        "titre": "Négociateur Telecom - Sites GSM Radio H/F (29)",
        "entreprise": "LTD International",
        "lieu": "Finistère (29)",
        "type": "CDI",
        "source": "LTD International",
        "lien": "https://www.ltd-international.com/annonces/negociateur-telecom-sites-gsm-radio-h-f-29/"
    },
    {
        "titre": "Négociateur Radio H/F",
        "entreprise": "France Travail",
        "lieu": "Gémenos (13)",
        "type": "CDI",
        "source": "France Travail",
        "lien": "https://candidat.francetravail.fr/offres/recherche/detail/174TJWZ"
    },
    {
        "titre": "Négociateurs Sites Déploiement Telecom (GSM) H/F",
        "entreprise": "M-TEAM",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "Talent.com",
        "lien": "https://fr.talent.com/view?id=8ef6c9714879"
    },
    {
        "titre": "Négociateur Telecom - Sites GSM Radio H/F (Intérim 8 mois)",
        "entreprise": "Bizmatch",
        "lieu": "France",
        "type": "Intérim",
        "source": "Bizmatch",
        "lien": "https://www.bizmatch.fr/job/negociateur-telecom-sites-gsm-radio-h-f-interim-8mois"
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
        "titre": "Toutes offres Négociateur Télécom (12 offres)",
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
    {
        "titre": "Toutes offres Négociateur de Sites Télécoms",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Option Carrière",
        "lien": "https://www.optioncarriere.com/emploi-negociateur-de-sites-telecoms.html"
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
        "titre": "Chef de Projet Déploiement Radio - Secteur Télécom F/H",
        "entreprise": "ALTEN France",
        "lieu": "France",
        "type": "CDI",
        "source": "ALTEN",
        "lien": "https://www.alten.fr/jobs/744000038876518-chef-de-projet-deploiement-radio-secteur-telecom-f-h/"
    },
    {
        "titre": "Chef de Projet Télécom / Radio",
        "entreprise": "AGH Consulting",
        "lieu": "Île-de-France",
        "type": "CDI/Freelance",
        "source": "Free-Work",
        "lien": "https://www.free-work.com/fr/tech-it/responsable-telecom/job-mission/chef-de-projet-telecom-radio"
    },
    {
        "titre": "Chef de Projet DI Radio F/H",
        "entreprise": "AGH Consulting",
        "lieu": "France",
        "type": "CDI",
        "source": "Talentdetection",
        "lien": "https://www.talentdetection.com/agh-consulting/offre-57993-b7udZS"
    },
    {
        "titre": "Chef de Projet Radio Télécom F/H",
        "entreprise": "Diverses entreprises",
        "lieu": "Grand Paris",
        "type": "CDI",
        "source": "Le Journal du Grand Paris des Talents",
        "lien": "https://emploi.lejournaldugrandparis.fr/poste/chef-de-projet-radio-telecom-f-h/"
    },
    {
        "titre": "Conducteur de Travaux Radio - Sites Neufs Radio Télécom",
        "entreprise": "AGH Consulting",
        "lieu": "Île-de-France",
        "type": "CDI/Freelance",
        "source": "Free-Work",
        "lien": "https://www.free-work.com/fr/tech-it/responsable-telecom/job-mission/conducteur-de-travaux-radio-sites-neufs-radio-telecom"
    },
    {
        "titre": "Toutes offres Chef de Projet Radio Télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=Chef+de+projet+Radio+T%C3%A9l%C3%A9com"
    },
    {
        "titre": "Toutes offres Chef de Projet Déploiement Télécom (10 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_chef-projet-deploiement-telecom.html"
    },
    {
        "titre": "Toutes offres Chef de Projet Télécom (+60 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_chef-de-projet-telecoms.html"
    },
    {
        "titre": "Toutes offres Chef de Projet Télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Jobijoba",
        "lien": "https://www.jobijoba.com/fr/emploi/Chef+de+projet+telecom"
    },
    {
        "titre": "Toutes offres Chef de Projet Télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Jooble",
        "lien": "https://fr.jooble.org/emploi-chef-de-projet-t%C3%A9l%C3%A9com"
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
• 10 annonces Chef de Projet Site Radio
• Sources : Indeed, LinkedIn, APEC, HelloWork, Jooble, France Travail, Talent.com, Bizmatch, LTD International, ALTEN, Free-Work, Talentdetection, Le Journal du Grand Paris, Option Carrière, Jobijoba

🔄 Relance ce script demain pour de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
