from collective.grok import gs
from odpn.resources import MessageFactory as _

@gs.importstep(
    name=u'odpn.resources', 
    title=_('odpn.resources import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('odpn.resources.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
