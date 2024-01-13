from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtSerialPort
from home import *

MOMENTARY_SWITCH_ON_TIME_MS = 500

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

ALL_BUTTONS_UNPRESSED = '0'

serial_connected = False


if __name__ == "__main__":
    import sys

    # Press Alt+F4 to close the window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)
    MainWindow.showFullScreen()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    @QtCore.pyqtSlot()
    def serial_receive():
        while serial.canReadLine():
            data = serial.readLine()
            formatted_data = QtCore.QTextCodec.codecForMib(106).toUnicode(data)
            formatted_data = formatted_data.rstrip('\r\n')
            ui.receivedData.setText(formatted_data)

    @QtCore.pyqtSlot()
    def serial_send(data_to_send):
        formatted_data = data_to_send.encode()
        serial.write(formatted_data)
        serial.flush()

    serial = QtSerialPort.QSerialPort()
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
                    ui.proteck_logo.setStyleSheet("background-color: red")

    unpressedTimer = QTimer()

    # set up push button functions---------------------------------------
    @QtCore.pyqtSlot()
    def unpressed_function():
        serial_send(ALL_BUTTONS_UNPRESSED)

    @QtCore.pyqtSlot()
    def cycle_start_function():
        serial_send(CYCLE_START_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def cycle_stop_function():
        serial_send(CYCLE_STOP_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def drv_function():
        serial_send(DRV_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def z_lock_function():
        serial_send(Z_LOCK_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def dry_run_function():
        serial_send(DRY_RUN_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def jog_function():
        serial_send(JOG_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def mdi_function():
        serial_send(MDI_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def auto_function():
        serial_send(AUTO_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def x_jog_function():
        serial_send(X_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def y_jog_function():
        serial_send(Y_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def z_jog_function():
        serial_send(Z_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def plus_jog_function():
        serial_send(PLUS_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def minus_jog_function():
        serial_send(MINUS_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def vvv_jog_function():
        serial_send(VVV_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def nc_ref_function():
        serial_send(NC_REF_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def nc_offset_function():
        serial_send(NC_OFFSET_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def ret_for_function():
        serial_send(RET_FOR_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def ret_rev_function():
        serial_send(RET_REV_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def prc_end_function():
        serial_send(PRC_END_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def alm_ovr_function():
        serial_send(ALM_OVR_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def alm_rst_function():
        serial_send(ALM_RST_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def lock_rst_function():
        serial_send(LOCK_RST_PRESSED)
        unpressedTimer.singleShot(MOMENTARY_SWITCH_ON_TIME_MS, lambda: unpressed_function())

    @QtCore.pyqtSlot()
    def laser_on_function():
        if ui.laserOnButton.isChecked():
            serial_send(LASER_ON_PRESSED)
        else:
            unpressed_function()

    ui.cycleStartButton.clicked.connect(lambda: cycle_start_function())
    ui.cycleStopButton.clicked.connect(lambda: cycle_stop_function())
    ui.drvButton.clicked.connect(lambda: drv_function())
    ui.zLockButton.clicked.connect(lambda: z_lock_function())
    ui.dryRunButton.clicked.connect(lambda: dry_run_function())
    ui.jogButton.clicked.connect(lambda: jog_function())
    ui.mdiButton.clicked.connect(lambda: mdi_function())
    ui.autoButton.clicked.connect(lambda: auto_function())
    ui.xButton.clicked.connect(lambda: x_jog_function())
    ui.yButton.clicked.connect(lambda: y_jog_function())
    ui.zButton.clicked.connect(lambda: z_jog_function())
    ui.plusButton.clicked.connect(lambda: plus_jog_function())
    ui.vvvButton.clicked.connect(lambda: vvv_jog_function())
    ui.minusButton.clicked.connect(lambda: minus_jog_function())
    ui.ncRefButton.clicked.connect(lambda: nc_ref_function())
    ui.ncOffsetButton.clicked.connect(lambda: nc_offset_function())
    ui.retForButton.clicked.connect(lambda: ret_for_function())
    ui.retRevButton.clicked.connect(lambda: ret_rev_function())
    ui.prcEndButton.clicked.connect(lambda: prc_end_function())
    ui.almOvrButton.clicked.connect(lambda: alm_ovr_function())
    ui.almRstButton.clicked.connect(lambda: alm_rst_function())
    ui.lockRstButton.clicked.connect(lambda: lock_rst_function())
    ui.laserOnButton.clicked.connect(lambda: laser_on_function())

    MainWindow.show()
    sys.exit(app.exec_())
