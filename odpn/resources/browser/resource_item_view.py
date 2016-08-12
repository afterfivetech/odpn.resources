from five import grok
from plone.directives import dexterity, form
from odpn.resources.content.resource_item import IResourceItem

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IResourceItem)
    grok.require('zope2.View')
    grok.template('resource_item_view')
    grok.name('view')

