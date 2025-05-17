from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nfl_athlete_injury_athlete_type_1 import NflAthleteInjuryAthleteType1
    from ..models.nfl_athlete_injury_source import NflAthleteInjurySource
    from ..models.nfl_athlete_injury_team_type_1 import NflAthleteInjuryTeamType1
    from ..models.nfl_athlete_injury_type import NflAthleteInjuryType
    from ..models.reference import Reference


T = TypeVar("T", bound="NflAthleteInjury")


@_attrs_define
class NflAthleteInjury:
    """Detailed NFL athlete injury object

    Attributes:
        ref (str):
        id (str):
        long_comment (str):
        short_comment (str):
        status (str):
        date (str):
        athlete (Union['NflAthleteInjuryAthleteType1', 'Reference']):
        team (Union['NflAthleteInjuryTeamType1', 'Reference']):
        source (NflAthleteInjurySource):
        type (NflAthleteInjuryType):
    """

    ref: str
    id: str
    long_comment: str
    short_comment: str
    status: str
    date: str
    athlete: Union["NflAthleteInjuryAthleteType1", "Reference"]
    team: Union["NflAthleteInjuryTeamType1", "Reference"]
    source: "NflAthleteInjurySource"
    type: "NflAthleteInjuryType"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference

        ref = self.ref

        id = self.id

        long_comment = self.long_comment

        short_comment = self.short_comment

        status = self.status

        date = self.date

        athlete: Dict[str, Any]
        if isinstance(self.athlete, Reference):
            athlete = self.athlete.to_dict()
        else:
            athlete = self.athlete.to_dict()

        team: Dict[str, Any]
        if isinstance(self.team, Reference):
            team = self.team.to_dict()
        else:
            team = self.team.to_dict()

        source = self.source.to_dict()

        type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "longComment": long_comment,
                "shortComment": short_comment,
                "status": status,
                "date": date,
                "athlete": athlete,
                "team": team,
                "source": source,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_athlete_injury_athlete_type_1 import NflAthleteInjuryAthleteType1
        from ..models.nfl_athlete_injury_source import NflAthleteInjurySource
        from ..models.nfl_athlete_injury_team_type_1 import NflAthleteInjuryTeamType1
        from ..models.nfl_athlete_injury_type import NflAthleteInjuryType
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        long_comment = d.pop("longComment")

        short_comment = d.pop("shortComment")

        status = d.pop("status")

        date = d.pop("date")

        def _parse_athlete(data: object) -> Union["NflAthleteInjuryAthleteType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                athlete_type_0 = Reference.from_dict(data)

                return athlete_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            athlete_type_1 = NflAthleteInjuryAthleteType1.from_dict(data)

            return athlete_type_1

        athlete = _parse_athlete(d.pop("athlete"))

        def _parse_team(data: object) -> Union["NflAthleteInjuryTeamType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = Reference.from_dict(data)

                return team_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            team_type_1 = NflAthleteInjuryTeamType1.from_dict(data)

            return team_type_1

        team = _parse_team(d.pop("team"))

        source = NflAthleteInjurySource.from_dict(d.pop("source"))

        type = NflAthleteInjuryType.from_dict(d.pop("type"))

        nfl_athlete_injury = cls(
            ref=ref,
            id=id,
            long_comment=long_comment,
            short_comment=short_comment,
            status=status,
            date=date,
            athlete=athlete,
            team=team,
            source=source,
            type=type,
        )

        nfl_athlete_injury.additional_properties = d
        return nfl_athlete_injury

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
