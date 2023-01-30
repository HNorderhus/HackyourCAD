from pivy import coin
from freecad import FreeCAD as App
from freecad import FreeCADGui as Gui

BOARD_LABELS = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]

class OneMove:
    def __init__(self):
        self.view = Gui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.getElements)
        self.token = None
        self.target_field = None

    def getElements(self, event_cb):
        event = event_cb.getEvent()
        if event.getButton() == 1: # left mouse button
            if event.getState() == coin.SoMouseButtonEvent.DOWN:
                selection = Gui.Selection.getSelection()[0]
                if selection.Label in BOARD_LABELS:
                    self.target_field = App.ActiveDocument.getObjectsByLabel(selection.Label)
                    print("Selected target field")
                else:
                    self.token = App.ActiveDocument.getObjectsByLabel(selection.Label)

                    print("Selected token")

        else: # event.getButton() == 3:
            self.view.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.callback)

    def moveToken(self):
        x = self.target_field.Placement.Base.x
        y = self.target_field.Placement.Base.y

        mid_x = x + (self.target_field.Length.Value / 2)
        mid_y = y + (self.target_field.Width.Value / 2)

        self.token.Placement.Base.x = mid_x
        self.token.Placement.Base.y = mid_y


move = OneMove()