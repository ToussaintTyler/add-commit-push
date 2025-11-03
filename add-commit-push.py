import subprocess
import argparse
import sys

def run_and_print(command):
    """Prints the command, executes it, and prints the result."""
    print(f"\n$ {' '.join(command)}")
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(f" Error: {e.stderr.strip()}")
        sys.exit(1)

def main():

    parser = argparse.ArgumentParser(
        description="Automate git add, commit, and push from the command line."
    )
    parser.add_argument("-m", "--message", type=str, help="Commit message.")
    parser.add_argument("-f", "--force", action="store_true", help="Skip confirmation step.")
    args = parser.parse_args()

    commit_message = args.message if args.message else "Auto commit via add-commit-push.py"

    print("git status:")
    try:
        subprocess.run(["git", "status"], check=True)
    except subprocess.CalledProcessError:
        print(" Not a git repository or git not installed.")
        sys.exit(1)

    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", commit_message],
        ["git", "push"]
    ]

    print("\nThe following commands will be executed:")
    for cmd in commands:
        print("  " + " ".join(cmd))

    if not args.force:
        confirm = input("\nProceed with these commands? (y/n): ").strip().lower()
        if confirm != "y":
            print(" Operation cancelled by user.")
            sys.exit(0)
    else:
        print("\n Force mode enabled — skipping confirmation.")

    for cmd in commands:
        run_and_print(cmd)

    print("\n All commands executed successfully!")

if __name__ == "__main__":
    main()