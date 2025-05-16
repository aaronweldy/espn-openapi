from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_standings import NflStandings
    from ..models.nfl_standings_content_config import NflStandingsContentConfig
    from ..models.nfl_standings_content_params import NflStandingsContentParams


T = TypeVar("T", bound="NflStandingsContent")


@_attrs_define
class NflStandingsContent:
    """
    Attributes:
        canonical (Union[Unset, str]):
        config (Union[Unset, NflStandingsContentConfig]):
        description (Union[Unset, str]):
        league (Union[Unset, str]):
        og_type (Union[Unset, str]):
        params (Union[Unset, NflStandingsContentParams]):
        sport (Union[Unset, str]):
        standings (Union[Unset, NflStandings]):
        title (Union[Unset, str]):
    """

    canonical: Union[Unset, str] = UNSET
    config: Union[Unset, "NflStandingsContentConfig"] = UNSET
    description: Union[Unset, str] = UNSET
    league: Union[Unset, str] = UNSET
    og_type: Union[Unset, str] = UNSET
    params: Union[Unset, "NflStandingsContentParams"] = UNSET
    sport: Union[Unset, str] = UNSET
    standings: Union[Unset, "NflStandings"] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        canonical = self.canonical

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        description = self.description

        league = self.league

        og_type = self.og_type

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        sport = self.sport

        standings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = self.standings.to_dict()

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description
        if league is not UNSET:
            field_dict["league"] = league
        if og_type is not UNSET:
            field_dict["og_type"] = og_type
        if params is not UNSET:
            field_dict["params"] = params
        if sport is not UNSET:
            field_dict["sport"] = sport
        if standings is not UNSET:
            field_dict["standings"] = standings
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_standings import NflStandings
        from ..models.nfl_standings_content_config import NflStandingsContentConfig
        from ..models.nfl_standings_content_params import NflStandingsContentParams

        d = src_dict.copy()
        canonical = d.pop("canonical", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, NflStandingsContentConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = NflStandingsContentConfig.from_dict(_config)

        description = d.pop("description", UNSET)

        league = d.pop("league", UNSET)

        og_type = d.pop("og_type", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, NflStandingsContentParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = NflStandingsContentParams.from_dict(_params)

        sport = d.pop("sport", UNSET)

        _standings = d.pop("standings", UNSET)
        standings: Union[Unset, NflStandings]
        if isinstance(_standings, Unset):
            standings = UNSET
        else:
            standings = NflStandings.from_dict(_standings)

        title = d.pop("title", UNSET)

        nfl_standings_content = cls(
            canonical=canonical,
            config=config,
            description=description,
            league=league,
            og_type=og_type,
            params=params,
            sport=sport,
            standings=standings,
            title=title,
        )

        nfl_standings_content.additional_properties = d
        return nfl_standings_content

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
