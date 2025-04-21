"""
Directory Traversal Logger and Email Notifier

This script allows users to:
1. Traverse and log the contents of a specified directory (including subfolders and files).
2. Generate a structured log file (`directory_traversal_log.txt`) with system details.
3. Send the log as an email attachment to a recipient.
4. Move the log file to the system trash/recycle bin after successful dispatch.

Modules used:
- os: For directory traversal and path operations.
- getpass: For retrieving the current system username.
- socket: For fetching the system's hostname.
- datetime: For timestamping the log.
- yagmail (installed if missing): For sending emails through Gmail.
- send2trash (installed if missing): For safely moving files to trash instead of permanently deleting.

Functions:
1. pip(module_name): Tries to import the specified module, and if it's not found, installs it using pip.
2. send_email(receiver): Sends an email with the generated directory traversal log file as an attachment.
3. setup(): Prompts the user for a directory path and prepares it for traversal, returning the directory tree and current timestamp.
4. info(): Displays usage instructions for the directory traversal log generator.
5. generate_result_log(): Generates a directory traversal log and saves it as a text file with system metadata.

Main Execution Block:
    - Displays usage instructions via `info()`.
    - Prompts the user for the directory path to log.
    - Calls `generate_result_log()` to generate the directory traversal log.
    - Asks the user for an email address to send the log file.
    - Sends the email using `send_email()`, including the generated log as an attachment.
    - Moves the log file to trash (using `send2trash`) after the email is sent.

Usage:
    - The script requires the user to provide a valid directory path with proper formatting (double backslashes for Windows paths).
    - The log file will be generated in the same directory where the script is executed.
    - After sending the email, the log file will be moved to trash to prevent clutter.

Requirements:
    - yagmail (for email functionality) and send2trash (for moving files to trash) will be automatically installed if missing.

Author: Aishik Mukherjee
Date Created: 21-04-2025
"""

import os
from getpass import getuser
from socket import gethostname
from datetime import datetime

def pip(module_name):
    """
        Attempts to import a Python module by name. If the module is not found,
        it automatically installs it using pip and then imports it.

        Parameters:
            module_name (str): The name of the module to import or install.

        Returns:
            module: The imported module object.

        Raises:
            subprocess.CalledProcessError: If the pip installation fails.
            ImportError: If the module cannot be imported after installation.
        """
    import importlib
    try:
        return importlib.import_module( module_name)
    except ImportError:
        import sys, subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        return importlib.import_module(module_name)

# importing yagmail and send2trash
yagmail = pip("yagmail")
send2trash = pip("send2trash")


def send_email(receiver):
    """
        Sends an email with the generated directory traversal log file as an attachment.

        Parameters:
            receiver (str): The email address of the recipient.

        Behavior:
            - Uses yagmail to authenticate the sender's Gmail account.
            - Attaches 'directory_traversal_log.txt' located in the current working directory.
            - Sends a predefined subject and message content.

        Notes:
            - Ensure yagmail is installed and properly configured.
            - An app-specific password may be required if two-factor authentication (2FA) is enabled.
            - The sender credentials are hardcoded for demonstration purposes and should be handled securely in production.

        Raises:
            yagmail.error.YagAddressError: If the recipient email address is invalid.
            yagmail.error.YagConnectionClosed: If connection to the SMTP server fails.
            smtplib.SMTPException: For general email-sending issues.
        """

    path = os.getcwd() + r"\directory_traversal_log.txt"

    sender = "missingchildfound2025@gmail.com"
    password = "ejvs prqg wjuh qkrm"

    yag = yagmail.SMTP(sender, password)
    yag.send(
        to = receiver,
        subject = "Directory log",
        contents = "This is a system generated email, kindly do not reply.",
        attachments = path
    )

def setup():
    """
    Prompts the user to input a directory path and prepares it for traversal.

    Returns:
        tuple:
            - tree (generator): An os.walk generator object for directory traversal.
            - watch (datetime): A datetime object representing the current timestamp.

    Prompts:
        - Asks the user to enter the path of the directory they want to scan.

    Behavior:
        - Uses os.walk() to traverse the given directory.
        - Captures the current date and time for logging purposes.

    Raises:
        Prints the exception and exits the program if the given path is invalid or inaccessible.
    """
    path = input("Enter Path: ")
    try:
        tree = os.walk(path)
        watch = datetime.now()
        return tree, watch
    except Exception as e1:
        print(f"ERROR OCCURRED: {e1}")
        exit(0)

def info():
    """
        Displays usage instructions for the directory traversal log generator.

        Behavior:
            - Explains the purpose of the script.
            - Informs the user about the correct input format for directory paths.
            - Notifies the user that the log file will be created in the current working directory.

        Notes:
            - On Windows, double backslashes (\\) are required in directory paths.
    """
    print("Instructions:")
    print("---> This is a directory traversal log generator.")
    print("---> Input format for path is exactly as usual")
    print("--->only difference is that there are 2 backslashes in place of one.")
    print("---> The result file will be generated at the same "
          "location from where you are running this script.")

def generate_result_log():
    """
        Generates a detailed directory traversal log file for a user-specified path.

        Behavior:
            - Calls the `setup()` function to get the target directory and current timestamp.
            - Traverses the directory tree using `os.walk()`.
            - Logs each folder, subfolder, and file into 'directory_traversal_log.txt'.
            - Includes system metadata such as date, time, hostname, and username.
            - Saves the log in the current working directory with UTF-8 encoding.

        File Generated:
            directory_traversal_log.txt

        Output Format:
            - Log header with timestamp and system info.
            - Each folder's name followed by its subfolders and files.
            - Clear separators between entries for readability.

        Prints:
            - A success message upon completion.
        """
    tree , watch = setup()
    with open('directory_traversal_log.txt', 'w+',  encoding='utf-8') as f:
        f.write("THE DIRECTORY TRAVERSAL LOG:\n\n")
        f.write(f"Date: {watch.date()}\n")
        f.write(f"Time: {watch.time()}\n")
        f.write(f"Day: {watch.strftime('%A')}\n")
        f.write(f"Host name: {gethostname()}\n")
        f.write(f"Username: {getuser()}")

        for folder, subfolder, file in tree:
            f.write("\n\n==================================="
                    "=======================================")
            f.write(f"\nFOLDER: {folder}")

            f.write("\n---> Subfolders:")
            for x in subfolder:
                f.write(f"\n------> {x}")

            f.write("\n---> Files:")
            for k in file:
                f.write(f"\n------> {k}")

    print("\nAll done :)")

if __name__ == "__main__":
    """
    Main Execution Block

    This block is executed when the script is run directly (not imported as a module).

    Workflow:
        1. Displays usage instructions to the user via the `info()` function.
        2. Generates a directory traversal log file by calling `generate_result_log()`.
        3. Prompts the user for an email address to send the log as an attachment.
        4. Attempts to send the email using the `send_email()` function.
        5. If successful, displays a confirmation message.
        6. Regardless of email success, moves the log file to the system trash using `send2trash`.

    Notes:
        - Any exceptions during the email process are caught and printed.
        - The generated log is always deleted (moved to trash) at the end.
    """
    info()
    generate_result_log()
    try:
        send_email(input("Enter your email id: "))
        print("Email sent successfully")
    except Exception as e2:
        print(e2)
    send2trash.send2trash(os.getcwd() + r"\directory_traversal_log.txt")
