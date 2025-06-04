from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_response_settings import GroupResponseSettings


T = TypeVar("T", bound="GroupResponse")


@_attrs_define
class GroupResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        challenge_id (Union[Unset, str]):
        size (Union[Unset, int]):
        settings (Union[Unset, GroupResponseSettings]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    challenge_id: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    settings: Union[Unset, "GroupResponseSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        challenge_id = self.challenge_id

        size = self.size

        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id
        if size is not UNSET:
            field_dict["size"] = size
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_response_settings import GroupResponseSettings

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        challenge_id = d.pop("challengeId", UNSET)

        size = d.pop("size", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, GroupResponseSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = GroupResponseSettings.from_dict(_settings)

        group_response = cls(
            id=id,
            name=name,
            challenge_id=challenge_id,
            size=size,
            settings=settings,
        )

        group_response.additional_properties = d
        return group_response

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
