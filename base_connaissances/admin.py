from django.contrib import admin
from .models import TypeCulture
from .models import Espece
from .models import Variete
from .models import Envahisseur
from .models import SituationGEO
from .models import TypeProduction
from .models import Action
from .models import Lutte
from .models import Realistation


admin.site.register(TypeCulture)
admin.site.register(Espece)
admin.site.register(Variete)
admin.site.register(Envahisseur)
admin.site.register(SituationGEO)
admin.site.register(TypeProduction)
admin.site.register(Action)
admin.site.register(Lutte)
admin.site.register(Realistation)
