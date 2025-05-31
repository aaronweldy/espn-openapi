from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Season")


@_attrs_define
class Season:
    """
    Attributes:
        year (int):  Example: 2023.
        type (int): Season type (1=preseason, 2=regular, 3=postseason) Example: 3.
        slug (Union[Unset, str]):  Example: post-season.
        name (Union[Unset, str]): Season name (e.g., "Regular Season", "Postseason") Example: Postseason.
        display_name (Union[Unset, str]): Display name of the season (e.g., "2024-25") Example: 2024-25.
        half (Union[Unset, int]): Season half (1 or 2, primarily for basketball)
    """

    year: int
    type: int
    slug: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    half: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        type = self.type

        slug = self.slug

        name = self.name

        display_name = self.display_name

        half = self.half

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "type": type,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if half is not UNSET:
            field_dict["half"] = half

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year")

        type = d.pop("type")

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        half = d.pop("half", UNSET)

        season = cls(
            year=year,
            type=type,
            slug=slug,
            name=name,
            display_name=display_name,
            half=half,
        )

        season.additional_properties = d
        return season

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
