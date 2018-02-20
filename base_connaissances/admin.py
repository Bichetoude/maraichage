from django.contrib import admin
from .models import Famille
from .models import Espece
from .models import Variete
from .models import Ravageur
from .models import Lutte
from .models import PbCulture
from .models import Action
from .models import Pratique
from .models import ModalitePratique
from .models import PlantesAmies
from .models import ZoneGEO
from .models import PlantesAmies2
from .models import VarieteGenerique


admin.site.register(Famille)
admin.site.register(Espece)
admin.site.register(Variete)
admin.site.register(Ravageur)
admin.site.register(Lutte)
admin.site.register(PbCulture)
admin.site.register(Action)
admin.site.register(Pratique)
admin.site.register(ModalitePratique)
admin.site.register(PlantesAmies)
admin.site.register(ZoneGEO)
admin.site.register(PlantesAmies2)
admin.site.register(VarieteGenerique)
