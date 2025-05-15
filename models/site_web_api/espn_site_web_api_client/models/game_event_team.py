from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="GameEventTeam")


@_attrs_define
class GameEventTeam:
    """
    Attributes:
        id (str):  Example: 24.
        abbreviation (str):  Example: LAC.
        uid (Union[Unset, str]):  Example: s:20~l:28~t:24.
        display_name (Union[Unset, str]):  Example: Los Angeles Chargers.
        links (Union[Unset, List['Link']]):
        logo (Union[Unset, str]):  Example: https://a.espncdn.com/i/teamlogos/nfl/500/lac.png.
        is_all_star (Union[Unset, bool]):
    """

    id: str
    abbreviation: str
    uid: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    logo: Union[Unset, str] = UNSET
    is_all_star: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        abbreviation = self.abbreviation

        uid = self.uid

        display_name = self.display_name

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        logo = self.logo

        is_all_star = self.is_all_star

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "abbreviation": abbreviation,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if links is not UNSET:
            field_dict["links"] = links
        if logo is not UNSET:
            field_dict["logo"] = logo
        if is_all_star is not UNSET:
            field_dict["isAllStar"] = is_all_star

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id")

        abbreviation = d.pop("abbreviation")

        uid = d.pop("uid", UNSET)

        display_name = d.pop("displayName", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        logo = d.pop("logo", UNSET)

        is_all_star = d.pop("isAllStar", UNSET)

        game_event_team = cls(
            id=id,
            abbreviation=abbreviation,
            uid=uid,
            display_name=display_name,
            links=links,
            logo=logo,
            is_all_star=is_all_star,
        )

        game_event_team.additional_properties = d
        return game_event_team

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
