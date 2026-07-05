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
📅 05/07/2026

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
        "titre": "Négociateur Telecom - Sites GSM Radio H/F",
        "entreprise": "LTd",
        "lieu": "Le Havre (76)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-telecom-sites-gsm-radio-h-f-at-ltd-3779233332"
    },
    {
        "titre": "Négociatrice ou Négociateur de Sites H/F",
        "entreprise": "Circet",
        "lieu": "France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociatrice-ou-n%C3%A9gociateur-de-sites-h-f-at-circet-4167730328"
    },
    {
        "titre": "Négociateur Radio H/F",
        "entreprise": "Extia Ingénierie",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emplois/80692692.html"
    },
    {
        "titre": "Négociateur Télécoms H/F",
        "entreprise": "VPI Telecom",
        "lieu": "France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-t%C3%A9l%C3%A9coms-h-f-at-vpi-telecom-4124748559"
    },
    {
        "titre": "Négociateur Télécom H/F",
        "entreprise": "DGE Systea",
        "lieu": "France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-t%C3%A9l%C3%A9com-h-f-at-dge-systea-3979112490"
    },
    {
        "titre": "Négociateur Telecom Radio F/H",
        "entreprise": "Amaris Consulting",
        "lieu": "France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-telecom-radio-f-h-x-at-amaris-consulting-3388904413"
    },
    {
        "titre": "Toutes offres — Négociateur Télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=N%C3%A9gociateur+T%C3%A9l%C3%A9com"
    },
    {
        "titre": "Toutes offres — Négociateur Sites Telecom Mobile",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "Indeed",
        "lien": "https://fr.indeed.com/q-negociateur-sites-telecom-mobile-emplois.html"
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
        "titre": "Toutes offres — Négociateur de Sites Télécoms",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "OptionCarrière",
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
        "titre": "Chef de Projet Déploiement Radio – Secteur Télécom H/F",
        "entreprise": "ALTEN",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-%E2%80%93-secteur-t%C3%A9l%C3%A9com-h-f-at-alten-3345041097"
    },
    {
        "titre": "Chef de Projet Déploiement Radio H/F",
        "entreprise": "TIBCO Telecoms",
        "lieu": "Rennes (35)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-h-f-at-tibco-telecoms-3554707489"
    },
    {
        "titre": "Chef de Projet Déploiement Radio H/F",
        "entreprise": "TIBCO Telecoms",
        "lieu": "Nancy (54)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-h-f-at-tibco-telecoms-3504927798"
    },
    {
        "titre": "Chef de Projet Déploiement Radio H/F",
        "entreprise": "Groupe Trèfle",
        "lieu": "Boulogne-Billancourt (92)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-h-f-at-groupe-trefle-3439855062/"
    },
    {
        "titre": "Chef de Projet Déploiement Radio Télécom F/H",
        "entreprise": "AGH Consulting",
        "lieu": "France",
        "type": "CDI",
        "source": "TalentDetection",
        "lien": "https://www.talentdetection.com/agh-consulting/offre-57993-O0MGPh"
    },
    {
        "titre": "Chef de Projet Infrastructure Réseaux Télécom F/H",
        "entreprise": "Ministère de l'Europe et des Affaires étrangères",
        "lieu": "France",
        "type": "CDD/Titulaire",
        "source": "Diplomatie.gouv.fr",
        "lien": "https://emplois.diplomatie.gouv.fr/nos-offres/28f1624f-0c91-47a6-9faa-6c5bf57e714c"
    },
    {
        "titre": "Chef de Projet Déploiement H/F",
        "entreprise": "NRJ AUDIO",
        "lieu": "Vénissieux (69)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aa4g7sznb8cn"
    },
    {
        "titre": "Responsable Adjoint Travaux Sud Ouest H/F",
        "entreprise": "NRJ AUDIO",
        "lieu": "Toulouse (31)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aatdylxncv8w"
    },
    {
        "titre": "Conducteur de Travaux Radio H/F",
        "entreprise": "ENSIO",
        "lieu": "Flins-sur-Seine (78)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aazvzvv82jsx"
    },
    {
        "titre": "Ingénieur Senior Telecom - Projet EPC Oil & Gas H/F",
        "entreprise": "NEO2",
        "lieu": "Paris (75)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aayjbqxs9qgw"
    },
    {
        "titre": "Toutes offres — Chef de Projet Radio Télécom",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "APEC",
        "lien": "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=Chef+de+projet+Radio+T%C3%A9l%C3%A9com"
    },
    {
        "titre": "Toutes offres — Chef de Projet Déploiement Radio (43 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/chef-de-projet-deploiement-radio-emplois/"
    },
    {
        "titre": "Toutes offres — Chef de Projet Télécom (+70 offres)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "CDI/CDD/Intérim",
        "source": "HelloWork",
        "lien": "https://www.hellowork.com/fr-fr/emploi/metier_chef-de-projet-telecoms.html"
    },
    {
        "titre": "Toutes offres — Chef Projet Déploiement Télécom",
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

send(f"""━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ <b>Envoi terminé !</b>

📊 <b>Récapitulatif :</b>
• {len(jobs_negociateur)} annonces Négociateur Site Radio Telecom
• {len(jobs_cdp)} annonces Chef de Projet Site Radio Telecom
• Sources : Indeed, LinkedIn, APEC, HelloWork, Jooble, TalentDetection, Diplomatie.gouv.fr, OptionCarrière

🔄 Relance ce script demain pour de nouvelles annonces.
━━━━━━━━━━━━━━━━━━━━━━━━━━""")

print("✅ Tous les messages envoyés sur Telegram !")
