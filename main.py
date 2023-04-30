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
        
        mode_file = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
        #checks for VPC in the filename if VPC2004:00 doesn't exist 
        if not os.path.isfile(mode_file):
            files = [f for f in os.listdir("/sys/bus/platform/drivers/ideapad_acpi/") if "VPC" in f]
            if len(files) > 0:
                mode_file = "/sys/bus/platform/drivers/ideapad_acpi/" + files[0] + "/conservation_mode"
            else:
                print("Error: could not find conservation_mode file for Lenovo laptop")
                return

        if state == 2:
            command = 'sudo echo 1 > ' + mode_file
            os.system(command)
        else:
            command = 'sudo echo 0 > ' + mode_file
            os.system(command)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
