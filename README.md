# Unet
name: Unet 1.0
author: Christopher.Andrus

# Dataset
The dataset used in paper is composed of hundreds of data sample from various location. The dataset here is only for running the code for demonstration purpose, only to show the code is . The loss referred in the paper is trained on original data.<br >
Since this is a demonstration dataset, the trained model is likely overfitting on result. But with real data, the result is much more improved. The data source doesn't allow full open, thus the original data can't be made public. We are only demonstrating the code authenticity.<br >

# Use
Due to size limit( can't upload over 25 MB ), the model is not uploaded.<br >
create a folder named "model" and run train.py to train a demonstration model.<br >
copy the state_dict.pt file generated during training and copy it to the folder of demonstration_model<br >
then run test.py to generate prediction and error. It will generate a file named "result.png" in the running folder and show predicted image in batch.<br >

# Requirement
opencv-python<br >
PIL<br >
numpy<br >
pandas<br >
scipy<br >
matplotlib<br >
natsort<br >
tensorflow<br >
keras<br >
pytorch<br >

# License
MIT License
