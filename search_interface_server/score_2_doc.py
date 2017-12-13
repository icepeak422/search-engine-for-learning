import scipy.io as sio
import numpy as np
import re
from urllib import urlopen

A = np.load('matrixA.npy')

# conceptbag = np.load('../bag/new_conceptbag.npy').item()


def score_2_doc(vec1,vec2):

	s21 = np.dot(np.dot(vec1, A),np.transpose(vec2))
	s12 = np.dot(np.dot(vec2, A),np.transpose(vec1))
	# print (s12-s21)
	return s21-s12
