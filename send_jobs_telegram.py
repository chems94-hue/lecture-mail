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

# ─── HEADER ───────────────────────────────────────────────────────────────────

send("""🔍 <b>RECHERCHE EMPLOI — RÉSULTATS DU JOUR</b>
📅 27/06/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 POSTE 1 : NÉGOCIATEUR SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_negociateur = [
    {
        "titre": "Concepteur Télécom F/H",
        "entreprise": "Eiffage Énergie Systèmes",
        "lieu": "Toulouse (31)",
        "type": "CDI",
        "source": "Indeed",
        "date": "27/02/2026",
        "lien": "https://to.indeed.com/aay9j7zpcpfg"
    },
    {
        "titre": "Négociateur Telecom - Sites GSM Radio H/F",
        "entreprise": "LTd",
        "lieu": "Éleu-Dit-Leauwette (62)",
        "type": "CDI",
        "source": "LinkedIn",
        "date": "Récent",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-telecom-sites-gsm-radio-h-f-at-ltd-3779231295"
    },
    {
        "titre": "Négociateur Télécom — Saint-Mandé (30–40k€/an)",
        "entreprise": "Multiples entreprises",
        "lieu": "Saint-Mandé (94)",
        "type": "CDI",
        "source": "HelloWork",
        "date": "23/06/2026",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Négociateur Télécom — Paris (25–35k€/an, télétravail)",
        "entreprise": "Multiples entreprises",
        "lieu": "Paris (75) — Télétravail",
        "type": "CDI",
        "source": "HelloWork",
        "date": "23/06/2026",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Négociateur Télécom — Offres juin 2026",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "Jobintree",
        "date": "Juin 2026",
        "lien": "https://www.jobintree.com/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Négociateur de Site Radio — Recherche APEC",
        "entreprise": "VINCI, Akinext, Eiffage, ND-Ingénierie",
        "lieu": "France (Paris, Nantes, Saint-Herblain...)",
        "type": "CDI/CDD",
        "source": "APEC",
        "date": "Juin 2026",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=N%C3%89GOCIATEUR+DE+SITE+RADIO"
    },
    {
        "titre": "Radio Telecom — +200 offres toutes fonctions",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "date": "15/06/2026",
        "lien": "https://fr.indeed.com/Emplois-Radio-Telecom"
    },
    {
        "titre": "Telecom — +2 550 offres tous profils",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "HelloWork",
        "date": "21/06/2026",
        "lien": "https://www.hellowork.com/fr-fr/emploi/domaine_telecom.html"
    },
]

for i, job in enumerate(jobs_negociateur, 1):
    send(f"""📌 <b>{i}. {job['titre']}</b>
🏢 {job['entreprise']}
📍 {job['lieu']}
📄 {job['type']} — {job['source']} ({job['date']})
🔗 <a href="{job['lien']}">Voir l'offre</a>""")

# ─── CHEF DE PROJET SITE RADIO TELECOM ────────────────────────────────────────

send("""━━━━━━━━━━━━━━━━━━━━━━━━━━
🔵 POSTE 2 : CHEF DE PROJET SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_cdp = [
    {
        "titre": "Ingénieur Réseau Projet H/F",
        "entreprise": "Seaowl Technology Solutions",
        "lieu": "Ollioules (83)",
        "type": "CDI",
        "source": "Indeed",
        "date": "01/06/2026",
        "lien": "https://to.indeed.com/aag964pcdnyw"
    },
    {
        "titre": "Ingénieur Systèmes H/F",
        "entreprise": "ROHDE & SCHWARZ GmbH & Co. KG",
        "lieu": "Meudon (92)",
        "type": "CDI",
        "source": "Indeed",
        "date": "04/06/2026",
        "lien": "https://to.indeed.com/aabx8vz67hxv"
    },
    {
        "titre": "Conducteur de Travaux Radio H/F",
        "entreprise": "ENSIO",
        "lieu": "Flins-sur-Seine (78)",
        "type": "CDI",
        "source": "Indeed",
        "date": "04/05/2026",
        "lien": "https://to.indeed.com/aa9gndbbvc6n"
    },
    {
        "titre": "Ingénieur Senior Telecom - Oil & Gas H/F",
        "entreprise": "NEO2",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "Indeed",
        "date": "06/03/2026",
        "lien": "https://to.indeed.com/aajdcphnwfp7"
    },
    {
        "titre": "CHEF DE PROJET DÉPLOIEMENT H/F/NB",
        "entreprise": "NRJ AUDIO",
        "lieu": "Vénissieux (69)",
        "type": "CDI",
        "source": "Indeed",
        "date": "25/02/2026",
        "lien": "https://to.indeed.com/aavyxt79myxw"
    },
    {
        "titre": "RESPONSABLE ADJOINT TRAVAUX SUD OUEST H/F/NB",
        "entreprise": "NRJ AUDIO",
        "lieu": "Toulouse (31)",
        "type": "CDI",
        "source": "Indeed",
        "date": "25/02/2026",
        "lien": "https://to.indeed.com/aaf6pfvfg7gq"
    },
    {
        "titre": "Chef de projet univers téléphonie H/F",
        "entreprise": "R&S TELECOM / SMARTPOINT",
        "lieu": "Vélizy-Villacoublay (78)",
        "type": "CDD 6 mois (dès juillet 2026, 2500€+300€/mois)",
        "source": "Jobijoba",
        "date": "Juin 2026",
        "lien": "https://www.jobijoba.com/fr/annonce/54/b94bb655cd1fcba2e4daf44b2ec90ea9"
    },
    {
        "titre": "Chef de Projet Radio Télécom — Recherche APEC",
        "entreprise": "Diverses entreprises",
        "lieu": "France",
        "type": "CDI",
        "source": "APEC",
        "date": "Juin 2026",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=Chef+de+projet+Radio+T%C3%A9l%C3%A9com"
    },
    {
        "titre": "Chef Projet Telecom — +800 offres",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "date": "20/06/2026",
        "lien": "https://fr.indeed.com/q-chef-projet-telecom-emplois.html"
    },
    {
        "titre": "43 offres — Chef de Projet Déploiement Radio",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "LinkedIn",
        "date": "Juin 2026",
        "lien": "https://fr.linkedin.com/jobs/chef-de-projet-deploiement-radio-emplois/"
    },
    {
        "titre": "Chef de projet télécom — Freelance & CDI",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/Freelance",
        "source": "Free-Work",
        "date": "Juin 2026",
        "lien": "https://www.free-work.com/fr/tech-it/jobs/telecom"
    },
    {
        "titre": "Chef Projet Déploiement Telecom — Jooble",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "Jooble",
        "date": "Juin 2026",
        "lien": "https://fr.jooble.org/emploi-chef-projet-deploiement-telecom"
    },
]

for i, job in enumerate(jobs_cdp, 1):
    send(f"""📌 <b>{i}. {job['titre']}</b>
🏢 {job['entreprise']}
📍 {job['lieu']}
📄 {job['type']} — {job['source']} ({job['date']})
🔗 <a href="{job['lien']}">Voir l'offre</a>""")

# ─── MESSAGE DE FIN ────────────────────────────────────────────────────────────

send("""━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ <b>Envoi terminé !</b>

📊 <b>Récapitulatif du 27/06/2026 :</b>
• 8 annonces Négociateur Site Radio Télécom
• 12 annonces Chef de Projet Site Radio Télécom
• Sources : Indeed, LinkedIn, APEC, HelloWork, Jobintree, Jooble, Jobijoba, Free-Work

🔄 Prochain envoi demain avec de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
