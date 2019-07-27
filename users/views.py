from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "%s %s"%(self.first_name,self.last_name)

    def get_fullname(self):
        return "%s %s"%(self.first_name,self.last_name)

name_list = [
    User('hamid','saeedi'),
    User('sina','qolami'),
    User('jafar','hashemi')
]


message = ["hi"]
@ensure_csrf_cookie
def chat (req):
    try:
        resp = ""
        print('user list:', req.GET)
        for name in name_list:
            resp += name.get_fullname()
        # return HttpResponse("the list is: %s" %resp)
        if "mssg" in req.POST:
            # print('mssg:', req.POST["mssg"])
            message.append(req.POST["mssg"])
            return render(
                    req ,
                    "userlist.html" , context = {"message":message, "name":resp, "users": name_list}
                )
        else:
            return render(
                    req ,
                    "userlist.html" , context = {"message":message, "name":resp, "users": name_list}
                )

    except:
        print("an error occured")
    



    
    