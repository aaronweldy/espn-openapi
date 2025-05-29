from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.athlete_contract_base_year_compensation import AthleteContractBaseYearCompensation
    from ..models.athlete_contract_poison_pill_provision import AthleteContractPoisonPillProvision
    from ..models.athlete_contract_trade_kicker import AthleteContractTradeKicker
    from ..models.reference import Reference


T = TypeVar("T", bound="AthleteContract")


@_attrs_define
class AthleteContract:
    """
    Attributes:
        ref (str):  Example:
            http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/athletes/1966/contracts/2024?lang=en&region=us.
        bird_status (int):
        base_year_compensation (AthleteContractBaseYearCompensation):
        poison_pill_provision (AthleteContractPoisonPillProvision):
        incoming_trade_value (int):  Example: 47607350.
        outgoing_trade_value (int):  Example: 47607350.
        minimum_salary_exception (bool):
        option_type (int):
        salary (int):  Example: 47607350.
        salary_remaining (int):
        years_remaining (int):  Example: 2.
        season (Reference):
        team (Reference):
        trade_kicker (AthleteContractTradeKicker):
        trade_restriction (bool):  Example: True.
        unsigned_foreign_pick (bool):
        active (bool):  Example: True.
    """

    ref: str
    bird_status: int
    base_year_compensation: "AthleteContractBaseYearCompensation"
    poison_pill_provision: "AthleteContractPoisonPillProvision"
    incoming_trade_value: int
    outgoing_trade_value: int
    minimum_salary_exception: bool
    option_type: int
    salary: int
    salary_remaining: int
    years_remaining: int
    season: "Reference"
    team: "Reference"
    trade_kicker: "AthleteContractTradeKicker"
    trade_restriction: bool
    unsigned_foreign_pick: bool
    active: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        bird_status = self.bird_status

        base_year_compensation = self.base_year_compensation.to_dict()

        poison_pill_provision = self.poison_pill_provision.to_dict()

        incoming_trade_value = self.incoming_trade_value

        outgoing_trade_value = self.outgoing_trade_value

        minimum_salary_exception = self.minimum_salary_exception

        option_type = self.option_type

        salary = self.salary

        salary_remaining = self.salary_remaining

        years_remaining = self.years_remaining

        season = self.season.to_dict()

        team = self.team.to_dict()

        trade_kicker = self.trade_kicker.to_dict()

        trade_restriction = self.trade_restriction

        unsigned_foreign_pick = self.unsigned_foreign_pick

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "birdStatus": bird_status,
                "baseYearCompensation": base_year_compensation,
                "poisonPillProvision": poison_pill_provision,
                "incomingTradeValue": incoming_trade_value,
                "outgoingTradeValue": outgoing_trade_value,
                "minimumSalaryException": minimum_salary_exception,
                "optionType": option_type,
                "salary": salary,
                "salaryRemaining": salary_remaining,
                "yearsRemaining": years_remaining,
                "season": season,
                "team": team,
                "tradeKicker": trade_kicker,
                "tradeRestriction": trade_restriction,
                "unsignedForeignPick": unsigned_foreign_pick,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_contract_base_year_compensation import AthleteContractBaseYearCompensation
        from ..models.athlete_contract_poison_pill_provision import AthleteContractPoisonPillProvision
        from ..models.athlete_contract_trade_kicker import AthleteContractTradeKicker
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref")

        bird_status = d.pop("birdStatus")

        base_year_compensation = AthleteContractBaseYearCompensation.from_dict(d.pop("baseYearCompensation"))

        poison_pill_provision = AthleteContractPoisonPillProvision.from_dict(d.pop("poisonPillProvision"))

        incoming_trade_value = d.pop("incomingTradeValue")

        outgoing_trade_value = d.pop("outgoingTradeValue")

        minimum_salary_exception = d.pop("minimumSalaryException")

        option_type = d.pop("optionType")

        salary = d.pop("salary")

        salary_remaining = d.pop("salaryRemaining")

        years_remaining = d.pop("yearsRemaining")

        season = Reference.from_dict(d.pop("season"))

        team = Reference.from_dict(d.pop("team"))

        trade_kicker = AthleteContractTradeKicker.from_dict(d.pop("tradeKicker"))

        trade_restriction = d.pop("tradeRestriction")

        unsigned_foreign_pick = d.pop("unsignedForeignPick")

        active = d.pop("active")

        athlete_contract = cls(
            ref=ref,
            bird_status=bird_status,
            base_year_compensation=base_year_compensation,
            poison_pill_provision=poison_pill_provision,
            incoming_trade_value=incoming_trade_value,
            outgoing_trade_value=outgoing_trade_value,
            minimum_salary_exception=minimum_salary_exception,
            option_type=option_type,
            salary=salary,
            salary_remaining=salary_remaining,
            years_remaining=years_remaining,
            season=season,
            team=team,
            trade_kicker=trade_kicker,
            trade_restriction=trade_restriction,
            unsigned_foreign_pick=unsigned_foreign_pick,
            active=active,
        )

        athlete_contract.additional_properties = d
        return athlete_contract

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
