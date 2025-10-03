import sys , os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from Objects.variables import general_variables


class css_gui_class():
    def __init__(self, root):
        self.root = root