from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_reference import TeamReference


T = TypeVar("T", bound="Draft")


@_attrs_define
class Draft:
    """
    Attributes:
        display_text (Union[Unset, str]):
        round_ (Union[Unset, int]):
        year (Union[Unset, int]):
        selection (Union[Unset, int]):
        team (Union[Unset, TeamReference]):
    """

    display_text: Union[Unset, str] = UNSET
    round_: Union[Unset, int] = UNSET
    year: Union[Unset, int] = UNSET
    selection: Union[Unset, int] = UNSET
    team: Union[Unset, "TeamReference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_text = self.display_text

        round_ = self.round_

        year = self.year

        selection = self.selection

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_text is not UNSET:
            field_dict["displayText"] = display_text
        if round_ is not UNSET:
            field_dict["round"] = round_
        if year is not UNSET:
            field_dict["year"] = year
        if selection is not UNSET:
            field_dict["selection"] = selection
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_reference import TeamReference

        d = src_dict.copy()
        display_text = d.pop("displayText", UNSET)

        round_ = d.pop("round", UNSET)

        year = d.pop("year", UNSET)

        selection = d.pop("selection", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, TeamReference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = TeamReference.from_dict(_team)

        draft = cls(
            display_text=display_text,
            round_=round_,
            year=year,
            selection=selection,
            team=team,
        )

        draft.additional_properties = d
        return draft

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
