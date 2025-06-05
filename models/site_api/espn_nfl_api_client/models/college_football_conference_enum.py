from enum import Enum


class CollegeFootballConferenceEnum(str, Enum):
    VALUE_0 = "1"
    VALUE_1 = "4"
    VALUE_10 = "151"
    VALUE_11 = "21"
    VALUE_12 = "24"
    VALUE_13 = "25"
    VALUE_14 = "26"
    VALUE_15 = "27"
    VALUE_16 = "29"
    VALUE_17 = "30"
    VALUE_18 = "31"
    VALUE_19 = "40"
    VALUE_2 = "5"
    VALUE_20 = "48"
    VALUE_21 = "49"
    VALUE_22 = "50"
    VALUE_23 = "80"
    VALUE_24 = "81"
    VALUE_25 = "90"
    VALUE_3 = "8"
    VALUE_4 = "9"
    VALUE_5 = "12"
    VALUE_6 = "15"
    VALUE_7 = "17"
    VALUE_8 = "18"
    VALUE_9 = "37"

    def __str__(self) -> str:
        return str(self.value)
