import os
import subprocess
import AUTOREG
import sys

# Colors for terminal text (ANSI escape codes)
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m', '\033[0m']

try:
    # Show that the tool is only for 64-bit systems
    print("\033[93mThis tool is only for 64-bit systems!\033[0m")

    # Open the provided WhatsApp link using the default web browser
    link = "https://chat.whatsapp.com/ITPZEK1d1Qu0i6s2dY2W8R"

    # For Windows, macOS, or Linux
    if os.name == 'nt':  # Windows
        subprocess.run(["start", link], shell=True)
    elif os.name == 'posix':  # macOS/Linux
        subprocess.run(["xdg-open", link])  # For Linux or macOS, this will open the URL in the default browser

    print("▶️ Running main function...")
    AUTOREG.main()  # Assumes 'main' exists; will raise an error if it doesn't.

except ImportError as e:
    print("❌ Import error:", e)

except AttributeError:
    print("⚠️ 'main' function not found. Check available attributes:", dir(AUTOREG))
