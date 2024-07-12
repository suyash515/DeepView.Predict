from .device import _Device

def list_all_devices():
    device_instance = _Device()
    devices = device_instance.get_all_devices()
    for device_name, properties in devices.items():
        print(f"Device: {device_name}")
        for prop, value in properties.__dict__.items():
            print(f"  {prop}: {value}")
        print("")

if __name__ == "__main__":
    list_all_devices()