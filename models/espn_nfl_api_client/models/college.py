from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logo import Logo


T = TypeVar("T", bound="College")


@_attrs_define
class College:
    """Information about athlete's college

    Attributes:
        id (Union[Unset, str]): College ID
        mascot (Union[Unset, str]): College team mascot
        name (Union[Unset, str]): College name
        short_name (Union[Unset, str]): Short name of the college
        abbrev (Union[Unset, str]): Abbreviation of the college
        logos (Union[Unset, List['Logo']]): College logos
    """

    id: Union[Unset, str] = UNSET
    mascot: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    abbrev: Union[Unset, str] = UNSET
    logos: Union[Unset, List["Logo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        mascot = self.mascot

        name = self.name

        short_name = self.short_name

        abbrev = self.abbrev

        logos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mascot is not UNSET:
            field_dict["mascot"] = mascot
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if abbrev is not UNSET:
            field_dict["abbrev"] = abbrev
        if logos is not UNSET:
            field_dict["logos"] = logos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.logo import Logo

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        mascot = d.pop("mascot", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        abbrev = d.pop("abbrev", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = Logo.from_dict(logos_item_data)

            logos.append(logos_item)

        college = cls(
            id=id,
            mascot=mascot,
            name=name,
            short_name=short_name,
            abbrev=abbrev,
            logos=logos,
        )

        college.additional_properties = d
        return college

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
