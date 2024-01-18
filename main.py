from PyQt5 import QtSerialPort
from PyQt5.QtCore import Qt

from home import *
from connection import Ui_Dialog as Form

# 1st column of keys
CYCLE_START_PRESSED = '1'

# 2nd column of keys
CYCLE_STOP_PRESSED = '2'

# 3rd column of keys
DRV_PRESSED = '3'
JOG_PRESSED = '4'
X_PRESSED = '5'
PLUS_PRESSED = '6'

# 4th column of keys
Z_LOCK_PRESSED = '7'
MDI_PRESSED = '8'
Y_PRESSED = '9'
VVV_PRESSED = '10'

# 5th column of keys
DRY_RUN_PRESSED = '11'
AUTO_PRESSED = '12'
Z_PRESSED = '13'
MINUS_PRESSED = '14'

# 6th column of keys
NC_REF_PRESSED = '15'
NC_OFFSET_PRESSED = '16'
RET_FOR_PRESSED = '17'
RET_REV_PRESSED = '18'

# 7th column of keys
PRC_END_PRESSED = '19'
ALM_OVR_PRESSED = '20'
ALM_RST_PRESSED = '21'
LOCK_RST_PRESSED = '22'

# 8th column of keys
LASER_ON_PRESSED = '23'
LASER_ON_UNPRESSED = '24'

ALL_BUTTONS_UNPRESSED = '0'

