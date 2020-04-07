from java.awt import Component
from java.awt import FlowLayout
from java.awt import Panel
from java.awt.event import ActionEvent
from java.awt.event import ActionListener
from javax.swing import JButton
from javax.swing import JLabel
from java.awt import BorderLayout
from javax.swing import JCheckBox
from javax.swing import JTable
from javax.swing import JScrollPane
from javax.swing.table import DefaultTableModel
from javax.swing import JTextArea
from java.io import PrintWriter
from utils import Helpers


class GUI(Helpers):

    def gui(self):

        x = 10  # panel padding
        y = 5  # panel padding

        self.panel = Panel()
        self.panel.setLayout(None)
        self.scn_lbl = JLabel("Enable scanning")
        self.scn_lbl.setBounds(x, y, 100, 20)
        self.panel.add(self.scn_lbl)
        self.enable = JCheckBox()
        self.enable.setBounds(x + 120, y, 50, 20)
        self.panel.add(self.enable)

        self.rand_lbl = JLabel("Randomize payloads")
        self.rand_lbl.setBounds(x, y + 15, 100, 20)
        self.panel.add(self.rand_lbl)
        self.randomize = JCheckBox()
        self.randomize.setBounds(x + 120, y + 15, 50, 20)
        self.panel.add(self.randomize)

        self.pyld_lbl = JLabel("Payloads List (Line separated)")
        self.pyld_lbl.setBounds(x, y + 30, 180, 20)
        self.panel.add(self.pyld_lbl)

        self.payloads_list = JTextArea()
        self.pyld_scrl = JScrollPane(self.payloads_list)
        self.pyld_scrl.setBounds(x, y + 50, 600, 200)
        self.panel.add(self.pyld_scrl)

        self.save_btn = JButton("Save", actionPerformed=self.save_settings)
        self.save_btn.setBounds(x, y + 250, 100, 30)
        self.panel.add(self.save_btn)

        # Settings loader from [utils/Helpers/load_settings]
        self.load_settings()
        return self