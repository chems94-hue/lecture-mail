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
📅 04/06/2026

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
        "titre": "Négociateur de Site Radio",
        "entreprise": "Diverses entreprises",
        "lieu": "France",
        "type": "CDI",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=N%C3%89GOCIATEUR+DE+SITE+RADIO"
    },
    {
        "titre": "Négociateur Télécom",
        "entreprise": "VINCI, Akinext, Eiffage, ND-Ingénierie",
        "lieu": "France (Paris, Nantes, Saint-Herblain...)",
        "type": "CDI/CDD",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=N%C3%A9gociateur+T%C3%A9l%C3%A9com"
    },
    {
        "titre": "Concepteur Télécom F/H",
        "entreprise": "Eiffage Énergie Systèmes",
        "lieu": "Toulouse (31)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aat9kb4jmyg9"
    },
    {
        "titre": "Toutes offres Négociateur Telecom Mobile",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-negociateur-sites-telecom-mobile-emplois.html"
    },
    {
        "titre": "Toutes offres Négociateur Telecom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-telecom.html"
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
        "titre": "Chef de Projet Déploiement H/F",
        "entreprise": "NRJ AUDIO",
        "lieu": "Vénissieux (69)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aabfgctwg626"
    },
    {
        "titre": "Ingénieur Réseau Projet H/F",
        "entreprise": "Seaowl Technology Solutions",
        "lieu": "Ollioules (83)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aal98jmf2hxm"
    },
    {
        "titre": "Conducteur de Travaux Radio H/F",
        "entreprise": "ENSIO",
        "lieu": "Flins-sur-Seine (78)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aas6c9txv667"
    },
    {
        "titre": "Ingénieur Senior Telecom - Oil & Gas H/F",
        "entreprise": "NEO2",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aaq69xslh9y8"
    },
    {
        "titre": "Chef de Projet Radio Télécom",
        "entreprise": "Diverses entreprises",
        "lieu": "France",
        "type": "CDI",
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
        "titre": "241 offres — Chef de Projet Telecom F/H",
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
• 6 annonces Négociateur Site Radio
• 9 annonces Chef de Projet Site Radio
• Sources : Indeed, LinkedIn, APEC, HelloWork, Jooble

🔄 Relance ce script demain pour de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
