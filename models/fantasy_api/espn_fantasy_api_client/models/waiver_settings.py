from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WaiverSettings")


@_attrs_define
class WaiverSettings:
    """
    Attributes:
        process_day (int): Day of week waivers process (1 = Mon, 3 = Wed) Example: 3.
        acquisition_type (int): Acquisition type (1 = waivers, 2 = free agency) Example: 1.
        process_hour (Union[Unset, int]): Hour of day waivers process Example: 8.
        acquisition_limit (Union[Unset, int]): Max acquisitions per season (-1 = unlimited) Example: -1.
    """

    process_day: int
    acquisition_type: int
    process_hour: Union[Unset, int] = UNSET
    acquisition_limit: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        process_day = self.process_day

        acquisition_type = self.acquisition_type

        process_hour = self.process_hour

        acquisition_limit = self.acquisition_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processDay": process_day,
                "acquisitionType": acquisition_type,
            }
        )
        if process_hour is not UNSET:
            field_dict["processHour"] = process_hour
        if acquisition_limit is not UNSET:
            field_dict["acquisitionLimit"] = acquisition_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        process_day = d.pop("processDay")

        acquisition_type = d.pop("acquisitionType")

        process_hour = d.pop("processHour", UNSET)

        acquisition_limit = d.pop("acquisitionLimit", UNSET)

        waiver_settings = cls(
            process_day=process_day,
            acquisition_type=acquisition_type,
            process_hour=process_hour,
            acquisition_limit=acquisition_limit,
        )

        waiver_settings.additional_properties = d
        return waiver_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
