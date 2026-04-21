# 9. Вычислить значения линейной функции вида: 3 x+ 5 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


x = np.array([-10, -5, 0, 5, 10, 15, 20])
y = np.array([-25, -10, 5, 20, 35, 50, 65])

model = Sequential()
model.add(Dense(units=1, input_shape=(1,), activation='linear'))
model.compile(loss='mean_squared_error', optimizer=Adam(0.1))
log = model.fit(x, y, epochs=500, verbose=False)

plt.plot(log.history['loss'])
plt.grid(True)
plt.show()

print("Веса модели:", model.get_weights())
print("Предсказание для x=100:", model.predict(np.array([[100]])))