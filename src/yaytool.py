import requests as req
import uuid
import math
import time
from errors import yaytoolError
from post import _post

class Login:
    def __init__(self,email:str="",password:any=""):
        if(email and password):
            self._uuid = str(uuid.uuid4())
            self._email = email
            self._password = password
            _payload = {
                "email":self._email,
                "password":str(self._password),
                "uuid":self._uuid,
                "api_key":"e9f1ae4c4470f29a92c0168dc42b13637cc332692103f23e626bc2b016f66603"
                
            }

            _loginRes = req.post(
                "https://api.yay.space/v2/users/login_with_email",
                json=_payload,
            )
            
            if(_loginRes.status_code != 201):
                addMessage = "\n"
                if(_loginRes.status_code == 429):
                    addMessage += "サーバーへのリクエストが多すぎます"
                raise yaytoolError(f"エラー ステータスコード:{str(_loginRes.status_code) + addMessage}")
            self._loginData = _loginRes.json()

        
    def post(self,text:str):
        _payload = {
            "color":"0",
            "font_size":"0",
            "language":None,
            "message_tags":"[]",
            "post_type":"text",
            "text":text,
            "uuid":self._uuid
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            "https://yay.space/api/posts",
            json=_payload,
            headers=headers
        )
        
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
        _res = _res.json()
        
        return _post(_res)
    
    def repost(self,repostId:str,text:str):
        _payload = {
            "in_reply_to":repostId,
            "color":"0",
            "font_size":"0",
            "language":None,
            "message_tags":"[]",
            "post_type":"text",
            "text":text,
            "uuid":self._uuid
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            "https://yay.space/api/posts",
            json=_payload,
            headers=headers
        )
        
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
        _res = _res.json()
        
        return _post(_res)
                
    def like(self,postId):
        _payload = {
            "post_ids":[postId]
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            "https://api.yay.space/v2/posts/like",
            json=_payload,
            headers=headers
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                
    def follow(self,userId):
        _payload = {
            "userId":[userId]
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            f"https://api.yay.space/v2/users/{userId}/follow",
            json=_payload,
            headers=headers
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                
    def unfollow(self,userId):
        _payload = {
            "userId":[userId]
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            f"https://api.yay.space/v2/users/{userId}/unfollow",
            json=_payload,
            headers=headers
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                
    def removepost(self,postId):
        _payload = {
            "posts_ids":[postId]
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            f"https://api.yay.space/v2/posts/mass_destroy",
            json=_payload,
            headers=headers
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
        
    def block(self,userId):
        _payload = {
            "result":"success"
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            f"https://api.yay.space/v1/users/{userId}/block",
            json=_payload,
            headers=headers
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
        
    def unblock(self,userId):
        _payload = {
            "result":"success"
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            f"https://api.yay.space/v2/users/{userId}/unblock",
            json=_payload,
            headers=headers
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                
    def gettimeline(self,number:int=100):
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }
        
        _timelines = []
        
        for i in range(math.ceil(number/100)):
            if(i == math.ceil(number/100)-1):
                # print(f"https://api.yay.space/v2/posts/timeline?mxn={i+1}&number={number%100 or 100}&order_by=hot_first&reduce_selfie=true&shared_interest_categories=false")
                _res = req.get(
                    f"https://api.yay.space/v2/posts/timeline?mxn={i+1}&number={number%100 or 100}&order_by=hot_first&reduce_selfie=true&shared_interest_categories=false",
                    headers=headers
                    )
                
                if(not(_res.status_code in [200,201])):
                    addMessage = "\n"
                    if(_res.status_code == 429):
                        addMessage += "サーバーへのリクエストが多すぎます"
                    raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                _res = _res.json()
                _timelines.append(_res)
                
            else:
                _res = req.get(f"https://api.yay.space/v2/posts/timeline?mxn={i+1}&number={100}&order_by=hot_first&reduce_selfie=true&shared_interest_categories=false")
                
                if(not(_res.status_code in [200,201])):
                    addMessage = "\n"
                    if(_res.status_code == 429):
                        addMessage += "サーバーへのリクエストが多すぎます"
                    raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                _res = _res.json()
                _timelines.append(_res)

        return _timelines
        
    def getlikers(self,postId):        
        _res = req.get(f"https://api.yay.space/v1/posts/{postId}/likers")
        
        if(not(_res.status_code in [200,201])):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
        _res = _res.json()
        # print(_res)
        
    def invitecall(self,callId:str,userId:str):
        
        files = [
            ("user_ids[]", (None,str(userId)))
        ]
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            f"https://api.yay.space/v1/calls/conference_calls/{callId}/invite",
            files=files,
            headers=headers
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
        
        # print(_res.json())

    def getmutalfollow(self,userId,number=50):    
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }
        
        _ress = []
        nextvalue = ""
        
        for i in range(math.ceil(number / 50)):
            if(i==0):
                _res = req.get(
                    f"https://api.yay.space/v3/users/{userId}/followers?number={number%50 or number}",
                    headers=headers,
                    )
                
                if(not(_res.status_code in [200,201])):
                    addMessage = "\n"
                    if(_res.status_code == 429):
                        addMessage += "サーバーへのリクエストが多すぎます"
                    raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                _res = _res.json()
                _ress.append(_res["users"])
                
                nextvalue = _res["next_page_value"]
            elif(i==math.ceil(number / 50) - 1):
                _res = req.get(
                    f"https://api.yay.space/v3/users/{userId}/followers?number={number%50}",
                    headers=headers,
                    )
                
                if(not(_res.status_code in [200,201])):
                    addMessage = "\n"
                    if(_res.status_code == 429):
                        addMessage += "サーバーへのリクエストが多すぎます"
                    raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                _res = _res.json()
                _ress.append(_res["users"])
                
                nextvalue = _res["next_page_value"]
            else:
                _res = req.get(
                    f"https://api.yay.space/v3/users/{userId}/followers?from={nextvalue}&number=50",
                    headers=headers,
                    )
                
                if(not(_res.status_code in [200,201])):
                    addMessage = "\n"
                    if(_res.status_code == 429):
                        addMessage += "サーバーへのリクエストが多すぎます"
                    raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
                _res = _res.json()
                _ress.append(_res["users"])
                
                nextvalue = _res["next_page_value"]
                
        _endres = [d for dd in _ress for d in dd]
                            
        return _endres
    
    def editName(self,newName:str):
        _payload = {
            "biography":"hello world",
            "nickname":str(newName)
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            f"https://api.yay.space/v3/users/edit",
            headers=headers,
            json=_payload,
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")

    def muteUser(self,callId:str,target_user_uuid:str):
        _payload = {
            "action":"mute",
            "conference_id":callId,
            "target_user_uuid":target_user_uuid
        }
        
        headers = {
            "Authorization": f"Bearer {self._loginData["access_token"]}",
        }

        _res = req.post(
            f"https://api.yay.space/v1/calls/action_signature/generate",
            headers=headers,
            json=_payload,
        )
        
        if(_res.status_code != 201):
            addMessage = "\n"
            if(_res.status_code == 429):
                addMessage += "サーバーへのリクエストが多すぎます"
            raise yaytoolError(f"エラー ステータスコード:{str(_res.status_code) + addMessage}")
