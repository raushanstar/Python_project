import  string
import random
class Password:
    def __init__(self,charset,lengh):
        self.charset=charset
        self.length=lengh
        self.char_array=[]
        self.passw=[]
    def set_charset(self):
        if ('u' in self.charset):
            self.char_array.append(string.ascii_uppercase)
        if ('l' in self.charset):
            self.char_array.append(string.ascii_lowercase)
        if ('d' in self.charset):
            self.char_array.append(string.digits)
        if ('s' in self.charset):
            self.char_array.append(string.punctuation)
    # def get_char_array(self):
    #     return self.char_array
    def generate_password(self):
        # print(self.char_array)
        for i in range((self.length)):
            outer_index=random.randrange(0,len(self.char_array))
            inner_index=random.randrange(0,len(self.char_array[outer_index]))
            self.passw.append(self.char_array[outer_index][inner_index])
    def get_password(self):
        return ''.join(self.passw)
a=input("enter symbol for\nLowerCase=l"
        "\nUpperCase=u"
        "\ndigits=d"
        "\nspacialCase=p\n",)
password=Password(a,8)
password.set_charset()
password.generate_password()
print("The random password is : ",password.get_password())