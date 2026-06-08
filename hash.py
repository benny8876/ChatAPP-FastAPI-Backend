import bcrypt


class Hash():
    @staticmethod
    def bcrypt(password: str):
        # string ကို bytes အဖြစ် ပြောင်းပေးရပါမယ်
        pw = password.encode('utf-8')[:72]
        return bcrypt.hashpw(pw, bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify(plain_password, hashed_password):
        pw = plain_password.encode('utf-8')[:72]
        return bcrypt.checkpw(pw, hashed_password.encode('utf-8'))
    