import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_details_alternate_ids import AthleteDetailsAlternateIds
    from ..models.athlete_details_college import AthleteDetailsCollege
    from ..models.birth_place import BirthPlace
    from ..models.draft import Draft
    from ..models.experience import Experience
    from ..models.flag_type_0 import FlagType0
    from ..models.hand_type_0 import HandType0
    from ..models.headshot import Headshot
    from ..models.injury import Injury
    from ..models.link import Link
    from ..models.note import Note
    from ..models.position import Position
    from ..models.reference import Reference
    from ..models.status import Status
    from ..models.team import Team
    from ..models.team_reference import TeamReference


T = TypeVar("T", bound="AthleteDetails")


@_attrs_define
class AthleteDetails:
    r"""
    Attributes:
        id (str):  Example: 2330.
        uid (str):  Example: s:20~a:2330.
        guid (str):  Example: 02927b1c67269964a3263940c6c17491.
        type (str):  Example: football.
        first_name (str):  Example: Tom.
        last_name (str):  Example: Brady.
        full_name (str):  Example: Tom Brady.
        display_name (str):  Example: Tom Brady.
        alternate_ids (Union[Unset, AthleteDetailsAlternateIds]):
        short_name (Union[Unset, str]):  Example: T. Brady.
        weight (Union[Unset, float]):  Example: 225.
        display_weight (Union[Unset, str]):  Example: 225 lbs.
        height (Union[Unset, float]):  Example: 76.
        display_height (Union[Unset, str]):  Example: 6' 4\".
        age (Union[Unset, int]):  Example: 46.
        date_of_birth (Union[Unset, datetime.datetime]):  Example: 1977-08-03T07:00:00Z.
        links (Union[Unset, List['Link']]):
        birth_place (Union[Unset, BirthPlace]):
        college (Union[Unset, AthleteDetailsCollege]):
        slug (Union[Unset, str]):  Example: tom-brady.
        headshot (Union[Unset, Headshot]):
        jersey (Union[Unset, str]):  Example: 12.
        position (Union[Unset, Position]):
        injuries (Union[List['Injury'], None, Unset]):
        teams (Union[Unset, List[Union['Team', 'TeamReference']]]):
        experience (Union[Unset, Experience]):
        status (Union[Unset, Status]):
        event_log (Union[Unset, Reference]):
        active (Union[Unset, bool]):  Example: True.
        debut_year (Union[Unset, int]):  Example: 2000.
        draft (Union[Unset, Draft]):
        notes (Union[List['Note'], None, Unset]):
        hand (Union['HandType0', None, Unset]):
        transactions (Union[Unset, Reference]):
        flag (Union['FlagType0', None, Unset]):
        career (Union[Unset, Reference]):
    """

    id: str
    uid: str
    guid: str
    type: str
    first_name: str
    last_name: str
    full_name: str
    display_name: str
    alternate_ids: Union[Unset, "AthleteDetailsAlternateIds"] = UNSET
    short_name: Union[Unset, str] = UNSET
    weight: Union[Unset, float] = UNSET
    display_weight: Union[Unset, str] = UNSET
    height: Union[Unset, float] = UNSET
    display_height: Union[Unset, str] = UNSET
    age: Union[Unset, int] = UNSET
    date_of_birth: Union[Unset, datetime.datetime] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    birth_place: Union[Unset, "BirthPlace"] = UNSET
    college: Union[Unset, "AthleteDetailsCollege"] = UNSET
    slug: Union[Unset, str] = UNSET
    headshot: Union[Unset, "Headshot"] = UNSET
    jersey: Union[Unset, str] = UNSET
    position: Union[Unset, "Position"] = UNSET
    injuries: Union[List["Injury"], None, Unset] = UNSET
    teams: Union[Unset, List[Union["Team", "TeamReference"]]] = UNSET
    experience: Union[Unset, "Experience"] = UNSET
    status: Union[Unset, "Status"] = UNSET
    event_log: Union[Unset, "Reference"] = UNSET
    active: Union[Unset, bool] = UNSET
    debut_year: Union[Unset, int] = UNSET
    draft: Union[Unset, "Draft"] = UNSET
    notes: Union[List["Note"], None, Unset] = UNSET
    hand: Union["HandType0", None, Unset] = UNSET
    transactions: Union[Unset, "Reference"] = UNSET
    flag: Union["FlagType0", None, Unset] = UNSET
    career: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.flag_type_0 import FlagType0
        from ..models.hand_type_0 import HandType0
        from ..models.team import Team

        id = self.id

        uid = self.uid

        guid = self.guid

        type = self.type

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        display_name = self.display_name

        alternate_ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alternate_ids, Unset):
            alternate_ids = self.alternate_ids.to_dict()

        short_name = self.short_name

        weight = self.weight

        display_weight = self.display_weight

        height = self.height

        display_height = self.display_height

        age = self.age

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        birth_place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_place, Unset):
            birth_place = self.birth_place.to_dict()

        college: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.college, Unset):
            college = self.college.to_dict()

        slug = self.slug

        headshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headshot, Unset):
            headshot = self.headshot.to_dict()

        jersey = self.jersey

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        injuries: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.injuries, Unset):
            injuries = UNSET
        elif isinstance(self.injuries, list):
            injuries = []
            for injuries_type_0_item_data in self.injuries:
                injuries_type_0_item = injuries_type_0_item_data.to_dict()
                injuries.append(injuries_type_0_item)

        else:
            injuries = self.injuries

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item: Dict[str, Any]
                if isinstance(teams_item_data, Team):
                    teams_item = teams_item_data.to_dict()
                else:
                    teams_item = teams_item_data.to_dict()

                teams.append(teams_item)

        experience: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.experience, Unset):
            experience = self.experience.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        event_log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event_log, Unset):
            event_log = self.event_log.to_dict()

        active = self.active

        debut_year = self.debut_year

        draft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        notes: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.notes, Unset):
            notes = UNSET
        elif isinstance(self.notes, list):
            notes = []
            for notes_type_0_item_data in self.notes:
                notes_type_0_item = notes_type_0_item_data.to_dict()
                notes.append(notes_type_0_item)

        else:
            notes = self.notes

        hand: Union[Dict[str, Any], None, Unset]
        if isinstance(self.hand, Unset):
            hand = UNSET
        elif isinstance(self.hand, HandType0):
            hand = self.hand.to_dict()
        else:
            hand = self.hand

        transactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = self.transactions.to_dict()

        flag: Union[Dict[str, Any], None, Unset]
        if isinstance(self.flag, Unset):
            flag = UNSET
        elif isinstance(self.flag, FlagType0):
            flag = self.flag.to_dict()
        else:
            flag = self.flag

        career: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.career, Unset):
            career = self.career.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "guid": guid,
                "type": type,
                "firstName": first_name,
                "lastName": last_name,
                "fullName": full_name,
                "displayName": display_name,
            }
        )
        if alternate_ids is not UNSET:
            field_dict["alternateIds"] = alternate_ids
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if display_weight is not UNSET:
            field_dict["displayWeight"] = display_weight
        if height is not UNSET:
            field_dict["height"] = height
        if display_height is not UNSET:
            field_dict["displayHeight"] = display_height
        if age is not UNSET:
            field_dict["age"] = age
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if links is not UNSET:
            field_dict["links"] = links
        if birth_place is not UNSET:
            field_dict["birthPlace"] = birth_place
        if college is not UNSET:
            field_dict["college"] = college
        if slug is not UNSET:
            field_dict["slug"] = slug
        if headshot is not UNSET:
            field_dict["headshot"] = headshot
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if position is not UNSET:
            field_dict["position"] = position
        if injuries is not UNSET:
            field_dict["injuries"] = injuries
        if teams is not UNSET:
            field_dict["teams"] = teams
        if experience is not UNSET:
            field_dict["experience"] = experience
        if status is not UNSET:
            field_dict["status"] = status
        if event_log is not UNSET:
            field_dict["eventLog"] = event_log
        if active is not UNSET:
            field_dict["active"] = active
        if debut_year is not UNSET:
            field_dict["debutYear"] = debut_year
        if draft is not UNSET:
            field_dict["draft"] = draft
        if notes is not UNSET:
            field_dict["notes"] = notes
        if hand is not UNSET:
            field_dict["hand"] = hand
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if flag is not UNSET:
            field_dict["flag"] = flag
        if career is not UNSET:
            field_dict["career"] = career

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_details_alternate_ids import AthleteDetailsAlternateIds
        from ..models.athlete_details_college import AthleteDetailsCollege
        from ..models.birth_place import BirthPlace
        from ..models.draft import Draft
        from ..models.experience import Experience
        from ..models.flag_type_0 import FlagType0
        from ..models.hand_type_0 import HandType0
        from ..models.headshot import Headshot
        from ..models.injury import Injury
        from ..models.link import Link
        from ..models.note import Note
        from ..models.position import Position
        from ..models.reference import Reference
        from ..models.status import Status
        from ..models.team import Team
        from ..models.team_reference import TeamReference

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        guid = d.pop("guid")

        type = d.pop("type")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        full_name = d.pop("fullName")

        display_name = d.pop("displayName")

        _alternate_ids = d.pop("alternateIds", UNSET)
        alternate_ids: Union[Unset, AthleteDetailsAlternateIds]
        if isinstance(_alternate_ids, Unset):
            alternate_ids = UNSET
        else:
            alternate_ids = AthleteDetailsAlternateIds.from_dict(_alternate_ids)

        short_name = d.pop("shortName", UNSET)

        weight = d.pop("weight", UNSET)

        display_weight = d.pop("displayWeight", UNSET)

        height = d.pop("height", UNSET)

        display_height = d.pop("displayHeight", UNSET)

        age = d.pop("age", UNSET)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, datetime.datetime]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        _birth_place = d.pop("birthPlace", UNSET)
        birth_place: Union[Unset, BirthPlace]
        if isinstance(_birth_place, Unset):
            birth_place = UNSET
        else:
            birth_place = BirthPlace.from_dict(_birth_place)

        _college = d.pop("college", UNSET)
        college: Union[Unset, AthleteDetailsCollege]
        if isinstance(_college, Unset):
            college = UNSET
        else:
            college = AthleteDetailsCollege.from_dict(_college)

        slug = d.pop("slug", UNSET)

        _headshot = d.pop("headshot", UNSET)
        headshot: Union[Unset, Headshot]
        if isinstance(_headshot, Unset):
            headshot = UNSET
        else:
            headshot = Headshot.from_dict(_headshot)

        jersey = d.pop("jersey", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        def _parse_injuries(data: object) -> Union[List["Injury"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                injuries_type_0 = []
                _injuries_type_0 = data
                for injuries_type_0_item_data in _injuries_type_0:
                    injuries_type_0_item = Injury.from_dict(injuries_type_0_item_data)

                    injuries_type_0.append(injuries_type_0_item)

                return injuries_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Injury"], None, Unset], data)

        injuries = _parse_injuries(d.pop("injuries", UNSET))

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:

            def _parse_teams_item(data: object) -> Union["Team", "TeamReference"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    teams_item_type_0 = Team.from_dict(data)

                    return teams_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                teams_item_type_1 = TeamReference.from_dict(data)

                return teams_item_type_1

            teams_item = _parse_teams_item(teams_item_data)

            teams.append(teams_item)

        _experience = d.pop("experience", UNSET)
        experience: Union[Unset, Experience]
        if isinstance(_experience, Unset):
            experience = UNSET
        else:
            experience = Experience.from_dict(_experience)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)

        _event_log = d.pop("eventLog", UNSET)
        event_log: Union[Unset, Reference]
        if isinstance(_event_log, Unset):
            event_log = UNSET
        else:
            event_log = Reference.from_dict(_event_log)

        active = d.pop("active", UNSET)

        debut_year = d.pop("debutYear", UNSET)

        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, Draft]
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = Draft.from_dict(_draft)

        def _parse_notes(data: object) -> Union[List["Note"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notes_type_0 = []
                _notes_type_0 = data
                for notes_type_0_item_data in _notes_type_0:
                    notes_type_0_item = Note.from_dict(notes_type_0_item_data)

                    notes_type_0.append(notes_type_0_item)

                return notes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Note"], None, Unset], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_hand(data: object) -> Union["HandType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hand_type_0 = HandType0.from_dict(data)

                return componentsschemas_hand_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HandType0", None, Unset], data)

        hand = _parse_hand(d.pop("hand", UNSET))

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, Reference]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = Reference.from_dict(_transactions)

        def _parse_flag(data: object) -> Union["FlagType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_flag_type_0 = FlagType0.from_dict(data)

                return componentsschemas_flag_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FlagType0", None, Unset], data)

        flag = _parse_flag(d.pop("flag", UNSET))

        _career = d.pop("career", UNSET)
        career: Union[Unset, Reference]
        if isinstance(_career, Unset):
            career = UNSET
        else:
            career = Reference.from_dict(_career)

        athlete_details = cls(
            id=id,
            uid=uid,
            guid=guid,
            type=type,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            display_name=display_name,
            alternate_ids=alternate_ids,
            short_name=short_name,
            weight=weight,
            display_weight=display_weight,
            height=height,
            display_height=display_height,
            age=age,
            date_of_birth=date_of_birth,
            links=links,
            birth_place=birth_place,
            college=college,
            slug=slug,
            headshot=headshot,
            jersey=jersey,
            position=position,
            injuries=injuries,
            teams=teams,
            experience=experience,
            status=status,
            event_log=event_log,
            active=active,
            debut_year=debut_year,
            draft=draft,
            notes=notes,
            hand=hand,
            transactions=transactions,
            flag=flag,
            career=career,
        )

        athlete_details.additional_properties = d
        return athlete_details

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
