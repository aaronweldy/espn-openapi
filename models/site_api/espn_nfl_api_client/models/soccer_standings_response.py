from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_reference import SeasonReference
    from ..models.soccer_standings_group import SoccerStandingsGroup


T = TypeVar("T", bound="SoccerStandingsResponse")


@_attrs_define
class SoccerStandingsResponse:
    """Soccer league standings response

    Attributes:
        id (str): League ID Example: 23.
        name (str): League name Example: English Premier League.
        abbreviation (str): League abbreviation Example: ENG.
        children (List['SoccerStandingsGroup']): Array of standings groups (e.g., overall standings, group standings)
        uid (Union[Unset, str]): Unique identifier for the standings Example: s:600~l:23.
        seasons (Union[Unset, List['SeasonReference']]): Available seasons
    """

    id: str
    name: str
    abbreviation: str
    children: List["SoccerStandingsGroup"]
    uid: Union[Unset, str] = UNSET
    seasons: Union[Unset, List["SeasonReference"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        uid = self.uid

        seasons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.seasons, Unset):
            seasons = []
            for seasons_item_data in self.seasons:
                seasons_item = seasons_item_data.to_dict()
                seasons.append(seasons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "abbreviation": abbreviation,
                "children": children,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if seasons is not UNSET:
            field_dict["seasons"] = seasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_reference import SeasonReference
        from ..models.soccer_standings_group import SoccerStandingsGroup

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = SoccerStandingsGroup.from_dict(children_item_data)

            children.append(children_item)

        uid = d.pop("uid", UNSET)

        seasons = []
        _seasons = d.pop("seasons", UNSET)
        for seasons_item_data in _seasons or []:
            seasons_item = SeasonReference.from_dict(seasons_item_data)

            seasons.append(seasons_item)

        soccer_standings_response = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            children=children,
            uid=uid,
            seasons=seasons,
        )

        soccer_standings_response.additional_properties = d
        return soccer_standings_response

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
