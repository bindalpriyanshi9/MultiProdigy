# setup_repo.py
import os
from github import Github

REPO_NAME = "Abhay-Cerberus/MultiProdigy"  # Change this to match your repo
ACCESS_TOKEN = os.environ.get("GH_TOKEN")

if not ACCESS_TOKEN:
    raise RuntimeError("Missing GitHub Token. Please set GH_TOKEN in your environment.")

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)

# -------------------- LABELS --------------------
labels = {
    "bug": "Something isn't working",
    "enhancement": "Improvement to existing code",
    "documentation": "Changes to docs",
    "good first issue": "Good entry-level issue",
    "help wanted": "Extra assistance needed",
    "discussion": "Discussion or proposal",
    "pinned": "Important issue to keep open",
    "on hold": "Deferred for now",
    "stale": "Marked as inactive"
}

print("🟡 Creating labels...")
for name, desc in labels.items():
    try:
        repo.create_label(name=name, color="ededed", description=desc)
        print(f"✅ Created label: {name}")
    except:
        print(f"⚠️ Label already exists or failed: {name}")

# -------------------- MILESTONES --------------------
milestones = ["Initial Setup", "Agent Core", "Messaging Bus", "Plugin System", "Documentation"]

print("🟢 Creating milestones...")
for m in milestones:
    try:
        repo.create_milestone(title=m)
        print(f"✅ Milestone created: {m}")
    except:
        print(f"⚠️ Milestone already exists: {m}")

# -------------------- ISSUES --------------------
default_issues = [
    ("Refactor agents.py", "Improve structure, add comments.", "enhancement"),
    ("Create demo", "Add a working example inside `demo/` folder.", "good first issue"),
    ("Improve scheduler", "Make task scheduling async and non-blocking.", "enhancement"),
]

print("📝 Creating default issues...")
for title, body, label in default_issues:
    issue = repo.create_issue(title=title, body=body, labels=[repo.get_label(label)])
    print(f"✅ Created issue: {title}")
