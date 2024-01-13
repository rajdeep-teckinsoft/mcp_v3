from time import sleep

from PyQt5.QtCore import Qt
from PyQt5 import QtSerialPort

from home import *

MOMENTARY_SWITCH_ON_TIME_SEC = 0.5

# 1st column of keys
CYCLE_START_ACTIVE = 'D1'
CYCLE_START_INACTIVE = 'D2'

# 2nd column of keys
CYCLE_STOP_ACTIVE = 'D3'
CYCLE_STOP_INACTIVE = 'D4'

# 3rd column of keys
DRV_ACTIVE = 'D5'
DRV_INACTIVE = 'D6'
JOG_ACTIVE = 'D7'
JOG_INACTIVE = 'D8'
X_ACTIVE = 'D9'
X_INACTIVE = 'D10'
PLUS_ACTIVE = 'D11'
PLUS_INACTIVE = 'D12'

# 4th column of keys
Z_LOCK_ACTIVE = 'D13'
Z_LOCK_INACTIVE = 'D14'
MDI_ACTIVE = 'D15'
MDI_INACTIVE = 'D16'
Y_ACTIVE = 'D17'
Y_INACTIVE = 'D18'
VVV_ACTIVE = 'D19'
VVV_INACTIVE = 'D20'

# 5th column of keys
DRY_RUN_ACTIVE = 'D21'
DRY_RUN_INACTIVE = 'D22'
AUTO_ACTIVE = 'D23'
AUTO_INACTIVE = 'D24'
Z_ACTIVE = 'D25'
Z_INACTIVE = 'D26'
MINUS_ACTIVE = 'D27'
MINUS_INACTIVE = 'D28'

# 6th column of keys
NC_REF_ACTIVE = 'D29'
NC_REF_INACTIVE = 'D30'
NC_OFF_ACTIVE = 'D31'
NC_OFF_INACTIVE = 'D32'
RET_FOR_ACTIVE = 'D33'
RET_FOR_INACTIVE = 'D34'
RET_REV_ACTIVE = 'D35'
RET_REV_INACTIVE = 'D36'

# 7th column of keys
PRC_END_ACTIVE = 'D37'
PRC_END_INACTIVE = 'D38'
ALM_OVR_ACTIVE = 'D39'
ALM_OVR_INACTIVE = 'D40'
ALM_RST_ACTIVE = 'D41'
ALM_RST_INACTIVE = 'D42'
LOCK_RST_ACTIVE = 'D43'
LOCK_RST_INACTIVE = 'D44'

# 8th column of keys
LASER_ON_ACTIVE = 'D45'
LASER_ON_INACTIVE = 'D46'

LASER_STATUS_CHECK = 'S1'

