from abc import ABC, abstractmethod

class Authentication(ABC):
    def login(self, username, credential):
        if not username:
            return "Username required"
        return self.validate(username, credential)
    @abstractmethod
    def validate(self, username, credential):
        pass
class PasswordAuth(Authentication):

    def validate(self, username, password):
        if password == "admin123":
            return "Password Login Successful"
        return "Invalid Password"
class OTPAuth(Authentication):

    def validate(self, username, otp):
        if otp == "9999":
            return "OTP Login Successful"
        return "Invalid OTP"
auth1 = PasswordAuth()
print(auth1.login("john", "admin123"))
auth2 = OTPAuth()
print(auth2.login("john", "9999"))
