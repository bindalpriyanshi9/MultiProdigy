import os
from github import Github, GithubException

REPO_NAME = "Abhay-Cerberus/MultiProdigy"  # ← update this (FORGOT TO UPDATE THIS XDD)
ACCESS_TOKEN = os.environ.get("GH_TOKEN")
if not ACCESS_TOKEN:
    raise RuntimeError("Missing GitHub Token. Please set GH_TOKEN in your environment.")

gh = Github(ACCESS_TOKEN)
repo = gh.get_repo(REPO_NAME)

# ————— LABELS —————
labels = {
    "bug": "Something isn't working",
    "enhancement": "Improvement to existing code",
    "documentation": "Changes to docs",
    "good first issue": "Good for newcomers",
    "help wanted": "Extra assistance needed",
    "discussion": "Design discussion",
    "pinned": "High visibility",
    "on hold": "Deferred for now",
    "stale": "Marked as inactive",
}

print("🟡 Ensuring labels exist…")
existing = {lbl.name for lbl in repo.get_labels()}
for name, desc in labels.items():
    if name not in existing:
        try:
            repo.create_label(name=name, color="ededed", description=desc)
            print(f"  ✅ Created label: {name}")
        except GithubException as e:
            print(f"  ⚠️ Failed to create label {name}: {e}")
    else:
        print(f"  • Label already exists: {name}")

# ————— MILESTONES —————
milestones = [
    "Initial Setup",
    "Agent Core",
    "Messaging Bus",
    "Plugin System",
    "Documentation",
]
print("\n🟢 Ensuring milestones exist…")
existing_ms = {m.title for m in repo.get_milestones(state="all")}
for title in milestones:
    if title not in existing_ms:
        try:
            repo.create_milestone(title=title)
            print(f"  ✅ Created milestone: {title}")
        except GithubException as e:
            print(f"  ⚠️ Failed to create milestone {title}: {e}")
    else:
        print(f"  • Milestone already exists: {title}")

# ————— ISSUES —————
default_issues = [
    ("Refactor agents.py", "Improve structure, add comments.", "enhancement"),
    ("Create demo", "Add a working example inside `demo/` folder.", "good first issue"),
    ("Improve scheduler", "Make task scheduling async and non-blocking.", "enhancement"),
]

print("\n📝 Ensuring issues exist…")
# build a set of titles of open and closed issues
all_issues = {issu.title for issu in repo.get_issues(state="all")}
for title, body, label in default_issues:
    if title not in all_issues:
        try:
            repo.create_issue(title=title, body=body, labels=[repo.get_label(label)])
            print(f"  ✅ Created issue: {title}")
        except GithubException as e:
            print(f"  ⚠️ Failed to create issue {title}: {e}")
    else:
        print(f"  • Issue already exists: {title}")
