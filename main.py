from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout
import os
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.checkbox = QCheckBox('Conservation Mode', self)
        self.checkbox.move(20, 20)
        self.checkbox.setChecked(True)

        self.checkbox.stateChanged.connect(self.change_mode)

        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

        self.check_permissions()

    def check_permissions(self):
        mode_file = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
        if os.access(mode_file, os.W_OK):
            return
        else:
            os.system("sudo chmod 666 " + mode_file)

    def change_mode(self, state):
        if state == 2:
            command = 'sudo echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode'
            os.system(command)
        else:
            command = 'sudo echo 0 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode'
            os.system(command)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
