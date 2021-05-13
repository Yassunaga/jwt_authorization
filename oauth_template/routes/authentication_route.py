from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from oauth_template.models.model_user import Token
from oauth_template.modules.user_module import authenticate, create_access_token, validate_token

router = APIRouter()


@router.post("/token", response_model=Token)
def get_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_data = authenticate(form_data.username, form_data.password)
    access_token = create_access_token(data={"sub": user_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/validate/token')
def token_validation(user=Depends(validate_token)):
    return dict(user)