if __name__ == "__main__":
    import sys

    # Press Alt+F4 to close the window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)
    MainWindow.showFullScreen()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    serial = QtSerialPort.QSerialPort()
    ports = QtSerialPort.QSerialPortInfo.availablePorts()


    @QtCore.pyqtSlot()
    def serial_receive():
        while serial.canReadLine():
            data = serial.readLine()
            formatted_data = QtCore.QTextCodec.codecForMib(106).toUnicode(data)
            formatted_data = formatted_data.rstrip('\r\n')
            array_data = list(formatted_data)

            if array_data[0] == '1':
                ui.cycleStartButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.cycleStartButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[1] == '1':
                ui.cycleStopButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.cycleStopButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[2] == '1':
                ui.drvButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.drvButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[3] == '1':
                ui.jogButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.jogButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[4] == '1':
                ui.xButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.xButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[5] == '1':
                ui.plusButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.plusButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[6] == '1':
                ui.zLockButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.zLockButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[7] == '1':
                ui.mdiButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.mdiButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[8] == '1':
                ui.yButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.yButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[9] == '1':
                ui.vvvButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.vvvButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[10] == '1':
                ui.dryRunButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.dryRunButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[11] == '1':
                ui.autoButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.autoButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[12] == '1':
                ui.zButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.zButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[13] == '1':
                ui.minusButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.minusButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[14] == '1':
                ui.ncRefButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.ncRefButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[15] == '1':
                ui.ncOffsetButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.ncOffsetButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[16] == '1':
                ui.retForButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.retForButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[17] == '1':
                ui.retRevButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.retRevButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[18] == '1':
                ui.prcEndButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.prcEndButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[19] == '1':
                ui.almOvrButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.almOvrButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[20] == '1':
                ui.almRstButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.almRstButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[21] == '1':
                ui.lockRstButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            else:
                ui.lockRstButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            # if array_data[22] == '1':
            #     ui.laserOnButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(255, 255, 255)")
            # else:
            #     ui.laserOnButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")

            if array_data[23] == '1':
                ui.laserReadyLamp.setStyleSheet("background-color: rgb(249, 183, 93); color: rgb(96, 96, 96); "
                                                "border-radius: 65px")
            else:
                ui.laserReadyLamp.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255); "
                                                "border-radius: 65px")


    @QtCore.pyqtSlot()
    def serial_send(data_to_send):
        formatted_data = data_to_send.encode()
        serial.write(formatted_data)
        serial.flush()


    def connection_dialog():
        connection = QtWidgets.QDialog()
        connection.ui = Form()
        connection.ui.setupUi(connection)
        for port in ports:
            connection.ui.comboBox.addItem(port.portName())

        connection.ui.pushButton.clicked.connect(lambda: dialog_connect_function())

        @QtCore.pyqtSlot()
        def dialog_connect_function():
            selected_port = connection.ui.comboBox.currentText()
            if not selected_port:
                connection.ui.messageLabel.setText("No port selected")
            else:
                serial.setPortName(selected_port)
                serial.setBaudRate(QtSerialPort.QSerialPort.BaudRate.Baud115200)
                serial.readyRead.connect(lambda: serial_receive())
                serial.setDataTerminalReady(True)
                ret = serial.open(QtSerialPort.QSerialPort.OpenModeFlag.ReadWrite)
                if not ret:
                    connection.ui.messageLabel.setText("Not connected!")
                else:
                    connection.close()

        connection.exec_()


    @QtCore.pyqtSlot()
    def usb_connect_function():
        serial.setPortName("/dev/ttyACM0")
        serial.setBaudRate(QtSerialPort.QSerialPort.BaudRate.Baud115200)
        serial.readyRead.connect(lambda: serial_receive())
        serial.setDataTerminalReady(True)
        ret = serial.open(QtSerialPort.QSerialPort.OpenModeFlag.ReadWrite)
        if not ret:
            serial.setPortName("/dev/ttyACM1")
            ret = serial.open(QtSerialPort.QSerialPort.OpenModeFlag.ReadWrite)
            if not ret:
                serial.setPortName("/dev/ttyACM2")
                ret = serial.open(QtSerialPort.QSerialPort.OpenModeFlag.ReadWrite)
                if not ret:
                    serial.setPortName("/dev/ttyACM3")
                    ret = serial.open(QtSerialPort.QSerialPort.OpenModeFlag.ReadWrite)
                    if not ret:
                        connection_dialog()

    usb_connect_function()

    # set up push button functions---------------------------------------
    @QtCore.pyqtSlot()
    def unpressed_function():
        serial_send(ALL_BUTTONS_UNPRESSED)


    @QtCore.pyqtSlot()
    def cycle_start_function():
        serial_send(CYCLE_START_PRESSED)


    @QtCore.pyqtSlot()
    def cycle_stop_function():
        serial_send(CYCLE_STOP_PRESSED)


    @QtCore.pyqtSlot()
    def drv_function():
        serial_send(DRV_PRESSED)


    @QtCore.pyqtSlot()
    def z_lock_function():
        serial_send(Z_LOCK_PRESSED)


    @QtCore.pyqtSlot()
    def dry_run_function():
        serial_send(DRY_RUN_PRESSED)


    @QtCore.pyqtSlot()
    def jog_function():
        serial_send(JOG_PRESSED)


    @QtCore.pyqtSlot()
    def mdi_function():
        serial_send(MDI_PRESSED)


    @QtCore.pyqtSlot()
    def auto_function():
        serial_send(AUTO_PRESSED)


    @QtCore.pyqtSlot()
    def x_jog_function():
        serial_send(X_PRESSED)


    @QtCore.pyqtSlot()
    def y_jog_function():
        serial_send(Y_PRESSED)


    @QtCore.pyqtSlot()
    def z_jog_function():
        serial_send(Z_PRESSED)


    @QtCore.pyqtSlot()
    def plus_jog_function():
        serial_send(PLUS_PRESSED)


    @QtCore.pyqtSlot()
    def minus_jog_function():
        serial_send(MINUS_PRESSED)


    @QtCore.pyqtSlot()
    def vvv_jog_function():
        serial_send(VVV_PRESSED)


    @QtCore.pyqtSlot()
    def nc_ref_function():
        serial_send(NC_REF_PRESSED)


    @QtCore.pyqtSlot()
    def nc_offset_function():
        serial_send(NC_OFFSET_PRESSED)


    @QtCore.pyqtSlot()
    def ret_for_function():
        serial_send(RET_FOR_PRESSED)


    @QtCore.pyqtSlot()
    def ret_rev_function():
        serial_send(RET_REV_PRESSED)


    @QtCore.pyqtSlot()
    def prc_end_function():
        serial_send(PRC_END_PRESSED)


    @QtCore.pyqtSlot()
    def alm_ovr_function():
        serial_send(ALM_OVR_PRESSED)


    @QtCore.pyqtSlot()
    def alm_rst_function():
        serial_send(ALM_RST_PRESSED)


    @QtCore.pyqtSlot()
    def lock_rst_function():
        serial_send(LOCK_RST_PRESSED)


    @QtCore.pyqtSlot()
    def laser_on_function():
        if ui.laserOnButton.isChecked():
            ui.laserOnButton.setStyleSheet("background-color: rgb(250, 122, 72); color: rgb(96, 96, 96)")
            serial_send(LASER_ON_PRESSED)
        else:
            ui.laserOnButton.setStyleSheet("background-color: rgb(96, 96, 96); color: rgb(255, 255, 255)")
            serial_send(LASER_ON_UNPRESSED)


    ui.cycleStartButton.pressed.connect(lambda: cycle_start_function())
    ui.cycleStopButton.pressed.connect(lambda: cycle_stop_function())
    ui.drvButton.pressed.connect(lambda: drv_function())
    ui.zLockButton.pressed.connect(lambda: z_lock_function())
    ui.dryRunButton.pressed.connect(lambda: dry_run_function())
    ui.jogButton.pressed.connect(lambda: jog_function())
    ui.mdiButton.pressed.connect(lambda: mdi_function())
    ui.autoButton.pressed.connect(lambda: auto_function())
    ui.xButton.pressed.connect(lambda: x_jog_function())
    ui.yButton.pressed.connect(lambda: y_jog_function())
    ui.zButton.pressed.connect(lambda: z_jog_function())
    ui.plusButton.pressed.connect(lambda: plus_jog_function())
    ui.vvvButton.pressed.connect(lambda: vvv_jog_function())
    ui.minusButton.pressed.connect(lambda: minus_jog_function())
    ui.ncRefButton.pressed.connect(lambda: nc_ref_function())
    ui.ncOffsetButton.pressed.connect(lambda: nc_offset_function())
    ui.retForButton.pressed.connect(lambda: ret_for_function())
    ui.retRevButton.pressed.connect(lambda: ret_rev_function())
    ui.prcEndButton.pressed.connect(lambda: prc_end_function())
    ui.almOvrButton.pressed.connect(lambda: alm_ovr_function())
    ui.almRstButton.pressed.connect(lambda: alm_rst_function())
    ui.lockRstButton.pressed.connect(lambda: lock_rst_function())

    ui.cycleStartButton.released.connect(lambda: unpressed_function())
    ui.cycleStopButton.released.connect(lambda: unpressed_function())
    ui.drvButton.released.connect(lambda: unpressed_function())
    ui.zLockButton.released.connect(lambda: unpressed_function())
    ui.dryRunButton.released.connect(lambda: unpressed_function())
    ui.jogButton.released.connect(lambda: unpressed_function())
    ui.mdiButton.released.connect(lambda: unpressed_function())
    ui.autoButton.released.connect(lambda: unpressed_function())
    ui.xButton.released.connect(lambda: unpressed_function())
    ui.yButton.released.connect(lambda: unpressed_function())
    ui.zButton.released.connect(lambda: unpressed_function())
    ui.plusButton.released.connect(lambda: unpressed_function())
    ui.vvvButton.released.connect(lambda: unpressed_function())
    ui.minusButton.released.connect(lambda: unpressed_function())
    ui.ncRefButton.released.connect(lambda: unpressed_function())
    ui.ncOffsetButton.released.connect(lambda: unpressed_function())
    ui.retForButton.released.connect(lambda: unpressed_function())
    ui.retRevButton.released.connect(lambda: unpressed_function())
    ui.prcEndButton.released.connect(lambda: unpressed_function())
    ui.almOvrButton.released.connect(lambda: unpressed_function())
    ui.almRstButton.released.connect(lambda: unpressed_function())
    ui.lockRstButton.released.connect(lambda: unpressed_function())

    ui.laserOnButton.clicked.connect(lambda: laser_on_function())

    MainWindow.show()
    sys.exit(app.exec_())
