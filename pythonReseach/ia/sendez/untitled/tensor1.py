import tensorflow as tf

x = tf.constant(6)
y=tf.constant(5)

resulst= x*y
print(resulst)

"""
sesss= tf.Session()
print(sesss.run(resulst))

"""

with tf.Session() as sesss:
    output = sesss.run(resulst)
    print(output)