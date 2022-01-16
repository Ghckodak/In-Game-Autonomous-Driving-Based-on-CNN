import cv2
import pickle
from getkeys import*

file_name = 'training_data.pkl'

pickle_file = open(file_name, 'rb')
training_data = pickle.load(pickle_file)
pickle_file.close()


