from __future__ import print_function
from keras.preprocessing import text as ktxt
from data.getData import *
import random
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM

tknizer = ktxt.Tokenizer(num_words=None, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',lower=True, split=" ", char_level=False)
a,b = getData()

# a = [normalSentence(x) for x in a]
# b = [normalSentence(x) for x in b]
tknizer.fit_on_texts(a+b)
a = tknizer.texts_to_sequences(a)
b = tknizer.texts_to_sequences(b)
sents = [[x,1] for x in a] + [[x,0] for x in b]
random.shuffle(sents)
x_train, y_train = [x[0] for x in sents[:5200]], [x[1] for x in sents[:5200]]
x_test, y_test = [x[0] for x in sents[5201:]], [x[1] for x in sents[5201:]]

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 50))
model.add(LSTM(50, dropout=0.05, recurrent_dropout=0.05))
model.add(Dense(1, activation='tanh'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=10,
          validation_data=(x_test, y_test))

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)