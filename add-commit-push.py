import subprocess
import argparse


def run_command(command):
    print(f"\n$ {' '.join(command)}") 
    result = subprocess.run(command, text=True)  
    print()  
    
    return result.returncode == 0

def main():
    
    parser = argparse.ArgumentParser(description="Automate git add, commit, and push.")
    parser.add_argument("-m", "--message", help="Commit message")
    parser.add_argument("-f", "--force", action="store_true", help="Skip confirmation step")
    args = parser.parse_args()

    
    message = args.message if args.message else "Auto commit via add-commit-push.py"

    
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", message],
        ["git", "push"]
    ]

   
    print("The following commands will be executed:")
    for cmd in commands:
        print("  " + " ".join(cmd))

   
    if not args.force:
        confirm = input("\nProceed with these commands? (y/n): ").strip().lower()
        if confirm != "y":
            print("Operation cancelled by user.")
            return
    else:
        print("\Force mode enabled — skipping confirmation.")

   
    for cmd in commands:
        success = run_command(cmd)
        if not success:
            print("Error running command. Stopping execution.")
            return

    print("\n✅ All commands executed successfully!")

if __name__ == "__main__":
    main()
