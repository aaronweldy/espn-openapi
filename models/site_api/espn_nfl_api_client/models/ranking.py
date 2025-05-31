from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dropped_out_team import DroppedOutTeam
    from ..models.others_receiving_votes import OthersReceivingVotes
    from ..models.ranking_entry import RankingEntry
    from ..models.ranking_occurrence import RankingOccurrence


T = TypeVar("T", bound="Ranking")


@_attrs_define
class Ranking:
    """Individual ranking system (AP, Coaches, etc.)

    Attributes:
        name (Union[Unset, str]): Full name of the ranking (e.g., "AP Top 25")
        short_name (Union[Unset, str]): Short name of the ranking (e.g., "AP Poll")
        record_type (Union[None, Unset, str]): Type of record used for ranking
        current (Union[None, Unset, bool]): Whether this is the current ranking
        ranks (Union[Unset, List['RankingEntry']]): List of ranked teams
        dropped_out (Union[Unset, List['DroppedOutTeam']]): Teams that dropped out of the rankings
        others (Union[Unset, List['OthersReceivingVotes']]): Teams receiving votes but not in top 25
        occurrence (Union[Unset, RankingOccurrence]): When this ranking occurred
    """

    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    record_type: Union[None, Unset, str] = UNSET
    current: Union[None, Unset, bool] = UNSET
    ranks: Union[Unset, List["RankingEntry"]] = UNSET
    dropped_out: Union[Unset, List["DroppedOutTeam"]] = UNSET
    others: Union[Unset, List["OthersReceivingVotes"]] = UNSET
    occurrence: Union[Unset, "RankingOccurrence"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        short_name = self.short_name

        record_type: Union[None, Unset, str]
        if isinstance(self.record_type, Unset):
            record_type = UNSET
        else:
            record_type = self.record_type

        current: Union[None, Unset, bool]
        if isinstance(self.current, Unset):
            current = UNSET
        else:
            current = self.current

        ranks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ranks, Unset):
            ranks = []
            for ranks_item_data in self.ranks:
                ranks_item = ranks_item_data.to_dict()
                ranks.append(ranks_item)

        dropped_out: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dropped_out, Unset):
            dropped_out = []
            for dropped_out_item_data in self.dropped_out:
                dropped_out_item = dropped_out_item_data.to_dict()
                dropped_out.append(dropped_out_item)

        others: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.others, Unset):
            others = []
            for others_item_data in self.others:
                others_item = others_item_data.to_dict()
                others.append(others_item)

        occurrence: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if record_type is not UNSET:
            field_dict["recordType"] = record_type
        if current is not UNSET:
            field_dict["current"] = current
        if ranks is not UNSET:
            field_dict["ranks"] = ranks
        if dropped_out is not UNSET:
            field_dict["droppedOut"] = dropped_out
        if others is not UNSET:
            field_dict["others"] = others
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dropped_out_team import DroppedOutTeam
        from ..models.others_receiving_votes import OthersReceivingVotes
        from ..models.ranking_entry import RankingEntry
        from ..models.ranking_occurrence import RankingOccurrence

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        def _parse_record_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        record_type = _parse_record_type(d.pop("recordType", UNSET))

        def _parse_current(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        current = _parse_current(d.pop("current", UNSET))

        ranks = []
        _ranks = d.pop("ranks", UNSET)
        for ranks_item_data in _ranks or []:
            ranks_item = RankingEntry.from_dict(ranks_item_data)

            ranks.append(ranks_item)

        dropped_out = []
        _dropped_out = d.pop("droppedOut", UNSET)
        for dropped_out_item_data in _dropped_out or []:
            dropped_out_item = DroppedOutTeam.from_dict(dropped_out_item_data)

            dropped_out.append(dropped_out_item)

        others = []
        _others = d.pop("others", UNSET)
        for others_item_data in _others or []:
            others_item = OthersReceivingVotes.from_dict(others_item_data)

            others.append(others_item)

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: Union[Unset, RankingOccurrence]
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = RankingOccurrence.from_dict(_occurrence)

        ranking = cls(
            name=name,
            short_name=short_name,
            record_type=record_type,
            current=current,
            ranks=ranks,
            dropped_out=dropped_out,
            others=others,
            occurrence=occurrence,
        )

        ranking.additional_properties = d
        return ranking

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
