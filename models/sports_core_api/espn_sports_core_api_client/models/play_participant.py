from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.play_participant_athlete_type_1 import PlayParticipantAthleteType1
    from ..models.play_participant_position_type_1 import PlayParticipantPositionType1
    from ..models.play_participant_statistics_type_1 import PlayParticipantStatisticsType1
    from ..models.play_stat import PlayStat
    from ..models.reference import Reference


T = TypeVar("T", bound="PlayParticipant")


@_attrs_define
class PlayParticipant:
    """
    Attributes:
        athlete (Union['PlayParticipantAthleteType1', 'Reference', Unset]):
        position (Union['PlayParticipantPositionType1', 'Reference', Unset]):
        statistics (Union['PlayParticipantStatisticsType1', 'Reference', Unset]):
        stats (Union[Unset, List['PlayStat']]):
        order (Union[Unset, int]):
        type (Union[Unset, str]):
    """

    athlete: Union["PlayParticipantAthleteType1", "Reference", Unset] = UNSET
    position: Union["PlayParticipantPositionType1", "Reference", Unset] = UNSET
    statistics: Union["PlayParticipantStatisticsType1", "Reference", Unset] = UNSET
    stats: Union[Unset, List["PlayStat"]] = UNSET
    order: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference

        athlete: Union[Dict[str, Any], Unset]
        if isinstance(self.athlete, Unset):
            athlete = UNSET
        elif isinstance(self.athlete, Reference):
            athlete = self.athlete.to_dict()
        else:
            athlete = self.athlete.to_dict()

        position: Union[Dict[str, Any], Unset]
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, Reference):
            position = self.position.to_dict()
        else:
            position = self.position.to_dict()

        statistics: Union[Dict[str, Any], Unset]
        if isinstance(self.statistics, Unset):
            statistics = UNSET
        elif isinstance(self.statistics, Reference):
            statistics = self.statistics.to_dict()
        else:
            statistics = self.statistics.to_dict()

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        order = self.order

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if position is not UNSET:
            field_dict["position"] = position
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if stats is not UNSET:
            field_dict["stats"] = stats
        if order is not UNSET:
            field_dict["order"] = order
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.play_participant_athlete_type_1 import PlayParticipantAthleteType1
        from ..models.play_participant_position_type_1 import PlayParticipantPositionType1
        from ..models.play_participant_statistics_type_1 import PlayParticipantStatisticsType1
        from ..models.play_stat import PlayStat
        from ..models.reference import Reference

        d = src_dict.copy()

        def _parse_athlete(data: object) -> Union["PlayParticipantAthleteType1", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                athlete_type_0 = Reference.from_dict(data)

                return athlete_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            athlete_type_1 = PlayParticipantAthleteType1.from_dict(data)

            return athlete_type_1

        athlete = _parse_athlete(d.pop("athlete", UNSET))

        def _parse_position(data: object) -> Union["PlayParticipantPositionType1", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                position_type_0 = Reference.from_dict(data)

                return position_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            position_type_1 = PlayParticipantPositionType1.from_dict(data)

            return position_type_1

        position = _parse_position(d.pop("position", UNSET))

        def _parse_statistics(data: object) -> Union["PlayParticipantStatisticsType1", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                statistics_type_0 = Reference.from_dict(data)

                return statistics_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            statistics_type_1 = PlayParticipantStatisticsType1.from_dict(data)

            return statistics_type_1

        statistics = _parse_statistics(d.pop("statistics", UNSET))

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = PlayStat.from_dict(stats_item_data)

            stats.append(stats_item)

        order = d.pop("order", UNSET)

        type = d.pop("type", UNSET)

        play_participant = cls(
            athlete=athlete,
            position=position,
            statistics=statistics,
            stats=stats,
            order=order,
            type=type,
        )

        play_participant.additional_properties = d
        return play_participant

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
