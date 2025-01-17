from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
)
from PyQt6.QtCore import Qt
# from io.database import Database  # Import the Database class
from database.database import Database
from ui.dialogs.controller_dialog import AddEditControllerDialog  # Optional: move dialog to its own file


class ControllerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()  # Initialize the Database
        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Add New Controller Button
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add New Controller")
        add_button.setStyleSheet("background-color: blue; color: white; padding: 5px 10px;")
        add_button.setFixedWidth(150)
        add_button.clicked.connect(self.show_add_controller_dialog)
        button_layout.addStretch()
        button_layout.addWidget(add_button)
        main_layout.addLayout(button_layout)

        # Table for Controllers
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Controller Name", "Role", "API URL", "Linked Cameras", "Actions"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        self.table.setColumnWidth(4, 150)

        # Add table to layout
        main_layout.addWidget(self.table)

        # Load data from the database
        self.load_data()

    def load_data(self):
        """
        Load data from the database and populate the table.
        """
        self.table.setRowCount(0)  # Clear the table
        rows = self.db.fetch_all()

        for row in rows:
            self.add_table_row(*row)

    def add_table_row(self, row_id, controller_name, role, api_url, linked_cameras):
        """
        Add a row to the table with the specified details.
        """
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Populate cells
        self.table.setItem(row_position, 0, QTableWidgetItem(controller_name))
        self.table.setItem(row_position, 1, QTableWidgetItem(role))
        self.table.setItem(row_position, 2, QTableWidgetItem(api_url))
        self.table.setItem(row_position, 3, QTableWidgetItem(linked_cameras))

        # Add Edit and Delete buttons in the Actions column
        actions_widget = QWidget()
        actions_layout = QHBoxLayout(actions_widget)

        edit_button = QPushButton("Edit")
        delete_button = QPushButton("Delete")
        edit_button.setStyleSheet("color: blue; padding: 2px 5px;")
        delete_button.setStyleSheet("color: red; padding: 2px 5px;")

        # Connect buttons to actions
        edit_button.clicked.connect(lambda: self.show_edit_controller_dialog(row_id))
        delete_button.clicked.connect(lambda: self.delete_controller(row_id))

        actions_layout.addWidget(edit_button)
        actions_layout.addWidget(delete_button)
        actions_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.table.setCellWidget(row_position, 4, actions_widget)

    def show_add_controller_dialog(self):
        """
        Show a dialog to add a new controller.
        """
        dialog = AddEditControllerDialog(self)
        if dialog.exec():
            data = dialog.get_data()

            # Validate input
            if not data["name"] or not data["role"] or not data["api_url"]:
                QMessageBox.warning(self, "Validation Error", "Please fill in all required fields.")
                return

            # Insert into database
            self.db.insert(data["name"], data["role"], data["api_url"], data["linked_cameras"])

            # Refresh the table
            self.load_data()

    def show_edit_controller_dialog(self, row_id):
        """
        Show a dialog to edit an existing controller.
        """
        row = self.db.fetch_one(row_id)
        if row:
            controller_data = {
                "name": row[0],
                "role": row[1],
                "api_url": row[2],
                "linked_cameras": row[3],
            }
            dialog = AddEditControllerDialog(self, controller_data)
            if dialog.exec():
                data = dialog.get_data()

                # Update database
                self.db.update(row_id, data["name"], data["role"], data["api_url"], data["linked_cameras"])

                # Refresh the table
                self.load_data()

    def delete_controller(self, row_id):
        """
        Delete a controller from the database.
        """
        confirm = QMessageBox.question(
            self, "Confirm Delete", "Are you sure you want to delete this controller?"
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.db.delete(row_id)
            self.load_data()
