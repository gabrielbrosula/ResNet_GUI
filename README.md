# ResNet_GUI
A GUI application that allows users to load an image, predict what is in the image, view the classification, and view the attention map.



![Walkthrough of Current Features](https://i.imgur.com/DyKcdEd.gif)

## To run the app:
- 1. Navigate into the desired directory and open the command prompt
- 1. Clone the current repository and change into the cloned directory
```bash
git clone https://github.com/gabrielbrosula/ResNet_GUI.git
cd ResNet_GUI
```
- 2. Create a Python virtual environment and activate it
```bash
# Installing virtualenv
pip install --user virtualenv

# Creating the ResNET_GUI environment
python -m venv ResNet_GUI

# Activating the ResNET_GUI environment in Windows
ResNet_GUI\Scripts\activate.bat

# Activating the ResNET_GUI environment in macOS or Linux
source Scripts/bin/activate
```
- 3. Install the required packages into the current environment
```bash
pip install -r requirements.txt
```
- 4. Run resnet_gui.py
```bash
py resnet_gui.py
```

## To Do:
- [ ] Add a "clear" button to reset all windows in GUI
- [ ] Create an executable file for the app
- [ ] Add feature to utilize other pre-trained models trained on the ImageNet database
- [ ] Add feature to compare performances of two pre-trained models at a time
- [ ] Create scalable windows for GUI
