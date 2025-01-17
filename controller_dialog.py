from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QComboBox,
    QPushButton,
)
from PyQt6.QtCore import Qt


class AddEditControllerDialog(QDialog):
    def __init__(self, parent=None, controller_data=None):
        """
        A dialog for adding or editing a controller.

        :param parent: The parent widget.
        :param controller_data: A dictionary with existing controller data (for editing).
        """
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Controller")
        self.setFixedSize(400, 300)
        self.controller_data = controller_data

        # Main layout
        layout = QVBoxLayout()

        # Controller Name
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Controller Name")
        layout.addWidget(QLabel("Controller Name:"))
        layout.addWidget(self.name_input)

        # Role Dropdown
        self.role_dropdown = QComboBox()
        self.role_dropdown.addItems(["Entry", "Exit", "Entry & Exit"])
        layout.addWidget(QLabel("Role:"))
        layout.addWidget(self.role_dropdown)

        # API URL
        self.api_url_input = QLineEdit()
        self.api_url_input.setPlaceholderText("e.g., https://api.example.com")
        layout.addWidget(QLabel("API URL:"))
        layout.addWidget(self.api_url_input)

        # Linked Cameras
        self.linked_cameras_input = QLineEdit()
        self.linked_cameras_input.setPlaceholderText("Linked Cameras (comma-separated)")
        layout.addWidget(QLabel("Linked Cameras:"))
        layout.addWidget(self.linked_cameras_input)

        # Pre-fill data if editing
        if self.controller_data:
            self.name_input.setText(controller_data.get("name", ""))
            self.role_dropdown.setCurrentText(controller_data.get("role", "Entry"))
            self.api_url_input.setText(controller_data.get("api_url", ""))
            self.linked_cameras_input.setText(controller_data.get("linked_cameras", ""))

        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")

        save_button.clicked.connect(self.accept)  # Close dialog and return success
        cancel_button.clicked.connect(self.reject)  # Close dialog without saving

        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_data(self):
        """
        Get the data entered in the dialog.

        :return: A dictionary with the entered data.
        """
        return {
            "name": self.name_input.text(),
            "role": self.role_dropdown.currentText(),
            "api_url": self.api_url_input.text(),
            "linked_cameras": self.linked_cameras_input.text(),
        }
