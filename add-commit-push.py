print ("Hello wold")
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="Automate git add, commit, and push.")
    parser.add_argument("-m", "--message", type=str, help="Commit message.")
    args = parser.parse_args()

    commit_message = args.message if args.message else "Auto commit via add-commit-push.py"

print ("Starting add-commit-push")

print ("git status")
subprocess.run(["git", "status"])

print ("git add -A")
subprocess.run(["git", "add", "-A"], check=True)

print ("git commit -m")
subprocess.run(["git", "commit", "-m", commit_message], check=True)

print ("git push")
subprocess.run(["git", "push"], check=True)
