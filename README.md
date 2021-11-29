# ResNet_GUI
A GUI application that allows users to load an image, predict what is in the image, view the classification, and view the attention map.

# ResNet_GUI
A GUI application that allows users to load an image, predict what is in the image, view the classification, and view the attention map.

## To run the app:
1. Navigate into the desired directory and open the command prompt
2. Clone the current repository and change into the cloned directory
```bash
git clone https://github.com/gabrielbrosula/ResNet_GUI.git
cd ResNet_GUI
```
3. Create a Python virtual environment and activate it
```bash
# Installing virtualenv
pip install --user virtualenv

# Creating the ResNET_GUI environment
python -m venv ResNET_GUI

# Activating the ResNET_GUI environment in Windows
ResNET_GUI\Scripts\activate.bat

# Activating the ResNET_GUI environment in macOS or Linux
source Scripts/bin/activate
```
4. Install the required packages into the current environment
```bash
pip install -r requirements.txt
```
5. Run resnet_gui.py
