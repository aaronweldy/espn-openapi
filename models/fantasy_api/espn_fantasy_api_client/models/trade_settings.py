import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TradeSettings")


@_attrs_define
class TradeSettings:
    """
    Attributes:
        deadline_date (datetime.datetime): Trade deadline Example: 2023-11-10T17:00:00Z.
        veto_period (Union[Unset, int]): Days to vote on trade veto Example: 1.
        veto_votes_required (Union[Unset, int]): Votes needed to veto a trade Example: 4.
    """

    deadline_date: datetime.datetime
    veto_period: Union[Unset, int] = UNSET
    veto_votes_required: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deadline_date = self.deadline_date.isoformat()

        veto_period = self.veto_period

        veto_votes_required = self.veto_votes_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deadlineDate": deadline_date,
            }
        )
        if veto_period is not UNSET:
            field_dict["vetoPeriod"] = veto_period
        if veto_votes_required is not UNSET:
            field_dict["vetoVotesRequired"] = veto_votes_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deadline_date = isoparse(d.pop("deadlineDate"))

        veto_period = d.pop("vetoPeriod", UNSET)

        veto_votes_required = d.pop("vetoVotesRequired", UNSET)

        trade_settings = cls(
            deadline_date=deadline_date,
            veto_period=veto_period,
            veto_votes_required=veto_votes_required,
        )

        trade_settings.additional_properties = d
        return trade_settings

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
