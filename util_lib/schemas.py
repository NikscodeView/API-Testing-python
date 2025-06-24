from pydantic import BaseModel

class UserSchema(BaseModel):
    Mfr_ID: int
    Country: str
    Mfr_CommonName: str
