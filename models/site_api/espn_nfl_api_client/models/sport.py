from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sport_league import SportLeague


T = TypeVar("T", bound="Sport")


@_attrs_define
class Sport:
    """
    Attributes:
        id (str):  Example: 20.
        name (str):  Example: Football.
        leagues (List['SportLeague']):
        uid (Union[Unset, str]):  Example: s:20.
        slug (Union[Unset, str]):  Example: football.
    """

    id: str
    name: str
    leagues: List["SportLeague"]
    uid: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        leagues = []
        for leagues_item_data in self.leagues:
            leagues_item = leagues_item_data.to_dict()
            leagues.append(leagues_item)

        uid = self.uid

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "leagues": leagues,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sport_league import SportLeague

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        leagues = []
        _leagues = d.pop("leagues")
        for leagues_item_data in _leagues:
            leagues_item = SportLeague.from_dict(leagues_item_data)

            leagues.append(leagues_item)

        uid = d.pop("uid", UNSET)

        slug = d.pop("slug", UNSET)

        sport = cls(
            id=id,
            name=name,
            leagues=leagues,
            uid=uid,
            slug=slug,
        )

        sport.additional_properties = d
        return sport

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
