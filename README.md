vmanalyzer is a simple python program to use whisper ai on each wav file in the directory the program is in.

vmanalyzer2 is a Tkinter GUI to use Whisper AI tiny english model to transcribe all of the wav files in the current directory (where the vmanalyzer2.py is located)
then output the transcription onto a new window.

The following dependencies need to be installed:
-Python https://www.python.org/
-Pytorch https://pytorch.org/get-started/locally/
-FFMPEG https://ffmpeg.org/
-Whisper AI https://github.com/openai/whisper
-Pillow Fork of Python Image Library

Recommended installation on Windows
Python:
Navigate to https://www.python.org/ and download the current verison of python. Once downloaded open the python installation file.
MAKE SURE TO ADD PYTHON TO PATH

PyTorch:
After python is installed, open an elevated command prompt or PowerShell. Copy and past the following and hit enter to run:
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

FFMPEG:
Follow the directions at https://chocolatey.org/install to install the package manager Chocolatey.
Once Chocolately is installed open an elevated command prompt or PowerShell, the copy and paste the following and hit enter to run:
choco install ffmpeg

Whisper AI:
Open an elevated command prompt or PowerShell, then copy and past the following and hit enter to run:
pip install openai-whisper

Pillow:
Open an elevated command prompt or PowerShell, then copy and paste the following and hit enter to run:
pip install pillow

