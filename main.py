from fastapi import FastAPI

# -------------------------
# VALID EMAIL DOMAINS
# -------------------------
email_domains = [
    {"domain": "gmail.com"},
    {"domain": "yahoo.com"},
    {"domain": "outlook.com"},
    {"domain": "hotmail.com"},
    {"domain": "aol.com"},
    {"domain": "icloud.com"},
    {"domain": "mail.com"},
    {"domain": "protonmail.com"},
    {"domain": "zoho.com"},
    {"domain": "gmx.com"},
]

app = FastAPI()

# -------------------------
# ROOT ENDPOINT
# -------------------------
@app.get("/")
async def root():
    return {"message": "Hello! Welcome to EmailAuth"}

# -------------------------
# HEALTH CHECK
# -------------------------
@app.get("/health")
async def health():
    return {"status": "ok"}

# -------------------------
# GET ALL VALID DOMAINS
# -------------------------
@app.get("/domains")
async def get_domains():
    return {"valid_domains": email_domains}

# -------------------------
# CHECK IF A DOMAIN IS VALID
# -------------------------
@app.get("/signup/{domain}")
async def check_domain(domain: str):
    for d in email_domains:
        if d["domain"] == domain.lower():
            return {"domain": domain, "valid": True}
    return {"domain": domain, "valid": False}
