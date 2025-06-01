from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_against_the_spread_current_line import FantasyAgainstTheSpreadCurrentLine
    from ..models.fantasy_against_the_spread_team import FantasyAgainstTheSpreadTeam


T = TypeVar("T", bound="FantasyAgainstTheSpread")


@_attrs_define
class FantasyAgainstTheSpread:
    """
    Attributes:
        team (Union[Unset, FantasyAgainstTheSpreadTeam]):
        current_line (Union[Unset, FantasyAgainstTheSpreadCurrentLine]):
    """

    team: Union[Unset, "FantasyAgainstTheSpreadTeam"] = UNSET
    current_line: Union[Unset, "FantasyAgainstTheSpreadCurrentLine"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        current_line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_line, Unset):
            current_line = self.current_line.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team
        if current_line is not UNSET:
            field_dict["currentLine"] = current_line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_against_the_spread_current_line import FantasyAgainstTheSpreadCurrentLine
        from ..models.fantasy_against_the_spread_team import FantasyAgainstTheSpreadTeam

        d = src_dict.copy()
        _team = d.pop("team", UNSET)
        team: Union[Unset, FantasyAgainstTheSpreadTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = FantasyAgainstTheSpreadTeam.from_dict(_team)

        _current_line = d.pop("currentLine", UNSET)
        current_line: Union[Unset, FantasyAgainstTheSpreadCurrentLine]
        if isinstance(_current_line, Unset):
            current_line = UNSET
        else:
            current_line = FantasyAgainstTheSpreadCurrentLine.from_dict(_current_line)

        fantasy_against_the_spread = cls(
            team=team,
            current_line=current_line,
        )

        fantasy_against_the_spread.additional_properties = d
        return fantasy_against_the_spread

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
