from django.apps import AppConfig
from tf_keras.saving import load_model
from django.conf import settings
import os

class RadiologyConfig(AppConfig):
    name = 'radiology'
    model = None

    def ready(self):
        
        model_path = os.path.join(settings.BASE_DIR, 'models', 'pneumonia_model.h5')
        if not RadiologyConfig.model:
            RadiologyConfig.model = load_model(model_path)
