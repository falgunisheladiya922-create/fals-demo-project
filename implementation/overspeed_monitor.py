"""
@file overspeed_monitor.py
@brief Overspeed warning system
"""

def check_speed(speed):
    """
    Check speed threshold

    @param speed Vehicle speed

    @return Warning status
    """

    if speed > 120:
        return "WARNING"

    return "OK"
