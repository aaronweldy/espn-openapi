from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qbr_splits import QBRSplits
    from ..models.reference import Reference


T = TypeVar("T", bound="QBRItem")


@_attrs_define
class QBRItem:
    """
    Attributes:
        athlete (Reference):
        splits (QBRSplits):
        event (Union[Unset, Reference]):
        season (Union[Unset, Reference]):
        team (Union[Unset, Reference]):
    """

    athlete: "Reference"
    splits: "QBRSplits"
    event: Union[Unset, "Reference"] = UNSET
    season: Union[Unset, "Reference"] = UNSET
    team: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athlete = self.athlete.to_dict()

        splits = self.splits.to_dict()

        event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "athlete": athlete,
                "splits": splits,
            }
        )
        if event is not UNSET:
            field_dict["event"] = event
        if season is not UNSET:
            field_dict["season"] = season
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.qbr_splits import QBRSplits
        from ..models.reference import Reference

        d = src_dict.copy()
        athlete = Reference.from_dict(d.pop("athlete"))

        splits = QBRSplits.from_dict(d.pop("splits"))

        _event = d.pop("event", UNSET)
        event: Union[Unset, Reference]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = Reference.from_dict(_event)

        _season = d.pop("season", UNSET)
        season: Union[Unset, Reference]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = Reference.from_dict(_season)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Reference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Reference.from_dict(_team)

        qbr_item = cls(
            athlete=athlete,
            splits=splits,
            event=event,
            season=season,
            team=team,
        )

        qbr_item.additional_properties = d
        return qbr_item

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
