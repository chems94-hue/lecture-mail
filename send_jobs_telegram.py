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
📅 02/07/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 POSTE 1 : NÉGOCIATEUR SITE RADIO TELECOM
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

jobs_negociateur = [
    {
        "titre": "Négociateur en Immobilier Telecom H/F",
        "entreprise": "ND-Ingénierie",
        "lieu": "La Houssaye-en-Brie (77)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aasl9ffzplmy"
    },
    {
        "titre": "Négociateur de Sites Radio H/F",
        "entreprise": "VPI Telecom",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-de-sites-radio-h-f-at-vpi-telecom-3329554722"
    },
    {
        "titre": "Négociateur de Sites Télécoms H/F",
        "entreprise": "Mentory",
        "lieu": "Metz (57)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-de-sites-t%C3%A9l%C3%A9coms-h-f-at-mentory-3619855352/"
    },
    {
        "titre": "ALTERNANCE Bac+2 Négociateur en Télécom H/F (Réf 446)",
        "entreprise": "BEFORMA",
        "lieu": "Saint-Paul (La Réunion)",
        "type": "Alternance",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aafrnzrflv2v"
    },
    {
        "titre": "Négociateur de Site Radio — toutes offres",
        "entreprise": "Diverses entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=N%C3%89GOCIATEUR+DE+SITE+RADIO"
    },
    {
        "titre": "Négociateur Télécom — toutes offres (12 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_negociateur-telecom.html"
    },
    {
        "titre": "Négociateur Sites Telecom Mobile — toutes offres",
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
        "lien": "https://to.indeed.com/aa2g96gdfxv6"
    },
    {
        "titre": "Chef de Projet Déploiement Radio – Secteur Télécom H/F",
        "entreprise": "ALTEN",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-%E2%80%93-secteur-t%C3%A9l%C3%A9com-h-f-at-alten-3345041097"
    },
    {
        "titre": "Conducteur de Travaux Radio H/F",
        "entreprise": "ENSIO",
        "lieu": "Flins-sur-Seine (78)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aacmnbqyhc8v"
    },
    {
        "titre": "Responsable Adjoint Travaux Sud-Ouest H/F/NB",
        "entreprise": "NRJ AUDIO",
        "lieu": "Toulouse (31)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aachynmc89fl"
    },
    {
        "titre": "Ingénieur Senior Télécom - Projet EPC Oil & Gas H/F",
        "entreprise": "NEO2",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aa4v6vn4kfr2"
    },
    {
        "titre": "Chef de Projet Radio Télécom — toutes offres",
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
• 7 annonces Négociateur Site Radio
• 9 annonces Chef de Projet Site Radio
• Sources : Indeed, LinkedIn, APEC, HelloWork

🔄 Relance ce script demain pour de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
