import obd
import config


class ecuThread():

    rpm = 0
    speed = 0
    coolant_temp = 0

    def new_rpm(self, response):
        self.rpm = int(response.value.magnitude)

    def new_speed(self, response):
        self.speed = int(response.value.magnitude)

    def new_coolant_temp(self, response):
        self.coolant_temp = int(response.value.magnitude)

    def __init__(self):
        # Display all the port available
        self.ports = obd.scan_serial()
        print("Porte disponibili: ")
        print(self.ports)

        # Set debug level, so we can see everything
        obd.logger.setLevel(obd.logging.DEBUG)

        # Connection to ECU
        print("Connecting...")
        self.connection = obd.Async("/dev/rfcomm1", 115200, "3", fast=False)

        print(self.connection.status())

        if (self.connection.is_connected == True):
            print("Connected")

            # Watch everything we care about.
            self.connection.watch(obd.commands.RPM, callback=self.new_rpm)
            self.connection.watch(obd.commands.SPEED, callback=self.new_speed)
            self.connection.watch(obd.commands.COOLANT_TEMP,
                                  callback=self.new_coolant_temp)

            config.ecuReady = True
        else:
            print("Not connected")

    def closeConnection(self):
        print("Closing connection...")
        self.connection.stop()
        self.connection.close()
