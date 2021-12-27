import torch
import os
import glob
from facenet_pytorch import InceptionResnetV1,fixed_image_standardization
from torchvision import transforms
import numpy as np
from PIL import Image
from facenet_pytorch import MTCNN
import cv2
from datetime import datetime

#gửi request tới trang chứa đường link download của mình
import urllib.request
# File download về là file zip nên phải unzip ra
import zipfile

import splitfolders

import mediapipe as mp
import cvzone
import math
import time