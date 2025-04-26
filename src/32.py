import os
import subprocess
from typing import List

def run_command(commands: List[str]) -> None:
    """
    Run multiple commands using subprocess.
    
    Args:
    - commands: A list of strings representing the command to be executed.
    """
    for command in commands:
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Example usage
    commands = ["ls", "pwd"]
    run_command(commands)
