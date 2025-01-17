import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem, QWidget, QGridLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont

from ui.screens.settings import DeviceConfigurationPage
from ui.screens.cloud_settings import CloudSettingsPage
from ui.screens.gate_controllers import ControllerPage
# Import the UI class from the 'main_ui' module
from main_ui import Ui_MainWindow


# Define a custom MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the UI from the generated 'main_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window properties
        self.setWindowIcon(QIcon("./icon/Logo.png"))
        self.setWindowTitle("GateGuardX")

        # Initialize UI elements
        self.title_label = self.ui.title_label
        self.title_label.setText("GateGuardX")

        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        # self.title_icon.setPixmap(QPixmap("./icon/Logo.png"))
        self.title_icon.setScaledContents(True)

        self.side_menu = self.ui.listWidget
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only = self.ui.listWidget_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only.hide()

        self.menu_btn = self.ui.menu_btn
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon("./icon/close.svg"))
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)

        self.main_content = self.ui.stackedWidget

        # Define a list of menu items with names and icons
        self.menu_list = [
            {
                "name": "General Settings",
                "icon": "./icon/dashboard.svg",
                "widget":  DeviceConfigurationPage()
            },
            {
                "name": "Cloud",
                "icon": "./icon/orders.svg",
                "widget":  CloudSettingsPage()
            },
            {
                "name": "Gate Controller",
                "icon": "./icon/products.svg",
                "widget":  ControllerPage()
            },
            {
                "name": "Cameras",
                "icon": "./icon/customers.svg",
                "widget":  QLabel("Cameras")
            },
            {
                "name": "License Plate Recognition",
                "icon": "./icon/reports.svg",
                "widget":  QLabel("License Plate Recognition")
            },
            {
                "name": "System Health",
                "icon": "./icon/settings.svg",
                "widget":  QLabel("System Health")
            },
        ]

        # Initialize the UI elements and slots
        self.init_list_widget()
        self.init_stackwidget()
        self.init_single_slot()

    def init_single_slot(self):
        # Connect signals and slots for menu button and side menu
        self.menu_btn.toggled['bool'].connect(self.side_menu.setHidden)
        self.menu_btn.toggled['bool'].connect(self.title_label.setHidden)
        self.menu_btn.toggled['bool'].connect(self.side_menu_icon_only.setVisible)
        self.menu_btn.toggled['bool'].connect(self.title_icon.setHidden)

        # Connect signals and slots for switching between menu items
        self.side_menu.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged['int'].connect(self.side_menu_icon_only.setCurrentRow)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.side_menu.setCurrentRow)
        self.menu_btn.toggled.connect(self.button_icon_change)

    def init_list_widget(self):
        # Initialize the side menu and side menu with icons only
        self.side_menu_icon_only.clear()
        self.side_menu.clear()

        for menu in self.menu_list:
            # Set items for the side menu with icons only
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setSizeHint(QSize(40, 40))
            self.side_menu_icon_only.addItem(item)
            self.side_menu_icon_only.setCurrentRow(0)

            # Set items for the side menu with icons and text
            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu.get("icon")))
            item_new.setText(menu.get("name"))
            self.side_menu.addItem(item_new)
            self.side_menu.setCurrentRow(0)

    def init_stackwidget(self):
        # Initialize the stack widget with content pages
        widget_list = self.main_content.findChildren(QWidget)
        for widget in widget_list:
            self.main_content.removeWidget(widget)

        for menu in self.menu_list:
            # text = menu.get("name")
            layout = QGridLayout()
            widget = menu.get("widget")

            # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            # font = QFont()
            # font.setPixelSize(20)
            # label.setFont(font)
            layout.addWidget(widget)
            new_page = QWidget()
            new_page.setLayout(layout)
            self.main_content.addWidget(new_page)

    def button_icon_change(self, status):
        # Change the menu button icon based on its status
        if status:
            self.menu_btn.setIcon(QIcon("./icon/open.svg"))
        else:
            self.menu_btn.setIcon(QIcon("./icon/close.svg"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load style file
    with open("style.qss") as f:
        style_str = f.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
