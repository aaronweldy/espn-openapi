from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.odds_record_stat import OddsRecordStat


T = TypeVar("T", bound="TeamOddsRecord")


@_attrs_define
class TeamOddsRecord:
    """
    Attributes:
        abbreviation (str): Abbreviation for the odds record type Example: ML.
        display_name (str): Display name for the odds record type Example: Money Line Overall Record.
        short_display_name (str): Short display name for the odds record type Example: Money Line.
        type (str): The type of odds record Example: moneyLineOverall.
        stats (List['OddsRecordStat']):
    """

    abbreviation: str
    display_name: str
    short_display_name: str
    type: str
    stats: List["OddsRecordStat"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        abbreviation = self.abbreviation

        display_name = self.display_name

        short_display_name = self.short_display_name

        type = self.type

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()
            stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "abbreviation": abbreviation,
                "displayName": display_name,
                "shortDisplayName": short_display_name,
                "type": type,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.odds_record_stat import OddsRecordStat

        d = src_dict.copy()
        abbreviation = d.pop("abbreviation")

        display_name = d.pop("displayName")

        short_display_name = d.pop("shortDisplayName")

        type = d.pop("type")

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = OddsRecordStat.from_dict(stats_item_data)

            stats.append(stats_item)

        team_odds_record = cls(
            abbreviation=abbreviation,
            display_name=display_name,
            short_display_name=short_display_name,
            type=type,
            stats=stats,
        )

        team_odds_record.additional_properties = d
        return team_odds_record

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
