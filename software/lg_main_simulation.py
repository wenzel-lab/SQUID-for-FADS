from qtpy.QtWidgets import *

app = QApplication([])
app.setStyle('Fusion')
import control.gui as gui

win = gui.OctopiGUI(is_simulation=True)
win.show()
app.exec_()  # sys.exit(app.exec_())
