from oauth_template.models.model_user import User

fake_users_db = {
    "bino": {
        "username": "bino",
        "full_name": "Bilada Cino",
        "email": "bino@bino.com",
        "hashed_password": "$2b$12$jbJbefYbkq8s3LS0pUx1v.IbSUDn.QO6zewEiC0UYAOr0Wd.1w3ie",
    },
    "borracha": {
        "username": "borracha",
        "full_name": "Borracha Fraca",
        "email": "borracha@borracha.com",
        "hashed_password": "$2b$12$jbJbefYbkq8s3LS0pUx1v.IbSUDn.QO6zewEiC0UYAOr0Wd.1w3ie",
    }
}


class UserDB:

    @staticmethod
    def get_user(username: str):
        if username in fake_users_db:
            user = User(**fake_users_db[username])
        else:
            user = None
        return user
