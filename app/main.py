from typing import Optional
import os
from fastapi import FastAPI, Security
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()

warpspeed_jwt = os.getenv('OAUTH_URL','/token')

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=warpspeed_jwt,
    description="OAuth2PasswordBearer security scheme",
    auto_error=False,
)


@app.get("/users/me")
async def read_items(token: Optional[str] = Security(oauth2_scheme)):
    if token is None and os.getenv('SOLARLUNAR_ENV') == 'local':
        return {"msg": "call logic to run in local env"}
    return {"token": token}
