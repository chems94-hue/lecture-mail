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
📅 01/07/2026

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
        "titre": "Négociateur de Sites Radio H/F",
        "entreprise": "VPI Telecom",
        "lieu": "Paris, Île-de-France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-de-sites-radio-h-f-at-vpi-telecom-3329554722"
    },
    {
        "titre": "Négociateur Telecom Radio F/H (x)",
        "entreprise": "Amaris Consulting",
        "lieu": "France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/n%C3%A9gociateur-telecom-radio-f-h-x-at-amaris-consulting-3388904413"
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
        "titre": "49 offres — Négociateur Telecom (H/F)",
        "entreprise": "Multiples entreprises",
        "lieu": "France",
        "type": "Divers",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/n%C3%A9gociateur-telecom-(h-f)-emplois"
    },
    {
        "titre": "Toutes offres Négociateur Télécom",
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
        "titre": "Chef de Projet Radio F/H",
        "entreprise": "Eiffage Énergie Systèmes",
        "lieu": "Cuincy (59)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aaz6ymlwvlnb"
    },
    {
        "titre": "Chef de Projet Déploiement H/F",
        "entreprise": "NRJ AUDIO",
        "lieu": "Vénissieux (69)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aacfrp42kpst"
    },
    {
        "titre": "Conducteur de Travaux Radio H/F",
        "entreprise": "ENSIO",
        "lieu": "Flins-sur-Seine (78)",
        "type": "CDI",
        "source": "Indeed",
        "lien": "https://to.indeed.com/aa84ktdcj2sw"
    },
    {
        "titre": "Chef de Projet Déploiement Radio — Secteur Télécom H/F",
        "entreprise": "ALTEN",
        "lieu": "Île-de-France",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-%E2%80%93-secteur-t%C3%A9l%C3%A9com-h-f-at-alten-3302661556/"
    },
    {
        "titre": "Chef de Projet Déploiement Radio H/F",
        "entreprise": "Groupe Trefle",
        "lieu": "Boulogne-Billancourt (92)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-h-f-at-groupe-trefle-3439855062/"
    },
    {
        "titre": "Chef de Projet Déploiement Radio H/F",
        "entreprise": "Tibco Telecoms",
        "lieu": "Rennes (35)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chef-de-projet-d%C3%A9ploiement-radio-h-f-at-tibco-telecoms-3554707489"
    },
    {
        "titre": "Chef(fe) de Projet Télécom (Radio) — Dept 33",
        "entreprise": "Groupe Maestra",
        "lieu": "Bordeaux (33)",
        "type": "CDI",
        "source": "LinkedIn",
        "lien": "https://fr.linkedin.com/jobs/view/chefs-fes-de-projet-t%C3%A9l%C3%A9com-radio-dept-33-at-groupe-maestra-3378255570"
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
