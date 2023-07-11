import tensorflow as tf
import tensorflow_hub as hub


async def add_score(data):
    embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
    hub_layer = hub.KerasLayer(embedding, input_shape=[],
                               dtype=tf.string, trainable=True)
    model = tf.keras.models.load_model('ml_service/my_model.h5', custom_objects={'KerasLayer': hub_layer})
    prediction = model.predict(data)
    return 1 if prediction[0] > 0.5 else 0
