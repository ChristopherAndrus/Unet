# Unet
name: Unet 1.0
author: Christopher.Andrus

# Dataset
The dataset used in paper is composed of hundreds of data sample from various location. The dataset here is only for running the code for demonstration purpose, only to show the code is . The loss referred in the paper is trained on original data.

# Use
Due to size limit, the model is not uploaded.
create a folder named "model" and run train.py to train a demonstration model.
copy the state_dict.pt file generated during training and copy it to the folder of demonstration_model
then run test.py to generate prediction and error. It will generate a file named "result.png" in the running folder and show predicted image in batch.

# Requirement
opencv-python
PIL
numpy
pandas
scipy
matplotlib
natsort
tensorflow
keras
pytorch

# License
MIT License
