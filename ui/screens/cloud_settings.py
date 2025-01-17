from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QComboBox
)
from PyQt6.QtCore import Qt


class CloudSettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main vertical layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Section: Settings
        settings_label = QLabel("Settings")
        settings_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        main_layout.addWidget(settings_label)

        push_data_layout = QVBoxLayout()
        push_data_label = QLabel("Push data to the cloud")
        push_data_dropdown = QComboBox()
        push_data_dropdown.addItems(["Yes", "No"])
        push_data_layout.addWidget(push_data_label)
        push_data_layout.addWidget(push_data_dropdown)
        main_layout.addLayout(push_data_layout)

        # Section: Connection Settings
        connection_settings_label = QLabel("Connection Settings")
        connection_settings_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 20px;")
        main_layout.addWidget(connection_settings_label)

        server_ip_layout = QVBoxLayout()
        server_ip_label = QLabel("Server IP address")
        server_ip_input = QLineEdit()
        server_ip_input.setPlaceholderText("e.g., 64.227.14.140")
        # server_ip_status = QLabel("•")
        # server_ip_status.setStyleSheet("color: green; font-size: 20px;")
        server_ip_layout.addWidget(server_ip_label)
        server_ip_layout.addWidget(server_ip_input)
        # server_ip_layout.addWidget(server_ip_status)
        main_layout.addLayout(server_ip_layout)

        secret_code_layout = QVBoxLayout()
        secret_code_label = QLabel("Secret Code")
        secret_code_input = QLineEdit()
        secret_code_input.setPlaceholderText("e.g., A1B2C3D4E5")
        secret_code_layout.addWidget(secret_code_label)
        secret_code_layout.addWidget(secret_code_input)
        main_layout.addLayout(secret_code_layout)

        # Section: Cloud Storage Settings
        cloud_storage_label = QLabel("Cloud Storage Settings")
        cloud_storage_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 20px;")
        main_layout.addWidget(cloud_storage_label)

        save_event_layout = QVBoxLayout()
        save_event_label = QLabel("Save Event Images to Cloud")
        save_event_dropdown = QComboBox()
        save_event_dropdown.addItems(["Yes", "No"])
        save_event_layout.addWidget(save_event_label)
        save_event_layout.addWidget(save_event_dropdown)
        main_layout.addLayout(save_event_layout)

        save_plate_layout = QVBoxLayout()
        save_plate_label = QLabel("Save Plate Images to Cloud")
        save_plate_dropdown = QComboBox()
        save_plate_dropdown.addItems(["Yes", "No"])
        save_plate_layout.addWidget(save_plate_label)
        save_plate_layout.addWidget(save_plate_dropdown)
        main_layout.addLayout(save_plate_layout)

        # Buttons
        cloud_buttons_layout = QVBoxLayout()
        upload_button = QPushButton("Upload Settings to Cloud")
        download_button = QPushButton("Download Settings from Cloud")
        cloud_buttons_layout.addWidget(upload_button)
        cloud_buttons_layout.addWidget(download_button)
        main_layout.addLayout(cloud_buttons_layout)

        # Save Changes Button
        save_changes_button = QPushButton("Save Changes")
        save_changes_button.setStyleSheet("background-color: blue; color: white; padding: 10px;")
        save_changes_button.setFixedWidth(150)
        main_layout.addWidget(save_changes_button, alignment=Qt.AlignmentFlag.AlignRight)
