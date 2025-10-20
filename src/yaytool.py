import requests as req
import uuid
from errors import LoginError
from user import _post

class Login(_post):
    def __init__(self,email:str,password:any):
        _payload = {
            "email":email,
            "password":password,
            "uuid":str(uuid.uuid4()),
            "api_key":"e9f1ae4c4470f29a92c0168dc42b13637cc332692103f23e626bc2b016f66603"
            
        }

        _loginRes = req.post(
            "https://api.yay.space/v2/users/login_with_email",
            json=_payload,
        )
        
        if(_loginRes.status_code != 201):
            raise LoginError(f"ログインエラー ステータスコード:{_loginRes.status_code}")