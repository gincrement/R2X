"""R2X pint units."""

from infrasys.base_quantity import ureg, BaseQuantity
from pint import Quantity

# ruff: noqa
# type: ignore

ureg.define("MMBtu = [energy] = 293071 * [watt_hour]")
ureg.define("MMBTu = [energy] = 293071 * [watt_hour]")
ureg.define("usd = []")


class Distance(BaseQuantity):
    __base_unit__ = "meter"


class Voltage(BaseQuantity):
    __base_unit__ = "kilovolt"


class Current(BaseQuantity):
    __base_unit__ = "ampere"


class Angle(BaseQuantity):
    __base_unit__ = "degree"


class ActivePower(BaseQuantity):
    __base_unit__ = "megawatt"


class ApparentPower(BaseQuantity):
    __base_unit__ = "volt_ampere"


class Time(BaseQuantity):
    __base_unit__ = "minute"


class Resistance(BaseQuantity):
    __base_unit__ = "ohm"


class HeatRate(BaseQuantity):
    __base_unit__ = "Btu/kWh"


class FuelPrice(BaseQuantity):
    __base_unit__ = "usd/Btu"


class VOMPrice(BaseQuantity):
    __base_unit__ = "usd/kWh"


class Energy(BaseQuantity):
    __base_unit__ = "watthour"


class Percentage(BaseQuantity):
    __base_unit__ = "percent"


class EmissionRate(BaseQuantity):
    __base_unit__ = "kg/MWh"


class PowerRate(BaseQuantity):
    __base_unit__ = "MW/min"


class Currency(BaseQuantity):
    __base_unit__ = "usd"


def get_magnitude(field) -> float | int:
    """Get reference base power of the component."""
    return field.magnitude if isinstance(field, Quantity) else field
