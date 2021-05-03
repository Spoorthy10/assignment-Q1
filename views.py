from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def loginpage(request):
    data = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>project login page</title>
    </head>
    <body>

    <form>
        Username:<input style="margin-top: 60px;" type="text" id="inp"  placeholder="enter username"><br><br>
        Password:<input type="text" id="pw" placeholder="enter password"><br><br>
        <button>sign in</button>

        <p>don't have an account?</p>
        <button>sign up</button>
    </form>
    </section>
    </body>
    </html>
    """
    return HttpResponse(data)