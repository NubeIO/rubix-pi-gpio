import io
import os
from rubix_http.resource import RubixResource


def is_raspberrypi():
    if os.name != 'posix':
        return False
    chips = ('BCM2708', 'BCM2709', 'BCM2711', 'BCM2835', 'BCM2836')
    try:
        with io.open('/proc/cpuinfo', 'r') as cpuinfo:
            for line in cpuinfo:
                if line.startswith('Hardware'):
                    _, value = line.strip().split(':', 1)
                    value = value.strip()
                    if value in chips:
                        return True
    except Exception:
        pass
    return False


class STM(RubixResource):
    @classmethod
    def get(cls):
        return {
            'version': is_raspberrypi()
        }


if is_raspberrypi():
    print(11111)
    import RPi.GPIO as GPIO