serial_connected = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)
    MainWindow.showFullScreen()
    # Press Alt+F4 to close the window
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    @QtCore.pyqtSlot()
    def serial_receive():
        while serial.canReadLine():
            data = serial.readLine()
            formatted_data = QtCore.QTextCodec.codecForMib(106).toUnicode(data)
            formatted_data = formatted_data.rstrip('\r\n')
            # data = data.rstrip('\r\n')
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

    # set up UI logics--------------------------------------------------
    @QtCore.pyqtSlot()
    def auto_ui_logic():
        ui.jogButton.setChecked(False)
        ui.mdiButton.setChecked(False)
        jog_ui_logic()
        x_jog_ui_logic()
        y_jog_ui_logic()
        z_jog_ui_logic()


    @QtCore.pyqtSlot()
    def mdi_ui_logic():
        ui.jogButton.setChecked(False)
        ui.autoButton.setChecked(False)
        jog_ui_logic()
        x_jog_ui_logic()
        y_jog_ui_logic()
        z_jog_ui_logic()


    @QtCore.pyqtSlot()
    def jog_ui_logic():
        if ui.jogButton.isChecked():
            ui.xButton.setEnabled(True)
            ui.yButton.setEnabled(True)
            ui.zButton.setEnabled(True)
            ui.mdiButton.setChecked(False)
            ui.autoButton.setChecked(False)
        else:
            ui.xButton.setChecked(False)
            ui.yButton.setChecked(False)
            ui.zButton.setChecked(False)
            ui.xButton.setEnabled(False)
            ui.yButton.setEnabled(False)
            ui.zButton.setEnabled(False)
            ui.plusButton.setEnabled(False)
            ui.vvvButton.setChecked(False)
            ui.vvvButton.setEnabled(False)
            ui.minusButton.setEnabled(False)


    @QtCore.pyqtSlot()
    def x_jog_ui_logic():
        if ui.xButton.isChecked():
            ui.plusButton.setEnabled(True)
            ui.vvvButton.setEnabled(True)
            ui.minusButton.setEnabled(True)
            ui.yButton.setChecked(False)
            ui.zButton.setChecked(False)
        else:
            ui.plusButton.setEnabled(False)
            ui.vvvButton.setChecked(False)
            ui.vvvButton.setEnabled(False)
            ui.minusButton.setEnabled(False)


    @QtCore.pyqtSlot()
    def y_jog_ui_logic():
        if ui.yButton.isChecked():
            ui.plusButton.setEnabled(True)
            ui.vvvButton.setEnabled(True)
            ui.minusButton.setEnabled(True)
            ui.xButton.setChecked(False)
            ui.zButton.setChecked(False)
        else:
            ui.plusButton.setEnabled(False)
            ui.vvvButton.setChecked(False)
            ui.vvvButton.setEnabled(False)
            ui.minusButton.setEnabled(False)


    @QtCore.pyqtSlot()
    def z_jog_ui_logic():
        if ui.zButton.isChecked():
            ui.plusButton.setEnabled(True)
            ui.vvvButton.setEnabled(True)
            ui.minusButton.setEnabled(True)
            ui.yButton.setChecked(False)
            ui.xButton.setChecked(False)
        else:
            ui.plusButton.setEnabled(False)
            ui.vvvButton.setChecked(False)
            ui.vvvButton.setEnabled(False)
            ui.minusButton.setEnabled(False)


    jog_ui_logic()
    x_jog_ui_logic()
    y_jog_ui_logic()
    z_jog_ui_logic()
    ui.jogButton.clicked.connect(lambda: jog_ui_logic())
    ui.xButton.clicked.connect(lambda: x_jog_ui_logic())
    ui.yButton.clicked.connect(lambda: y_jog_ui_logic())
    ui.zButton.clicked.connect(lambda: z_jog_ui_logic())
    ui.mdiButton.clicked.connect(lambda: mdi_ui_logic())
    ui.autoButton.clicked.connect(lambda: auto_ui_logic())

    # set up push button functions---------------------------------------
    """"
    serial_connected = communication.connect_ethercat0()
    if serial_connected:
        print("Serial is connected")
    else:
        serial_connected = communication.connect_ethercat1()
        if serial_connected:
            print("Serial is connected")
        else:
            serial_connected = communication.connect_ethercat2()
            if serial_connected:
                print("Serial is connected")
            else:
                serial_connected = communication.connect_ethercat3()
                if serial_connected:
                    print("Serial is connected")
                else:
                    ui.proteck_logo.setStyleSheet("background-color: red")
                    print("Serial is not connected. Please check!")
    """


    @QtCore.pyqtSlot()
    def cycle_start_function():
        serial_send(CYCLE_START_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(CYCLE_START_INACTIVE)


    @QtCore.pyqtSlot()
    def cycle_stop_function():
        serial_send(CYCLE_STOP_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(CYCLE_STOP_INACTIVE)


    @QtCore.pyqtSlot()
    def drv_function():
        if ui.drvButton.isChecked():
            serial_send(DRV_ACTIVE)
        else:
            serial_send(DRV_INACTIVE)


    @QtCore.pyqtSlot()
    def z_lock_function():
        if ui.zLockButton.isChecked():
            serial_send(Z_LOCK_ACTIVE)
        else:
            serial_send(Z_LOCK_INACTIVE)


    @QtCore.pyqtSlot()
    def dry_run_function():
        if ui.dryRunButton.isChecked():
            serial_send(DRY_RUN_ACTIVE)
        else:
            serial_send(DRY_RUN_INACTIVE)


    @QtCore.pyqtSlot()
    def jog_function():
        if ui.jogButton.isChecked():
            serial_send(JOG_ACTIVE)
        else:
            serial_send(JOG_INACTIVE)


    @QtCore.pyqtSlot()
    def mdi_function():
        if ui.mdiButton.isChecked():
            serial_send(MDI_ACTIVE)
        else:
            serial_send(MDI_INACTIVE)


    @QtCore.pyqtSlot()
    def auto_function():
        if ui.autoButton.isChecked():
            serial_send(AUTO_ACTIVE)
        else:
            serial_send(AUTO_INACTIVE)


    @QtCore.pyqtSlot()
    def x_jog_function():
        if ui.xButton.isChecked():
            serial_send(X_ACTIVE)
        else:
            serial_send(X_INACTIVE)


    @QtCore.pyqtSlot()
    def y_jog_function():
        if ui.yButton.isChecked():
            serial_send(Y_ACTIVE)
        else:
            serial_send(Y_INACTIVE)


    @QtCore.pyqtSlot()
    def z_jog_function():
        if ui.zButton.isChecked():
            serial_send(Z_ACTIVE)
        else:
            serial_send(Z_INACTIVE)


    @QtCore.pyqtSlot()
    def plus_jog_function():
        serial_send(PLUS_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(PLUS_INACTIVE)


    @QtCore.pyqtSlot()
    def minus_jog_function():
        serial_send(MINUS_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(MINUS_INACTIVE)


    @QtCore.pyqtSlot()
    def vvv_jog_function():
        if ui.vvvButton.isChecked():
            serial_send(VVV_ACTIVE)
        else:
            serial_send(VVV_INACTIVE)


    @QtCore.pyqtSlot()
    def nc_ref_function():
        if ui.ncRefButton.isChecked():
            serial_send(NC_REF_ACTIVE)
        else:
            serial_send(NC_REF_INACTIVE)


    @QtCore.pyqtSlot()
    def nc_offset_function():
        if ui.ncOffsetButton.isChecked():
            serial_send(NC_OFF_ACTIVE)
        else:
            serial_send(NC_OFF_INACTIVE)


    @QtCore.pyqtSlot()
    def ret_for_function():
        serial_send(RET_FOR_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(RET_FOR_INACTIVE)


    @QtCore.pyqtSlot()
    def ret_rev_function():
        serial_send(RET_REV_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(RET_REV_INACTIVE)


    @QtCore.pyqtSlot()
    def prc_end_function():
        serial_send(PRC_END_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(PRC_END_INACTIVE)


    @QtCore.pyqtSlot()
    def alm_ovr_function():
        serial_send(ALM_OVR_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(ALM_OVR_INACTIVE)


    @QtCore.pyqtSlot()
    def alm_rst_function():
        serial_send(ALM_RST_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(ALM_RST_INACTIVE)


    @QtCore.pyqtSlot()
    def lock_rst_function():
        serial_send(LOCK_RST_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        serial_send(LOCK_RST_INACTIVE)


    """
    def laser_status_check():
        serial_send(LASER_STATUS_CHECK)
        received = communication.read_data()
        if received:
            ui.laserReadyLamp.setPixmap(QtGui.QPixmap("images/laserready_on.png"))
        else:
            ui.laserReadyLamp.setPixmap(QtGui.QPixmap("images/laserready_off.png"))


    laserTimer = QTimer()
    laserTimer.timeout.connect(lambda: laser_status_check())
    """


    @QtCore.pyqtSlot()
    def laser_on_function():
        if ui.laserOnButton.isChecked():
            serial_send(LASER_ON_ACTIVE)
            sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
            serial_send(LASER_STATUS_CHECK)
        else:
            serial_send(LASER_ON_INACTIVE)


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
