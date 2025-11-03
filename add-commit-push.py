print ("Hello wold")
import subprocess
<<<<<<< HEAD
commit_message="\"Your actual commit message\""
=======
commit_message= "\"Your actual commit message\""
>>>>>>> 2a54e0d9b6f9f24e49ab4d2cd7e94d59a86f2134
import argparse


def main():
    parser = argparse.ArgumentParser(description="Automate git add, commit, and push.")
    parser.add_argument("-m", "--message", type=str, help="Commit message.")
    args = parser.parse_args()
    message = args.message if args.message else "Auto commit via add-commit-push.py"

print ("Starting add-commit-push")

commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", commit_message],
    ["git", "push"]
]

print("The following commands will be executed:")
for cmd in commands:
    print("  " + " ".join(cmd))

confirm = input("\nProceed with these commands? (y/n): ").strip().lower()
if confirm != "y":
    print("Cancelled.")
    quit()

for cmd in commands:
    print(f"\n$ {' '.join(cmd)}")
    result = subprocess.run(cmd, text=True)
    if result.returncode != 0:
        print(" Error running command.")
        quit()

print("\ All commands executed successfully!")

print ("git status")
subprocess.run(["git", "status"])

print ("git add -A")
subprocess.run(["git", "add", "-A"], check=True)

print ("git commit -m")
subprocess.run(["git", "commit", "-m", commit_message], check=True)

print ("git push")
subprocess.run(["git", "push"], check=True)
