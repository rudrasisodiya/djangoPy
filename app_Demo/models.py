from django.db import models

# Create your models here.

class Destination:

    id : int
    location : str
    price : int
    desc : str
    img : str
    offer : bool