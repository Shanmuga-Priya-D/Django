from django.contrib.auth.models import User
from django.conf import settings



                
class EmailAuthBackend():
    def authenticate(self,request,username,password):
        try:
            user=User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self,uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None
        

            
