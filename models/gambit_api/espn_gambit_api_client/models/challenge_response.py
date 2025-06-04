from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.challenge_response_scoring_periods_item import ChallengeResponseScoringPeriodsItem
    from ..models.challenge_response_settings import ChallengeResponseSettings
    from ..models.proposition import Proposition


T = TypeVar("T", bound="ChallengeResponse")


@_attrs_define
class ChallengeResponse:
    """
    Attributes:
        id (Union[Unset, str]): Challenge ID
        key (Union[Unset, str]): Challenge key/name
        name (Union[Unset, str]): Display name
        abbrev (Union[Unset, str]): Abbreviation
        active (Union[Unset, bool]):
        game_id (Union[Unset, int]): Associated game ID
        current_scoring_period (Union[Unset, int]): Current scoring period
        requested_scoring_period_id (Union[Unset, int]): Requested scoring period
        start_date (Union[Unset, int]): Start date as Unix timestamp in milliseconds
        end_date (Union[Unset, int]): End date as Unix timestamp in milliseconds
        state (Union[Unset, str]): Challenge state (e.g., 'active')
        settings (Union[Unset, ChallengeResponseSettings]):
        propositions (Union[Unset, List['Proposition']]):
        scoring_periods (Union[Unset, List['ChallengeResponseScoringPeriodsItem']]):
        leaderboard_sort_options (Union[Unset, List[str]]):
    """

    id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    abbrev: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    game_id: Union[Unset, int] = UNSET
    current_scoring_period: Union[Unset, int] = UNSET
    requested_scoring_period_id: Union[Unset, int] = UNSET
    start_date: Union[Unset, int] = UNSET
    end_date: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    settings: Union[Unset, "ChallengeResponseSettings"] = UNSET
    propositions: Union[Unset, List["Proposition"]] = UNSET
    scoring_periods: Union[Unset, List["ChallengeResponseScoringPeriodsItem"]] = UNSET
    leaderboard_sort_options: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        key = self.key

        name = self.name

        abbrev = self.abbrev

        active = self.active

        game_id = self.game_id

        current_scoring_period = self.current_scoring_period

        requested_scoring_period_id = self.requested_scoring_period_id

        start_date = self.start_date

        end_date = self.end_date

        state = self.state

        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        propositions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.propositions, Unset):
            propositions = []
            for propositions_item_data in self.propositions:
                propositions_item = propositions_item_data.to_dict()
                propositions.append(propositions_item)

        scoring_periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scoring_periods, Unset):
            scoring_periods = []
            for scoring_periods_item_data in self.scoring_periods:
                scoring_periods_item = scoring_periods_item_data.to_dict()
                scoring_periods.append(scoring_periods_item)

        leaderboard_sort_options: Union[Unset, List[str]] = UNSET
        if not isinstance(self.leaderboard_sort_options, Unset):
            leaderboard_sort_options = self.leaderboard_sort_options

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if abbrev is not UNSET:
            field_dict["abbrev"] = abbrev
        if active is not UNSET:
            field_dict["active"] = active
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if current_scoring_period is not UNSET:
            field_dict["currentScoringPeriod"] = current_scoring_period
        if requested_scoring_period_id is not UNSET:
            field_dict["requestedScoringPeriodId"] = requested_scoring_period_id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if state is not UNSET:
            field_dict["state"] = state
        if settings is not UNSET:
            field_dict["settings"] = settings
        if propositions is not UNSET:
            field_dict["propositions"] = propositions
        if scoring_periods is not UNSET:
            field_dict["scoringPeriods"] = scoring_periods
        if leaderboard_sort_options is not UNSET:
            field_dict["leaderboardSortOptions"] = leaderboard_sort_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.challenge_response_scoring_periods_item import ChallengeResponseScoringPeriodsItem
        from ..models.challenge_response_settings import ChallengeResponseSettings
        from ..models.proposition import Proposition

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        abbrev = d.pop("abbrev", UNSET)

        active = d.pop("active", UNSET)

        game_id = d.pop("gameId", UNSET)

        current_scoring_period = d.pop("currentScoringPeriod", UNSET)

        requested_scoring_period_id = d.pop("requestedScoringPeriodId", UNSET)

        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        state = d.pop("state", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, ChallengeResponseSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ChallengeResponseSettings.from_dict(_settings)

        propositions = []
        _propositions = d.pop("propositions", UNSET)
        for propositions_item_data in _propositions or []:
            propositions_item = Proposition.from_dict(propositions_item_data)

            propositions.append(propositions_item)

        scoring_periods = []
        _scoring_periods = d.pop("scoringPeriods", UNSET)
        for scoring_periods_item_data in _scoring_periods or []:
            scoring_periods_item = ChallengeResponseScoringPeriodsItem.from_dict(scoring_periods_item_data)

            scoring_periods.append(scoring_periods_item)

        leaderboard_sort_options = cast(List[str], d.pop("leaderboardSortOptions", UNSET))

        challenge_response = cls(
            id=id,
            key=key,
            name=name,
            abbrev=abbrev,
            active=active,
            game_id=game_id,
            current_scoring_period=current_scoring_period,
            requested_scoring_period_id=requested_scoring_period_id,
            start_date=start_date,
            end_date=end_date,
            state=state,
            settings=settings,
            propositions=propositions,
            scoring_periods=scoring_periods,
            leaderboard_sort_options=leaderboard_sort_options,
        )

        challenge_response.additional_properties = d
        return challenge_response

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
