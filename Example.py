import  numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import tensorflow as tf
a = tf.global_variables(3)
sess= tf.Session()
sess.run(a)
print(a)