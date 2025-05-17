from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_draft_pick_status import NflDraftPickStatus
    from ..models.reference import Reference


T = TypeVar("T", bound="NflDraftPick")


@_attrs_define
class NflDraftPick:
    """
    Attributes:
        status (NflDraftPickStatus):
        pick (int):
        overall (int):
        round_ (int):
        traded (bool):
        athlete (Reference):
        team (Reference):
        trade_note (Union[None, Unset, str]):
    """

    status: "NflDraftPickStatus"
    pick: int
    overall: int
    round_: int
    traded: bool
    athlete: "Reference"
    team: "Reference"
    trade_note: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.to_dict()

        pick = self.pick

        overall = self.overall

        round_ = self.round_

        traded = self.traded

        athlete = self.athlete.to_dict()

        team = self.team.to_dict()

        trade_note: Union[None, Unset, str]
        if isinstance(self.trade_note, Unset):
            trade_note = UNSET
        else:
            trade_note = self.trade_note

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "pick": pick,
                "overall": overall,
                "round": round_,
                "traded": traded,
                "athlete": athlete,
                "team": team,
            }
        )
        if trade_note is not UNSET:
            field_dict["tradeNote"] = trade_note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_draft_pick_status import NflDraftPickStatus
        from ..models.reference import Reference

        d = src_dict.copy()
        status = NflDraftPickStatus.from_dict(d.pop("status"))

        pick = d.pop("pick")

        overall = d.pop("overall")

        round_ = d.pop("round")

        traded = d.pop("traded")

        athlete = Reference.from_dict(d.pop("athlete"))

        team = Reference.from_dict(d.pop("team"))

        def _parse_trade_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        trade_note = _parse_trade_note(d.pop("tradeNote", UNSET))

        nfl_draft_pick = cls(
            status=status,
            pick=pick,
            overall=overall,
            round_=round_,
            traded=traded,
            athlete=athlete,
            team=team,
            trade_note=trade_note,
        )

        nfl_draft_pick.additional_properties = d
        return nfl_draft_pick

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
