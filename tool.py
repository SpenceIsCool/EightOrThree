# tool.py


# LIBRABRIES
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import time


# FUNCTIONS
"""
convert_prediction_vector_to_language
@param pv: a linear collection of length 2 with values between 0 and 1
@returns: a string either 'asl' if the first value of $pv is larger,
        or 'isl' if the second value of $pv is larger
"""
def convert_prediction_vector_to_language(pv):
  return 'asl' if pv[0] > pv[1] else 'isl'


"""
convert_prediction
@param pred: a linear collection of values each b/w 0 and 1 that would summate to 1
@returns: the index of the largest value in $pred
"""
def convert_prediction(pred):
  arr_indx = 0
  max = -1
  for i in range(0, len(pred)):
    if pred[i] > max:
      max = pred[i]
      arr_indx = i
  return arr_indx


"""
convert_img
@param img: an np array size 224x224x3
@let out_img: be the image found after translation of $img
@return: { 'out_img': $out_img, 'langauge': 'asl' | 'isl', 'semantic': string value int in [0, 9]}
"""
def convert_img(img):
  test_img_tensor = tf.convert_to_tensor(np.array([img]))
  test_img_language = langauge_classifier.predict(test_img_tensor)
  test_language = convert_prediction_vector_to_language(test_img_language[0])
  test_img_semantic = isl_classifier.predict(test_img_tensor) if test_language == "isl" else asl_classifier.predict(test_img_tensor)

  test_semantic = convert_prediction(test_img_semantic[0])
  out_img = asl_samples[test_semantic] if test_language == "isl" else isl_samples[test_semantic]

  struct = { "out_img": np.array(out_img), "langauge": test_language, "semantic": test_semantic}
  return struct


"""
time_it
@param it: a thunk
@returns: a series
        1. the result of executing $it
        2. the time it took to execute $it
"""
def time_it(it):
  start = time.time()
  res = it()
  end = time.time()
  diff_time_seconds = (end-start)
  return res, diff_time_seconds


"""
test_img
@param o: {'img_shaped': np array size 224x224x3, 'langauge': 'asl' | 'isl', 'semantic': string value int in [0, 9]}
@param save_path: the path to a filename where an image will be saved
times and executes convert_img over the image at $o.img_shaped, displays some information and stores an image to $save_path
"""
def test_img(o, save_path):
  in_img = o['img_shaped']

  struct, seconds_spent = time_it(lambda: convert_img(in_img))

  new_img = struct['out_img']
  langauge_classified = struct['langauge']
  semantic_classified = struct['semantic']

  print(f"\n\nExpected language {o['language']}")
  if langauge_classified == o['language']:
    print(f"correct languge identified: {langauge_classified}")
  else:
    print(f"XXXXXXXXXX Incorrect language identified: {langauge_classified}")

  print(f"\n\nExpected semantic {o['semantic']}")
  if semantic_classified == int(o['semantic']):
    print(f"correct semantic identified: {semantic_classified}")
  else:
    print(f"XXXXXXXXXX Incorrect semantic identified: {semantic_classified}")

  print(f"\n\ntime took:        {seconds_spent}s\n\n")

  f, ax = plt.subplots(2)
  # f.set_size_inches(2,4)
  ax[0].imshow(in_img)
  ax[0].set_title("Original Image")
  ax[1].imshow(new_img)
  ax[1].set_title("Translated Image")
  f.subplots_adjust(top=1.2)
  f.savefig(save_path, pad_inches=0.1, format='png', bbox_inches='tight')


if __name__ == "__main__":

    project = os.getcwd()
    datasets = f'{project}/datasets/'
    asl_isl = f'{datasets}/original/asl_isl.tiny.test.npy'
    models = f'{project}/models/'
    results = f'{project}/results'

    langauge_classifier = tf.keras.models.load_model(f'{models}/tl_asl_isl_language_best.hdf5')
    isl_classifier = tf.keras.models.load_model(f'{models}/tl_isl_semantic_best.hdf5')
    asl_classifier = tf.keras.models.load_model(f'{models}/tl_asl_semantic_best.hdf5')
    asl_samples = np.load(f'{datasets}/asl_sample.npy', allow_pickle=True)
    isl_samples = np.load(f'{datasets}/isl_sample.npy', allow_pickle=True)

    my_np = np.load(asl_isl, allow_pickle='True')

    i = 1
    my_img = f'{results}/my_random_image.png'
    test_img(my_np[i], my_img)

    
