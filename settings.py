
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox
)


class DeviceConfigurationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main vertical layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Section: Device Configuration Title
        title_label = QLabel("Device Configuration")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(title_label)

        # Device Unique ID
        unique_id_layout = QVBoxLayout()
        unique_id_label = QLabel("Device Unique ID")
        unique_id_value = QLabel("3f6a2c4d8e9b")
        unique_id_value.setStyleSheet("background-color: #ddd; padding: 5px; border: 1px solid #aaa;")
        unique_id_layout.addWidget(unique_id_label)
        unique_id_layout.addWidget(unique_id_value)
        unique_id_layout.addStretch()

        main_layout.addLayout(unique_id_layout)

        # Secret Code
        secret_code_layout = QVBoxLayout()
        secret_code_layout_h = QHBoxLayout()
        secret_code_label = QLabel("Secret Code")
        secret_code_value = QLabel("A7x9P3Qk")

        secret_code_value.setStyleSheet("background-color: #ddd; padding: 5px; border: 1px solid #aaa;")
        generate_code_button = QPushButton("Generate New Secret Code")
        secret_code_layout.addWidget(secret_code_label)

 
        secret_code_layout_h.addWidget(secret_code_value)
        secret_code_layout_h.addWidget(generate_code_button)
        secret_code_layout_h.addStretch()
        secret_code_layout.addLayout(secret_code_layout_h)


        main_layout.addLayout(secret_code_layout)
        # main_layout.addLayout(secret_code_layout_h)

        # Company Identifier
        company_id_layout = QVBoxLayout()
        company_id_label = QLabel("Company Identifier")
        company_id_input = QLineEdit("3f6a2c4d8e9b")
        company_id_layout.addWidget(company_id_label)
        company_id_layout.addWidget(company_id_input)
        company_id_layout.addStretch()

        main_layout.addLayout(company_id_layout)

        # Timezone
        timezone_layout = QVBoxLayout()
        timezone_label = QLabel("Timezone")
        timezone_combo = QComboBox()
        timezone_combo.addItems(["Central European Time (CET): UTC +1", "Eastern Time (ET): UTC -5", "Pacific Time (PT): UTC -8"])
        timezone_layout.addWidget(timezone_label)
        timezone_layout.addWidget(timezone_combo)
        main_layout.addLayout(timezone_layout)

        # Region/Country
        region_layout = QVBoxLayout()
        region_label = QLabel("Region/Country")
        region_combo = QComboBox()
        region_combo.addItems(["North America / United States", "Europe / Germany", "Asia / Japan"])
        region_layout.addWidget(region_label)
        region_layout.addWidget(region_combo)
        main_layout.addLayout(region_layout)

        # Spacer
        main_layout.addStretch()

        # Buttons
        button_layout = QHBoxLayout()
        factory_reset_button = QPushButton("Factory Reset")
        factory_reset_button.setStyleSheet("background-color: red; color: white; padding: 10px;")
        save_button = QPushButton("Save Changes")
        save_button.setStyleSheet("background-color: blue; color: white; padding: 10px;")
        button_layout.addWidget(factory_reset_button)
        button_layout.addStretch()
        button_layout.addWidget(save_button)
        main_layout.addLayout(button_layout)
