import os
import json
import uuid
from datetime import datetime




def generate_user_profile(name,age):
    profile={
        "user_id":str(uuid.uuid4()),
        "user_name":name,
        "user_age":age,
        "admit_time":datetime.now().strftime("%d/%m/%Y  %H:%M:%S"),
        "current_folder":os.getcwd()
    }
    return json.dumps(profile,indent=4)