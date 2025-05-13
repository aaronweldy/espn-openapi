from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.draft_settings import DraftSettings
    from ..models.roster_settings import RosterSettings
    from ..models.schedule_settings import ScheduleSettings
    from ..models.scoring_settings import ScoringSettings
    from ..models.trade_settings import TradeSettings
    from ..models.waiver_settings import WaiverSettings


T = TypeVar("T", bound="LeagueSettings")


@_attrs_define
class LeagueSettings:
    """
    Attributes:
        name (str):  Example: Example League.
        size (int): Number of teams Example: 10.
        draft_settings (Union[Unset, DraftSettings]):
        roster_settings (Union[Unset, RosterSettings]):
        schedule_settings (Union[Unset, ScheduleSettings]):
        scoring_settings (Union[Unset, ScoringSettings]):
        trade_settings (Union[Unset, TradeSettings]):
        waiver_settings (Union[Unset, WaiverSettings]):
    """

    name: str
    size: int
    draft_settings: Union[Unset, "DraftSettings"] = UNSET
    roster_settings: Union[Unset, "RosterSettings"] = UNSET
    schedule_settings: Union[Unset, "ScheduleSettings"] = UNSET
    scoring_settings: Union[Unset, "ScoringSettings"] = UNSET
    trade_settings: Union[Unset, "TradeSettings"] = UNSET
    waiver_settings: Union[Unset, "WaiverSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        size = self.size

        draft_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft_settings, Unset):
            draft_settings = self.draft_settings.to_dict()

        roster_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.roster_settings, Unset):
            roster_settings = self.roster_settings.to_dict()

        schedule_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule_settings, Unset):
            schedule_settings = self.schedule_settings.to_dict()

        scoring_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scoring_settings, Unset):
            scoring_settings = self.scoring_settings.to_dict()

        trade_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trade_settings, Unset):
            trade_settings = self.trade_settings.to_dict()

        waiver_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.waiver_settings, Unset):
            waiver_settings = self.waiver_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "size": size,
            }
        )
        if draft_settings is not UNSET:
            field_dict["draftSettings"] = draft_settings
        if roster_settings is not UNSET:
            field_dict["rosterSettings"] = roster_settings
        if schedule_settings is not UNSET:
            field_dict["scheduleSettings"] = schedule_settings
        if scoring_settings is not UNSET:
            field_dict["scoringSettings"] = scoring_settings
        if trade_settings is not UNSET:
            field_dict["tradeSettings"] = trade_settings
        if waiver_settings is not UNSET:
            field_dict["waiverSettings"] = waiver_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.draft_settings import DraftSettings
        from ..models.roster_settings import RosterSettings
        from ..models.schedule_settings import ScheduleSettings
        from ..models.scoring_settings import ScoringSettings
        from ..models.trade_settings import TradeSettings
        from ..models.waiver_settings import WaiverSettings

        d = src_dict.copy()
        name = d.pop("name")

        size = d.pop("size")

        _draft_settings = d.pop("draftSettings", UNSET)
        draft_settings: Union[Unset, DraftSettings]
        if isinstance(_draft_settings, Unset):
            draft_settings = UNSET
        else:
            draft_settings = DraftSettings.from_dict(_draft_settings)

        _roster_settings = d.pop("rosterSettings", UNSET)
        roster_settings: Union[Unset, RosterSettings]
        if isinstance(_roster_settings, Unset):
            roster_settings = UNSET
        else:
            roster_settings = RosterSettings.from_dict(_roster_settings)

        _schedule_settings = d.pop("scheduleSettings", UNSET)
        schedule_settings: Union[Unset, ScheduleSettings]
        if isinstance(_schedule_settings, Unset):
            schedule_settings = UNSET
        else:
            schedule_settings = ScheduleSettings.from_dict(_schedule_settings)

        _scoring_settings = d.pop("scoringSettings", UNSET)
        scoring_settings: Union[Unset, ScoringSettings]
        if isinstance(_scoring_settings, Unset):
            scoring_settings = UNSET
        else:
            scoring_settings = ScoringSettings.from_dict(_scoring_settings)

        _trade_settings = d.pop("tradeSettings", UNSET)
        trade_settings: Union[Unset, TradeSettings]
        if isinstance(_trade_settings, Unset):
            trade_settings = UNSET
        else:
            trade_settings = TradeSettings.from_dict(_trade_settings)

        _waiver_settings = d.pop("waiverSettings", UNSET)
        waiver_settings: Union[Unset, WaiverSettings]
        if isinstance(_waiver_settings, Unset):
            waiver_settings = UNSET
        else:
            waiver_settings = WaiverSettings.from_dict(_waiver_settings)

        league_settings = cls(
            name=name,
            size=size,
            draft_settings=draft_settings,
            roster_settings=roster_settings,
            schedule_settings=schedule_settings,
            scoring_settings=scoring_settings,
            trade_settings=trade_settings,
            waiver_settings=waiver_settings,
        )

        league_settings.additional_properties = d
        return league_settings

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
