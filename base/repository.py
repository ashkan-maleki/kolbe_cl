

class BaseRepository():
    def __init__(self):
        self._model = self.Meta.model

    def get_model(self):
        return self._model

    def all(self):
        return self._model.objects.all()

    def create(self, **kwargs):
        return self._model.objects.create(**kwargs)

