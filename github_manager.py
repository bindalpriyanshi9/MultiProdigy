from github import Github
import os
from datetime import datetime, timedelta

# Replace with your personal access token and repo name
ACCESS_TOKEN = "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"
REPO_NAME = "bindalpriyanshi9/Agentic-AI"

# Connect to GitHub
g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)

# Create Milestones
milestone_titles = ["MVP Release", "Bug Bash", "Final Launch"]
milestones = []

existing_milestones = {m.title: m for m in repo.get_milestones(state="all")}

for title in milestone_titles:
    if title in existing_milestones:
        print(f"Milestone '{title}' already exists. Reusing it.")
        milestones.append(existing_milestones[title])
    else:
        milestone = repo.create_milestone(
            title=title,
            due_on=datetime.utcnow() + timedelta(days=30)
        )
        milestones.append(milestone)
        print(f"Created milestone: {title}")


# Create Labels
labels = {
    "bug": "d73a4a",
    "enhancement": "a2eeef",
    "documentation": "0075ca",
    "good-first-issue": "7057ff"
}

for name, color in labels.items():
    try:
        repo.create_label(name=name, color=color)
        print(f"Label '{name}' created.")
    except:
        print(f"Label '{name}' might already exist.")

# Create Issues
issues_data = [
    ("Refactor agents.py", "Clean and modularize agent logic", "enhancement"),
    ("Create demo", "Add a streamlit or CLI demo", "good-first-issue"),
    ("Improve scheduler", "Optimize task scheduling algorithm", "bug"),
]

for title, body, label in issues_data:
    issue = repo.create_issue(
        title=title,
        body=body,
        labels=[repo.get_label(label)],
        milestone=milestones[0]
    )
    print(f"Created issue: {title}")

# Create Release Checklist as Issue
release_checklist = """
### Release Checklist

- [ ] Final code review
- [ ] Pass all CI checks
- [ ] Documentation updated
- [ ] Version bumped
- [ ] Draft release notes
- [ ] Tag release
"""

repo.create_issue(
    title="Release Preparation",
    body=release_checklist,
    labels=[repo.get_label("documentation")],
    milestone=milestones[0]
)

print("Release checklist issue created.")

# Optional: Setup stale bot config template (needs to be committed manually)
stale_config = """
# Configuration for probot/stale - https://github.com/probot/stale

daysUntilStale: 30
daysUntilClose: 7
exemptLabels:
  - pinned
  - security
staleLabel: stale
markComment: >
  This issue has been automatically marked as stale because it has not had recent activity.
  It will be closed if no further activity occurs. Thank you!
"""

# Create the `.github` directory if it doesn't exist
os.makedirs(".github", exist_ok=True)

# Now safely write the stale bot config
with open(".github/stale.yml", "w") as f:
    f.write(stale_config)

print("Created stale bot config. Commit it to `.github/stale.yml`.")
