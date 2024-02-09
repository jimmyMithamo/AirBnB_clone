from models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        # initializes Review class
        super().__init__(*args, **kwargs)
        self.place_id = ''
        self.user.id = ''
        self.text = ''
