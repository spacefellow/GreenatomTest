import tensorflow as tf
import keras
import pickle


async def add_score(data):
    with open('ml_service/tokenizer.pickle', 'rb') as f:
        loaded_tokenizer = pickle.load(f)
    model = tf.keras.models.load_model('ml_service/my_model.h5')
    sample_conversion = keras.preprocessing.sequence.pad_sequences(loaded_tokenizer.texts_to_sequences(data))
    prediction = model.predict(sample_conversion)
    return 1 if prediction[0] > 0.5 else 0
