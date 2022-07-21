import torch
import os
from torch import cuda
from src.utils import Color_map
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"

class config(object):

  model_path = "./model/"
  path = "./demonstration_dataset/"
  load_model = "./demonstration_model/state_dict.pt"
  batch = 1
  lr = 1e-4  
  epochs = 100
  input_size = (256,256)
  if cuda.is_available(): device = torch.device("cuda")
  else: device = torch.device('cpu')
  code2id, id2code, name2id, id2name = Color_map(path+'class_dict.csv') #change?