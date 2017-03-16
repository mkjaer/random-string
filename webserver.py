import web # http://webpy.org/
import os
import random
        
urls = (
    "/(.+)", "randomoutput",
)

class randomoutput:
    def GET(self, number):
        if number.isdigit():
            valid_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            output = ''.join((random.choice(valid_chars) for i in xrange(int(number))))
        else:
            output = "Please insert a number..."
        return output 

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

