#!/usr/bin/env python3
import os
from github import Github
import pandas as pd

# === Configuración ===
token = os.getenv("GITHUB_TOKEN", None)
g = Github(token) if token else Github()

# Repositorio a analizar
REPO_NAME = "spring-projects/spring-framework"
SINCE = "2022-01-01T00:00:00Z"
KEYWORDS = ["cve", "security", "vulnerability", "fix"]
OUTPUT_CSV = os.path.join("data", "dataset_inicial.csv")

def extract_security_commits():
    repo = g.get_repo(REPO_NAME)
    commits = repo.get_commits(since=SINCE)
    records = []

    for commit in commits:
        msg = commit.commit.message.lower()
        if any(kw in msg for kw in KEYWORDS):
            records.append({
                "commit_sha": commit.sha,
                "commit_url": commit.html_url,
                "message": commit.commit.message.replace("\n", " "),
                "date": commit.commit.author.date.isoformat()
            })

    df = pd.DataFrame(records)
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"[+] {len(records)} commits extraídos. Guardados en {OUTPUT_CSV}")

if __name__ == "__main__":
    extract_security_commits()
