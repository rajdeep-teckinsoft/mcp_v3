from PyQt5 import QtSerialPort
from PyQt5.QtCore import Qt, QTimer

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

if __name__ == "__main__":
    import sys

    # Press Alt+F4 to close the window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)
    MainWindow.showFullScreen()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    icon_cycle_start_on = QtGui.QPixmap("images/on/cyclestart.png")
    icon_cycle_stop_on = QtGui.QPixmap("images/on/cyclestop.png")
    icon_drv_on = QtGui.QPixmap("images/on/drv.png")
    icon_jog_on = QtGui.QPixmap("images/on/jog.png")
    icon_x_on = QtGui.QPixmap("images/on/x.png")
    icon_plus_on = QtGui.QPixmap("images/on/plus.png")
    icon_zlock_on = QtGui.QPixmap("images/on/zlock.png")
    icon_mdi_on = QtGui.QPixmap("images/on/mdi.png")
    icon_y_on = QtGui.QPixmap("images/on/y.png")
    icon_vvv_on = QtGui.QPixmap("images/on/vvv.png")
    icon_dry_run_on = QtGui.QPixmap("images/on/dryrun.png")
    icon_auto_on = QtGui.QPixmap("images/on/auto.png")
    icon_z_on = QtGui.QPixmap("images/on/z.png")
    icon_minus_on = QtGui.QPixmap("images/on/minus.png")
    icon_nc_ref_on = QtGui.QPixmap("images/on/ncref.png")
    icon_nc_offset_on = QtGui.QPixmap("images/on/ncoffset.png")
    icon_ret_for_on = QtGui.QPixmap("images/on/retfor.png")
    icon_ret_rev_on = QtGui.QPixmap("images/on/retrev.png")
    icon_prc_end_on = QtGui.QPixmap("images/on/prcend.png")
    icon_alm_ovr_on = QtGui.QPixmap("images/on/almovr.png")
    icon_alm_rst_on = QtGui.QPixmap("images/on/almrst.png")
    icon_lock_rst_on = QtGui.QPixmap("images/on/lockrst.png")
    icon_laser_ready_on = QtGui.QPixmap("images/laserready_on.png")
    icon_usb_connect_on = QtGui.QPixmap("images/on/usb_connection.png")

    icon_cycle_start_off = QtGui.QPixmap("images/off/cyclestart.png")
    icon_cycle_stop_off = QtGui.QPixmap("images/off/cyclestop.png")
    icon_drv_off = QtGui.QPixmap("images/off/drv.png")
    icon_jog_off = QtGui.QPixmap("images/off/jog.png")
    icon_x_off = QtGui.QPixmap("images/off/x.png")
    icon_plus_off = QtGui.QPixmap("images/off/plus.png")
    icon_zlock_off = QtGui.QPixmap("images/off/zlock.png")
    icon_mdi_off = QtGui.QPixmap("images/off/mdi.png")
    icon_y_off = QtGui.QPixmap("images/off/y.png")
    icon_vvv_off = QtGui.QPixmap("images/off/vvv.png")
    icon_dry_run_off = QtGui.QPixmap("images/off/dryrun.png")
    icon_auto_off = QtGui.QPixmap("images/off/auto.png")
    icon_z_off = QtGui.QPixmap("images/off/z.png")
    icon_minus_off = QtGui.QPixmap("images/off/minus.png")
    icon_nc_ref_off = QtGui.QPixmap("images/off/ncref.png")
    icon_nc_offset_off = QtGui.QPixmap("images/off/ncoffset.png")
    icon_ret_for_off = QtGui.QPixmap("images/off/retfor.png")
    icon_ret_rev_off = QtGui.QPixmap("images/off/retrev.png")
    icon_prc_end_off = QtGui.QPixmap("images/off/prcend.png")
    icon_alm_ovr_off = QtGui.QPixmap("images/off/almovr.png")
    icon_alm_rst_off = QtGui.QPixmap("images/off/almrst.png")
    icon_lock_rst_off = QtGui.QPixmap("images/off/lockrst.png")
    icon_laser_ready_off = QtGui.QPixmap("images/laserready_off.png")
    icon_usb_connect_off = QtGui.QPixmap("images/off/usb_connection.png")


    @QtCore.pyqtSlot()
    def serial_receive():
        while serial.canReadLine():
            data = serial.readLine()
            formatted_data = QtCore.QTextCodec.codecForMib(106).toUnicode(data)
            formatted_data = formatted_data.rstrip('\r\n')
            array_data = list(formatted_data)

            if array_data[0] == '1':
                ui.cycleStartButton.setIcon(QtGui.QIcon(icon_cycle_start_on))
            else:
                ui.cycleStartButton.setIcon(QtGui.QIcon(icon_cycle_start_off))

            if array_data[1] == '1':
                ui.cycleStopButton.setIcon(QtGui.QIcon(icon_cycle_stop_on))
            else:
                ui.cycleStopButton.setIcon(QtGui.QIcon(icon_cycle_stop_off))

            if array_data[2] == '1':
                ui.drvButton.setIcon(QtGui.QIcon(icon_drv_on))
            else:
                ui.drvButton.setIcon(QtGui.QIcon(icon_drv_off))

            if array_data[3] == '1':
                ui.jogButton.setIcon(QtGui.QIcon(icon_jog_on))
            else:
                ui.jogButton.setIcon(QtGui.QIcon(icon_jog_off))

            if array_data[4] == '1':
                ui.xButton.setIcon(QtGui.QIcon(icon_x_on))
            else:
                ui.xButton.setIcon(QtGui.QIcon(icon_x_off))

            if array_data[5] == '1':
                ui.plusButton.setIcon(QtGui.QIcon(icon_plus_on))
            else:
                ui.plusButton.setIcon(QtGui.QIcon(icon_plus_off))

            if array_data[6] == '1':
                ui.zLockButton.setIcon(QtGui.QIcon(icon_zlock_on))
            else:
                ui.zLockButton.setIcon(QtGui.QIcon(icon_zlock_off))

            if array_data[7] == '1':
                ui.mdiButton.setIcon(QtGui.QIcon(icon_mdi_on))
            else:
                ui.mdiButton.setIcon(QtGui.QIcon(icon_mdi_off))

            if array_data[8] == '1':
                ui.yButton.setIcon(QtGui.QIcon(icon_y_on))
            else:
                ui.yButton.setIcon(QtGui.QIcon(icon_y_off))

            if array_data[9] == '1':
                ui.vvvButton.setIcon(QtGui.QIcon(icon_vvv_on))
            else:
                ui.vvvButton.setIcon(QtGui.QIcon(icon_vvv_off))

            if array_data[10] == '1':
                ui.dryRunButton.setIcon(QtGui.QIcon(icon_dry_run_on))
            else:
                ui.dryRunButton.setIcon(QtGui.QIcon(icon_dry_run_off))

            if array_data[11] == '1':
                ui.autoButton.setIcon(QtGui.QIcon(icon_auto_on))
            else:
                ui.autoButton.setIcon(QtGui.QIcon(icon_auto_off))

            if array_data[12] == '1':
                ui.zButton.setIcon(QtGui.QIcon(icon_z_on))
            else:
                ui.zButton.setIcon(QtGui.QIcon(icon_z_off))

            if array_data[13] == '1':
                ui.minusButton.setIcon(QtGui.QIcon(icon_minus_on))
            else:
                ui.minusButton.setIcon(QtGui.QIcon(icon_minus_off))

            if array_data[14] == '1':
                ui.ncRefButton.setIcon(QtGui.QIcon(icon_nc_ref_on))
            else:
                ui.ncRefButton.setIcon(QtGui.QIcon(icon_nc_ref_off))

            if array_data[15] == '1':
                ui.ncOffsetButton.setIcon(QtGui.QIcon(icon_nc_offset_on))
            else:
                ui.ncOffsetButton.setIcon(QtGui.QIcon(icon_nc_offset_off))

            if array_data[16] == '1':
                ui.retForButton.setIcon(QtGui.QIcon(icon_ret_for_on))
            else:
                ui.retForButton.setIcon(QtGui.QIcon(icon_ret_for_off))

            if array_data[17] == '1':
                ui.retRevButton.setIcon(QtGui.QIcon(icon_ret_rev_on))
            else:
                ui.retRevButton.setIcon(QtGui.QIcon(icon_ret_rev_off))

            if array_data[18] == '1':
                ui.prcEndButton.setIcon(QtGui.QIcon(icon_prc_end_on))
            else:
                ui.prcEndButton.setIcon(QtGui.QIcon(icon_prc_end_off))

            if array_data[19] == '1':
                ui.almOvrButton.setIcon(QtGui.QIcon(icon_alm_ovr_on))
            else:
                ui.almOvrButton.setIcon(QtGui.QIcon(icon_alm_ovr_off))

            if array_data[20] == '1':
                ui.almRstButton.setIcon(QtGui.QIcon(icon_alm_rst_on))
            else:
                ui.almRstButton.setIcon(QtGui.QIcon(icon_alm_rst_off))

            if array_data[21] == '1':
                ui.lockRstButton.setIcon(QtGui.QIcon(icon_lock_rst_on))
            else:
                ui.lockRstButton.setIcon(QtGui.QIcon(icon_lock_rst_off))

            # if array_data[22] == '1':
            #     ui.cycleStartButton.setIcon(QtGui.QIcon(icon_cycle_start_on))
            # else:
            #     ui.cycleStartButton.setIcon(QtGui.QIcon(icon_cycle_start_off))

            if array_data[23] == '1':
                ui.laserReadyLamp.setPixmap(icon_laser_ready_on)
            else:
                ui.laserReadyLamp.setPixmap(icon_laser_ready_off)


    @QtCore.pyqtSlot()
    def serial_send(data_to_send):
        formatted_data = data_to_send.encode()
        serial.write(formatted_data)
        serial.flush()

    serial = QtSerialPort.QSerialPort()

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
                        ui.usbConnectButton.setIcon(QtGui.QIcon(icon_usb_connect_off))
                    else:
                        ui.usbConnectButton.setIcon(QtGui.QIcon(icon_usb_connect_on))
                else:
                    ui.usbConnectButton.setIcon(QtGui.QIcon(icon_usb_connect_on))
            else:
                ui.usbConnectButton.setIcon(QtGui.QIcon(icon_usb_connect_on))
        else:
            ui.usbConnectButton.setIcon(QtGui.QIcon(icon_usb_connect_on))

    usb_connect_function()

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
    ui.usbConnectButton.clicked.connect(lambda: usb_connect_function())

    MainWindow.show()
    sys.exit(app.exec_())
