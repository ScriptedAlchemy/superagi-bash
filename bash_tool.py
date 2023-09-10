import os  # Import the os module

class BashCommandTool(BaseTool):
    """
    Bash Command Tool
    """
    name: str = "Bash Command Tool"
    args_schema: Type[BaseModel] = BashCommandInput
    description: str = "Executes a Bash Command"

    def _execute(self, command: str = None):
        # Check current working directory
        current_dir = os.getcwd()
        target_dir = "/app/workspace"

        # Change directory if not in target directory
        if current_dir != "/app":
            os.chdir(target_dir)

        if not validate_command(command):
            return "Invalid bash command."

        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Command '{command}' returned non-zero exit status {e.returncode}."
