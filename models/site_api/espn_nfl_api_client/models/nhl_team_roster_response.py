from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nhl_athlete import NhlAthlete
    from ..models.nhl_coach import NhlCoach
    from ..models.team_detail import TeamDetail


T = TypeVar("T", bound="NhlTeamRosterResponse")


@_attrs_define
class NhlTeamRosterResponse:
    """NHL team roster response with player and coach information

    Attributes:
        team (TeamDetail):
        athletes (List['NhlAthlete']):
        coaches (Union[Unset, List['NhlCoach']]):
    """

    team: "TeamDetail"
    athletes: List["NhlAthlete"]
    coaches: Union[Unset, List["NhlCoach"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team = self.team.to_dict()

        athletes = []
        for athletes_item_data in self.athletes:
            athletes_item = athletes_item_data.to_dict()
            athletes.append(athletes_item)

        coaches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coaches, Unset):
            coaches = []
            for coaches_item_data in self.coaches:
                coaches_item = coaches_item_data.to_dict()
                coaches.append(coaches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "athletes": athletes,
            }
        )
        if coaches is not UNSET:
            field_dict["coaches"] = coaches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nhl_athlete import NhlAthlete
        from ..models.nhl_coach import NhlCoach
        from ..models.team_detail import TeamDetail

        d = src_dict.copy()
        team = TeamDetail.from_dict(d.pop("team"))

        athletes = []
        _athletes = d.pop("athletes")
        for athletes_item_data in _athletes:
            athletes_item = NhlAthlete.from_dict(athletes_item_data)

            athletes.append(athletes_item)

        coaches = []
        _coaches = d.pop("coaches", UNSET)
        for coaches_item_data in _coaches or []:
            coaches_item = NhlCoach.from_dict(coaches_item_data)

            coaches.append(coaches_item)

        nhl_team_roster_response = cls(
            team=team,
            athletes=athletes,
            coaches=coaches,
        )

        nhl_team_roster_response.additional_properties = d
        return nhl_team_roster_response

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
