from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoTrackingDetails")


@_attrs_define
class VideoTrackingDetails:
    """
    Attributes:
        sport_name (Union[Unset, str]):
        league_name (Union[Unset, str]):
        coverage_type (Union[Unset, str]):
        tracking_name (Union[Unset, str]):
        tracking_id (Union[Unset, str]):
    """

    sport_name: Union[Unset, str] = UNSET
    league_name: Union[Unset, str] = UNSET
    coverage_type: Union[Unset, str] = UNSET
    tracking_name: Union[Unset, str] = UNSET
    tracking_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sport_name = self.sport_name

        league_name = self.league_name

        coverage_type = self.coverage_type

        tracking_name = self.tracking_name

        tracking_id = self.tracking_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sport_name is not UNSET:
            field_dict["sportName"] = sport_name
        if league_name is not UNSET:
            field_dict["leagueName"] = league_name
        if coverage_type is not UNSET:
            field_dict["coverageType"] = coverage_type
        if tracking_name is not UNSET:
            field_dict["trackingName"] = tracking_name
        if tracking_id is not UNSET:
            field_dict["trackingId"] = tracking_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sport_name = d.pop("sportName", UNSET)

        league_name = d.pop("leagueName", UNSET)

        coverage_type = d.pop("coverageType", UNSET)

        tracking_name = d.pop("trackingName", UNSET)

        tracking_id = d.pop("trackingId", UNSET)

        video_tracking_details = cls(
            sport_name=sport_name,
            league_name=league_name,
            coverage_type=coverage_type,
            tracking_name=tracking_name,
            tracking_id=tracking_id,
        )

        video_tracking_details.additional_properties = d
        return video_tracking_details

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
