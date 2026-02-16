from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
import re

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        
        if username is None or password is None:
            return None
        
     
        normalized_username = self.normalize_username(username)
        
        try:
          
            user = UserModel.objects.get(
                Q(username=username) | 
                Q(email=normalized_username) | 
                Q(phone_number=normalized_username)
            )
        except UserModel.DoesNotExist:
            return None
        except UserModel.MultipleObjectsReturned:
            
            user = UserModel.objects.filter(
                Q(username=username) |
                Q(email=normalized_username) | 
                Q(phone_number=normalized_username)
            ).first()
        else:
            
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        
        return None
    
    def normalize_username(self, username):
        """Нормализует имя пользователя для поиска"""
        if '@' in username:
            return username.lower()
        
       
        phone = re.sub(r'[^\d+]', '', username)
        if phone.startswith('8'):
            phone = '+7' + phone[1:]
        elif phone.startswith('7'):
            phone = '+' + phone
        elif not phone.startswith('+7'):
            phone = '+7' + phone
        
        return phone