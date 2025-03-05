import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

c = np.array([[3.,4], [5.,6], [6.,7]])
step = tf.reduce_mean(c, 1)                                                                                 
print(step)