from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mlb_position_name import MLBPositionName
from ..models.nba_position_name import NBAPositionName
from ..models.nfl_position_name import NFLPositionName
from ..models.nhl_position_name import NHLPositionName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roster_athlete import RosterAthlete


T = TypeVar("T", bound="Position")


@_attrs_define
class Position:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[MLBPositionName, NBAPositionName, NFLPositionName, NHLPositionName, Unset]):
        display_name (Union[Unset, str]): Display name of the position
        abbreviation (Union[Unset, str]): Position abbreviation
        items (Union[Unset, List['RosterAthlete']]): List of athletes in this position category
    """

    id: Union[Unset, str] = UNSET
    name: Union[MLBPositionName, NBAPositionName, NFLPositionName, NHLPositionName, Unset] = UNSET
    display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    items: Union[Unset, List["RosterAthlete"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name: Union[Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, NFLPositionName):
            name = self.name.value
        elif isinstance(self.name, NBAPositionName):
            name = self.name.value
        elif isinstance(self.name, MLBPositionName):
            name = self.name.value
        else:
            name = self.name.value

        display_name = self.display_name

        abbreviation = self.abbreviation

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.roster_athlete import RosterAthlete

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        def _parse_name(
            data: object,
        ) -> Union[MLBPositionName, NBAPositionName, NFLPositionName, NHLPositionName, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_0 = NFLPositionName(data)

                return name_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_1 = NBAPositionName(data)

                return name_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_2 = MLBPositionName(data)

                return name_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            name_type_3 = NHLPositionName(data)

            return name_type_3

        name = _parse_name(d.pop("name", UNSET))

        display_name = d.pop("displayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = RosterAthlete.from_dict(items_item_data)

            items.append(items_item)

        position = cls(
            id=id,
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            items=items,
        )

        position.additional_properties = d
        return position

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
