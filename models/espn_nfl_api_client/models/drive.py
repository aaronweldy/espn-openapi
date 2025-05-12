from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drive_time_of_possession import DriveTimeOfPossession


T = TypeVar("T", bound="Drive")


@_attrs_define
class Drive:
    """
    Attributes:
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        sequence_number (Union[Unset, str]):
        result (Union[Unset, str]):
        play_count (Union[Unset, int]):
        yards (Union[Unset, int]):
        time_of_possession (Union[Unset, DriveTimeOfPossession]):
    """

    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    sequence_number: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    play_count: Union[Unset, int] = UNSET
    yards: Union[Unset, int] = UNSET
    time_of_possession: Union[Unset, "DriveTimeOfPossession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        sequence_number = self.sequence_number

        result = self.result

        play_count = self.play_count

        yards = self.yards

        time_of_possession: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_of_possession, Unset):
            time_of_possession = self.time_of_possession.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if sequence_number is not UNSET:
            field_dict["sequenceNumber"] = sequence_number
        if result is not UNSET:
            field_dict["result"] = result
        if play_count is not UNSET:
            field_dict["playCount"] = play_count
        if yards is not UNSET:
            field_dict["yards"] = yards
        if time_of_possession is not UNSET:
            field_dict["timeOfPossession"] = time_of_possession

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drive_time_of_possession import DriveTimeOfPossession

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        sequence_number = d.pop("sequenceNumber", UNSET)

        result = d.pop("result", UNSET)

        play_count = d.pop("playCount", UNSET)

        yards = d.pop("yards", UNSET)

        _time_of_possession = d.pop("timeOfPossession", UNSET)
        time_of_possession: Union[Unset, DriveTimeOfPossession]
        if isinstance(_time_of_possession, Unset):
            time_of_possession = UNSET
        else:
            time_of_possession = DriveTimeOfPossession.from_dict(_time_of_possession)

        drive = cls(
            id=id,
            description=description,
            sequence_number=sequence_number,
            result=result,
            play_count=play_count,
            yards=yards,
            time_of_possession=time_of_possession,
        )

        drive.additional_properties = d
        return drive

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
