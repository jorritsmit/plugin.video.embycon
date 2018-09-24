import xbmc
import xbmcaddon
import xbmcgui

from simple_logging import SimpleLogging

log = SimpleLogging(__name__)


class ServerInfo():

    name = ""
    host = ""
    port = 0
    secure = False


class ServerSelect(xbmcgui.WindowXMLDialog):

    selected_action = None
    action_items = None

    def __init__(self, *args, **kwargs):
        log.debug("SelectServer: __init__")
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        log.debug("SelectServer: onInit")
        self.action_exitkeys_id = [10, 13]

        self.listControl = self.getControl(3000)
        self.listControl.addItems(self.action_items)
        self.setFocus(self.listControl)

    def setActionItems(self, action_items):
        self.action_items = action_items

    def onFocus(self, controlId):
        pass

    def doAction(self, actionID):
        pass

    def onClick(self, controlID):
        if controlID == 3000:
            self.selected_action = self.listControl.getSelectedItem()
            log.debug("SelectServer: Selected Item: {0}", self.selected_action)
            self.close()

        elif controlID == 3011:
            settings = xbmcaddon.Addon()
            path = settings.getAddonInfo('path')
            path = xbmc.translatePath(path)
            server_add = ServerInfoEdit("ServerInfoEdit.xml", path, "default", "720p")
            server_add.doModal()

            log.debug("SelectServer : New Server : {0}", server_add.server_info.name)

        elif controlID == 3012:
            settings = xbmcaddon.Addon()
            path = settings.getAddonInfo('path')
            path = xbmc.translatePath(path)
            action_menu = ServerInfoEdit("ServerInfoEdit.xml", path, "default", "720p")
            action_menu.doModal()

        elif controlID == 3013:
            index = self.listControl.getSelectedPosition()
            log.debug("SelectServer: Deleting Item: {0}", index)
            self.listControl.removeItem(index)

    def getActionItem(self):
        return self.selected_action


class ServerInfoEdit(xbmcgui.WindowXMLDialog):

    server_info = None
    action_exitkeys_id = [10, 13]

    def __init__(self, *args, **kwargs):
        log.debug("ServerInfoEdit: __init__")
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        log.debug("ServerInfoEdit: onInit")
        self.action_exitkeys_id = [10, 13]

    def onClick(self, controlID):
        if controlID == 3010:

            info = ServerInfo()
            info.name = "New Server Name HERE"
            info.host = "127.0.0.1"
            info.port = 8096
            info.secure = False

            self.server_info = info
            self.close()
