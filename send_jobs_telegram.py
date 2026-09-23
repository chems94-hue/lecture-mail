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
📅 23/09/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 POSTE 1 : NÉGOCIATEUR SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_negociateur = [
    {
        "titre": "Négociateur Radio H/F (CDI)",
        "entreprise": "Extia Ingénierie",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emplois/80692692.html"
    },
    {
        "titre": "Négociateur Télécom H/F",
        "entreprise": "AGH Consulting",
        "lieu": "Bordeaux (33)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/entreprises/agh-consulting-80953.html"
    },
    {
        "titre": "Négociateur Sites Télécom (2 offres, dont Eiffage Énergie Systèmes)",
        "entreprise": "Diverses entreprises",
        "lieu": "France",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-n%C3%A9gociateur-sites-t%C3%A9l%C3%A9com-emplois.html"
    },
    {
        "titre": "Toutes les offres — Négociateur télécom (12 offres CDI/CDD/Intérim)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Toutes les offres — Négociateur télécom Paris",
        "entreprise": "Multiples entreprises",
        "lieu": "Paris (75)",
        "type": "Divers",
        "source": "HelloWork",
        "lien": "https://parisjob.com/paris-75000-emplois-negociateur-telecom.html"
    },
    {
        "titre": "Toutes les offres — Négociateur télécom (22 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Jobintree",
        "lien": "https://www.jobintree.com/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Toutes les offres — Négociateur foncier / négociatrice foncière (15 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/n%C3%A9gociateur-foncier-n%C3%A9gociatrice-fonci%C3%A8re-(h-f)-emplois"
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
        "titre": "Chef de Projet Accueil Radio Télécom H/F (CDI)",
        "entreprise": "AGH Consulting",
        "lieu": "Issy-les-Moulineaux (92)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emplois/28197916.html"
    },
    {
        "titre": "Chef de Projet Radio Réaménagement de Sites H/F (CDI)",
        "entreprise": "AGH Consulting",
        "lieu": "Nantes (44)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emplois/77729662.html"
    },
    {
        "titre": "Chef de Projet Télécom / Radio",
        "entreprise": "AGH Consulting",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "Free-Work",
        "lien": "https://www.free-work.com/fr/tech-it/responsable-telecom/job-mission/chef-de-projet-telecom-radio"
    },
    {
        "titre": "Conducteur de Travaux Radio — Sites Neufs Radio Télécom",
        "entreprise": "AGH Consulting",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "Free-Work",
        "lien": "https://www.free-work.com/fr/tech-it/responsable-telecom/job-mission/conducteur-de-travaux-radio-sites-neufs-radio-telecom"
    },
    {
        "titre": "Chef de Projet Déploiement Radio Télécom F/H",
        "entreprise": "AGH Consulting",
        "lieu": "France (Aix-en-Provence, Toulouse...)",
        "type": "CDI",
        "source": "TalentDetection",
        "lien": "https://talentdetection.com/agh-consulting/offre-57993-O0MGPh"
    },
    {
        "titre": "Chef de Projet DI Radio F/H",
        "entreprise": "AGH Consulting",
        "lieu": "France",
        "type": "CDI",
        "source": "TalentDetection",
        "lien": "https://www.talentdetection.com/agh-consulting/offre-57993-b7udZS"
    },
    {
        "titre": "Toutes les offres — Chef Projet Déploiement Télécom (141 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-chef-projet-d%C3%A9ploiement-t%C3%A9l%C3%A9com-emplois.html"
    },
    {
        "titre": "Toutes les offres — Chef de projet déploiement télécom (60 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_chef-projet-deploiement-telecom.html"
    },
    {
        "titre": "Toutes les offres — Chef de projet telecom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Jobijoba",
        "lien": "https://www.jobijoba.com/fr/emploi/Chef+de+projet+telecom"
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
• 7 annonces Négociateur Site Radio (dont 2 offres individuelles ciblées : Extia Paris, AGH Bordeaux)
• 9 annonces Chef de Projet Site Radio (dont 6 offres individuelles ciblées chez AGH Consulting)
• Sources : Indeed, HelloWork, LinkedIn, Jobintree, Free-Work, TalentDetection, Jobijoba
• AGH Consulting ressort comme le recruteur le plus actif sur les deux postes actuellement

🔄 Prochaine recherche automatique demain.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
