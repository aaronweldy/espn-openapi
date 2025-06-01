from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsCategory")


@_attrs_define
class NewsCategory:
    """
    Attributes:
        id (Union[Unset, int]):
        uid (Union[Unset, str]):
        type (Union[Unset, str]):
        description (Union[Unset, str]):
        sport_id (Union[Unset, int]):
        league_id (Union[Unset, int]):
        team_id (Union[Unset, int]):
        athlete_id (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    uid: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    sport_id: Union[Unset, int] = UNSET
    league_id: Union[Unset, int] = UNSET
    team_id: Union[Unset, int] = UNSET
    athlete_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        type = self.type

        description = self.description

        sport_id = self.sport_id

        league_id = self.league_id

        team_id = self.team_id

        athlete_id = self.athlete_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if sport_id is not UNSET:
            field_dict["sportId"] = sport_id
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if athlete_id is not UNSET:
            field_dict["athleteId"] = athlete_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        type = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        sport_id = d.pop("sportId", UNSET)

        league_id = d.pop("leagueId", UNSET)

        team_id = d.pop("teamId", UNSET)

        athlete_id = d.pop("athleteId", UNSET)

        news_category = cls(
            id=id,
            uid=uid,
            type=type,
            description=description,
            sport_id=sport_id,
            league_id=league_id,
            team_id=team_id,
            athlete_id=athlete_id,
        )

        news_category.additional_properties = d
        return news_category

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
