import textwrap

from django.http import HttpResponse
from django.views.generic.base import View

class HomePageView(View):
  def dispatch(request, *args, **kwargs):
    response_text = textwrap.dedent('''\
      <!DOCTYPE html>
      <head>
        <title>Hello World</title>
      </head>
      <body>
        <h2>Hello World</h2>
      </body>
      </html>
      
    ''')
    return HttpResponse(response_text)