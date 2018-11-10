# coding: utf-8

# **[MSE-01]** ���W���[�����C���|�[�g���āA�����̃V�[�h��ݒ肵�܂��B

# In[1]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

np.random.seed(20160604)


# **[MSE-02]** MNIST�̃f�[�^�Z�b�g��p�ӂ��܂��B

# In[2]:


mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)


# **[MSE-03]** �\�t�g�}�b�N�X�֐��ɂ��m�� p �̌v�Z����p�ӂ��܂��B

# In[3]:


x = tf.placeholder(tf.float32, [None, 784])
w = tf.Variable(tf.zeros([784, 10]))
w0 = tf.Variable(tf.zeros([10]))
f = tf.matmul(x, w) + w0
p = tf.nn.softmax(f)


# **[MSE-04]** �덷�֐� loss �ƃg���[�j���O�A���S���Y�� train_step ��p�ӂ��܂��B

# In[4]:


t = tf.placeholder(tf.float32, [None, 10])
loss = -tf.reduce_sum(t * tf.log(p))
train_step = tf.train.AdamOptimizer().minimize(loss)


# **[MSE-05]** ���� accuracy ���`���܂��B

# In[5]:


correct_prediction = tf.equal(tf.argmax(p, 1), tf.argmax(t, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# **[MSE-06]** �Z�b�V������p�ӂ��āAVariable�����������܂��B

# In[6]:


sess = tf.Session()
sess.run(tf.initialize_all_variables())


# **[MSE-07]** �p�����[�^�[�̍œK����2000��J��Ԃ��܂��B
# 
# 1��̏����ɂ����āA�g���[�j���O�Z�b�g������o����100�̃f�[�^��p���āA���z�~���@��K�p���܂��B
# 
# �ŏI�I�ɁA�e�X�g�Z�b�g�ɑ΂��Ė�92%�̐��𗦂������܂��B

# In[7]:


i = 0
for _ in range(2000):
    i += 1
    batch_xs, batch_ts = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, t: batch_ts})
    if i % 100 == 0:
        loss_val, acc_val = sess.run([loss, accuracy],
            feed_dict={x:mnist.test.images, t: mnist.test.labels})
        print ('Step: %d, Loss: %f, Accuracy: %f'
               % (i, loss_val, acc_val))


# **[MSE-08]** ���̎��_�̃p�����[�^�[��p���āA�e�X�g�Z�b�g�ɑ΂���\����\�����܂��B
# 
# �����ł́A�u�O�v?�u�X�v�̐����ɑ΂��āA�����ƕs�����̗���R���\�����܂��B

# In[8]:


images, labels = mnist.test.images, mnist.test.labels
p_val = sess.run(p, feed_dict={x:images, t: labels}) 

fig = plt.figure(figsize=(8,15))
for i in range(10):                                                                                                                      
    c = 1
    for (image, label, pred) in zip(images, labels, p_val):
        prediction, actual = np.argmax(pred), np.argmax(label)
        if prediction != i:
            continue
        if (c < 4 and i == actual) or (c >= 4 and i != actual):
            subplot = fig.add_subplot(10,6,i*6+c)
            subplot.set_xticks([])
            subplot.set_yticks([])
            subplot.set_title('%d / %d' % (prediction, actual))
            subplot.imshow(image.reshape((28,28)), vmin=0, vmax=1,
                           cmap=plt.cm.gray_r, interpolation="nearest")
            c += 1
            if c > 6:
                break