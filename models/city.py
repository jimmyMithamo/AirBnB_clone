from models.base_model import BaseModel


class City(BaseModel):
    def __init__(self, *args, **kwargs):
        # initializes user class
        super().__init__(*args, **kwargs)
        self.state_id = ''
        self.name = ''
