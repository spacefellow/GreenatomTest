import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
import os
import pickle

url = 'https://disk.yandex.ru/client/disk/aclImdb'
origin_dir = 'C:\\programes\\greenatom\\src\\ml_service'
train_dir = url + '/train'
test_dir = origin_dir + '/test'
texts = []
labels = []
for fname in os.listdir(train_dir + '\\neg'):
    with open(train_dir + '\\neg\\' + fname, 'r', encoding='utf8') as f:
        texts.append(f.read())
    labels.append(0)
for fname in os.listdir(train_dir + '\\pos'):
    with open(train_dir + '\\pos\\' + fname, 'r', encoding='utf8') as f:
        texts.append(f.read())
    labels.append(1)

maxlen = 1000
max_words = 10000

tokenizer = keras.preprocessing.text.Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
data = keras.preprocessing.sequence.pad_sequences(sequences, maxlen=maxlen)

indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = np.array(labels)[indices]

model = tf.keras.Sequential([
    keras.layers.Embedding(max_words + 1, 16),
    keras.layers.Dropout(0.2),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(1, activation='sigmoid')])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

history = model.fit(data, labels, epochs=10, batch_size=32, validation_split=0.2)

loss, accuracy = model.evaluate(data, labels)

print("Loss: ", loss)
print("Accuracy: ", accuracy)
model.save('my_model.h5')
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
