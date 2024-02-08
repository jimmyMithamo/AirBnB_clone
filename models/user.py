from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        #initializes user class 
        super().__init__(*args, **kwargs)
        self.email = None
        self.password = None
        self.first_name = None
        self.last_name = None

