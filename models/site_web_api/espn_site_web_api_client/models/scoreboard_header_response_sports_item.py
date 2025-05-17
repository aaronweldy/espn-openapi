from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_header_response_sports_item_leagues_item import (
        ScoreboardHeaderResponseSportsItemLeaguesItem,
    )


T = TypeVar("T", bound="ScoreboardHeaderResponseSportsItem")


@_attrs_define
class ScoreboardHeaderResponseSportsItem:
    """
    Attributes:
        id (Union[Unset, str]):
        uid (Union[Unset, str]):
        name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        short_name (Union[Unset, str]):
        slug (Union[Unset, str]):
        tag (Union[Unset, str]):
        is_tournament (Union[Unset, bool]):
        leagues (Union[Unset, List['ScoreboardHeaderResponseSportsItemLeaguesItem']]):
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    is_tournament: Union[Unset, bool] = UNSET
    leagues: Union[Unset, List["ScoreboardHeaderResponseSportsItemLeaguesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        name = self.name

        abbreviation = self.abbreviation

        short_name = self.short_name

        slug = self.slug

        tag = self.tag

        is_tournament = self.is_tournament

        leagues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leagues, Unset):
            leagues = []
            for leagues_item_data in self.leagues:
                leagues_item = leagues_item_data.to_dict()
                leagues.append(leagues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if tag is not UNSET:
            field_dict["tag"] = tag
        if is_tournament is not UNSET:
            field_dict["isTournament"] = is_tournament
        if leagues is not UNSET:
            field_dict["leagues"] = leagues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_header_response_sports_item_leagues_item import (
            ScoreboardHeaderResponseSportsItemLeaguesItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        name = d.pop("name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_name = d.pop("shortName", UNSET)

        slug = d.pop("slug", UNSET)

        tag = d.pop("tag", UNSET)

        is_tournament = d.pop("isTournament", UNSET)

        leagues = []
        _leagues = d.pop("leagues", UNSET)
        for leagues_item_data in _leagues or []:
            leagues_item = ScoreboardHeaderResponseSportsItemLeaguesItem.from_dict(leagues_item_data)

            leagues.append(leagues_item)

        scoreboard_header_response_sports_item = cls(
            id=id,
            uid=uid,
            name=name,
            abbreviation=abbreviation,
            short_name=short_name,
            slug=slug,
            tag=tag,
            is_tournament=is_tournament,
            leagues=leagues,
        )

        scoreboard_header_response_sports_item.additional_properties = d
        return scoreboard_header_response_sports_item

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
