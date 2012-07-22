from django.db import models

# Create your models here.

from treebeard.mp_tree import MP_Node

class Managed(MP_Node):
    name = models.CharField(max_length=30)
    node_order_by = ['name']

    def __unicode__(self):
        return 'Managed: %s' % self.name
