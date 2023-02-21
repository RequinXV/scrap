class Bass:

    def __init__(self, manufacturer, model, serial_type, category, price):
        self.set_manufacturer(manufacturer)
        self.set_model(model)
        self.set_serial_type(serial_type)

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_model(self, model):
        self.model = model

    def set_serial_type(self, serial_type):
        self.serial_type = serial_type
