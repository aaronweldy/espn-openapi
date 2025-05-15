from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drive_field_position import DriveFieldPosition
    from ..models.drive_source import DriveSource
    from ..models.drive_time_elapsed import DriveTimeElapsed
    from ..models.plays_list_response import PlaysListResponse
    from ..models.reference import Reference
    from ..models.team import Team


T = TypeVar("T", bound="Drive")


@_attrs_define
class Drive:
    """
    Attributes:
        ref (Union[Unset, str]):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        sequence_number (Union[Unset, str]):
        team (Union['Reference', 'Team', Unset]):
        end_team (Union['Reference', 'Team', Unset]):
        start (Union[Unset, DriveFieldPosition]):
        end (Union[Unset, DriveFieldPosition]):
        time_elapsed (Union[Unset, DriveTimeElapsed]):
        yards (Union[Unset, int]):
        is_score (Union[Unset, bool]):
        offensive_plays (Union[Unset, int]):
        result (Union[Unset, str]):
        short_display_result (Union[Unset, str]):
        display_result (Union[Unset, str]):
        source (Union[Unset, DriveSource]):
        plays (Union[Unset, PlaysListResponse]):
    """

    ref: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    sequence_number: Union[Unset, str] = UNSET
    team: Union["Reference", "Team", Unset] = UNSET
    end_team: Union["Reference", "Team", Unset] = UNSET
    start: Union[Unset, "DriveFieldPosition"] = UNSET
    end: Union[Unset, "DriveFieldPosition"] = UNSET
    time_elapsed: Union[Unset, "DriveTimeElapsed"] = UNSET
    yards: Union[Unset, int] = UNSET
    is_score: Union[Unset, bool] = UNSET
    offensive_plays: Union[Unset, int] = UNSET
    result: Union[Unset, str] = UNSET
    short_display_result: Union[Unset, str] = UNSET
    display_result: Union[Unset, str] = UNSET
    source: Union[Unset, "DriveSource"] = UNSET
    plays: Union[Unset, "PlaysListResponse"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference

        ref = self.ref

        id = self.id

        description = self.description

        sequence_number = self.sequence_number

        team: Union[Dict[str, Any], Unset]
        if isinstance(self.team, Unset):
            team = UNSET
        elif isinstance(self.team, Reference):
            team = self.team.to_dict()
        else:
            team = self.team.to_dict()

        end_team: Union[Dict[str, Any], Unset]
        if isinstance(self.end_team, Unset):
            end_team = UNSET
        elif isinstance(self.end_team, Reference):
            end_team = self.end_team.to_dict()
        else:
            end_team = self.end_team.to_dict()

        start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        time_elapsed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_elapsed, Unset):
            time_elapsed = self.time_elapsed.to_dict()

        yards = self.yards

        is_score = self.is_score

        offensive_plays = self.offensive_plays

        result = self.result

        short_display_result = self.short_display_result

        display_result = self.display_result

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        plays: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plays, Unset):
            plays = self.plays.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if sequence_number is not UNSET:
            field_dict["sequenceNumber"] = sequence_number
        if team is not UNSET:
            field_dict["team"] = team
        if end_team is not UNSET:
            field_dict["endTeam"] = end_team
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if time_elapsed is not UNSET:
            field_dict["timeElapsed"] = time_elapsed
        if yards is not UNSET:
            field_dict["yards"] = yards
        if is_score is not UNSET:
            field_dict["isScore"] = is_score
        if offensive_plays is not UNSET:
            field_dict["offensivePlays"] = offensive_plays
        if result is not UNSET:
            field_dict["result"] = result
        if short_display_result is not UNSET:
            field_dict["shortDisplayResult"] = short_display_result
        if display_result is not UNSET:
            field_dict["displayResult"] = display_result
        if source is not UNSET:
            field_dict["source"] = source
        if plays is not UNSET:
            field_dict["plays"] = plays

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.drive_field_position import DriveFieldPosition
        from ..models.drive_source import DriveSource
        from ..models.drive_time_elapsed import DriveTimeElapsed
        from ..models.plays_list_response import PlaysListResponse
        from ..models.reference import Reference
        from ..models.team import Team

        d = src_dict.copy()
        ref = d.pop("$ref", UNSET)

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        sequence_number = d.pop("sequenceNumber", UNSET)

        def _parse_team(data: object) -> Union["Reference", "Team", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = Reference.from_dict(data)

                return team_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            team_type_1 = Team.from_dict(data)

            return team_type_1

        team = _parse_team(d.pop("team", UNSET))

        def _parse_end_team(data: object) -> Union["Reference", "Team", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                end_team_type_0 = Reference.from_dict(data)

                return end_team_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            end_team_type_1 = Team.from_dict(data)

            return end_team_type_1

        end_team = _parse_end_team(d.pop("endTeam", UNSET))

        _start = d.pop("start", UNSET)
        start: Union[Unset, DriveFieldPosition]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = DriveFieldPosition.from_dict(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, DriveFieldPosition]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = DriveFieldPosition.from_dict(_end)

        _time_elapsed = d.pop("timeElapsed", UNSET)
        time_elapsed: Union[Unset, DriveTimeElapsed]
        if isinstance(_time_elapsed, Unset):
            time_elapsed = UNSET
        else:
            time_elapsed = DriveTimeElapsed.from_dict(_time_elapsed)

        yards = d.pop("yards", UNSET)

        is_score = d.pop("isScore", UNSET)

        offensive_plays = d.pop("offensivePlays", UNSET)

        result = d.pop("result", UNSET)

        short_display_result = d.pop("shortDisplayResult", UNSET)

        display_result = d.pop("displayResult", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, DriveSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = DriveSource.from_dict(_source)

        _plays = d.pop("plays", UNSET)
        plays: Union[Unset, PlaysListResponse]
        if isinstance(_plays, Unset):
            plays = UNSET
        else:
            plays = PlaysListResponse.from_dict(_plays)

        drive = cls(
            ref=ref,
            id=id,
            description=description,
            sequence_number=sequence_number,
            team=team,
            end_team=end_team,
            start=start,
            end=end,
            time_elapsed=time_elapsed,
            yards=yards,
            is_score=is_score,
            offensive_plays=offensive_plays,
            result=result,
            short_display_result=short_display_result,
            display_result=display_result,
            source=source,
            plays=plays,
        )

        drive.additional_properties = d
        return drive

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
