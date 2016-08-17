from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from odpn.resources import MessageFactory as _

class IResourceExtender(form.Schema):
    """
       Marker/Form interface for ODPN Resource
    """
    field_type =  schema.TextLine(
        title = _(u'Type'),
        required = False,
    )

    authors =  schema.TextLine(
        title = _(u'Authors'),
        required = False,
    )

    # -*- Your Zope schema definitions here ... -*-

alsoProvides(IResourceExtender,IFormFieldProvider)
