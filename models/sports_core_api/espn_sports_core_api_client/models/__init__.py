"""Contains all the data models used in inputs/outputs"""

from .address import Address
from .alternate_ids import AlternateIDS
from .athlete_details_response import AthleteDetailsResponse
from .athlete_details_response_alternate_ids import AthleteDetailsResponseAlternateIds
from .athlete_details_response_experience import AthleteDetailsResponseExperience
from .athlete_reference import AthleteReference
from .athlete_statistics_log_response import AthleteStatisticsLogResponse
from .athlete_statistics_response import AthleteStatisticsResponse
from .athlete_statistics_response_splits import AthleteStatisticsResponseSplits
from .athlete_status import AthleteStatus
from .calendar_list_response import CalendarListResponse
from .competition_broadcast import CompetitionBroadcast
from .competition_competitor import CompetitionCompetitor
from .competition_competitor_leaders_type_1 import CompetitionCompetitorLeadersType1
from .competition_competitor_linescores_type_1 import CompetitionCompetitorLinescoresType1
from .competition_competitor_record_type_1 import CompetitionCompetitorRecordType1
from .competition_competitor_roster_type_1 import CompetitionCompetitorRosterType1
from .competition_competitor_score_type_1 import CompetitionCompetitorScoreType1
from .competition_competitor_statistics_type_1 import CompetitionCompetitorStatisticsType1
from .competition_competitor_team_type_1 import CompetitionCompetitorTeamType1
from .competition_detail import CompetitionDetail
from .competition_detail_notes_item import CompetitionDetailNotesItem
from .competition_format import CompetitionFormat
from .competition_overtime import CompetitionOvertime
from .competition_situation_response import CompetitionSituationResponse
from .competition_source import CompetitionSource
from .competition_status import CompetitionStatus
from .competition_status_type import CompetitionStatusType
from .competition_type import CompetitionType
from .core_nfl_season_team_response import CoreNflSeasonTeamResponse
from .drive import Drive
from .drive_clock import DriveClock
from .drive_field_position import DriveFieldPosition
from .drive_period import DrivePeriod
from .drive_source import DriveSource
from .drive_time_elapsed import DriveTimeElapsed
from .drives_list_response import DrivesListResponse
from .error_response import ErrorResponse
from .error_response_error import ErrorResponseError
from .event_detail import EventDetail
from .event_detail_competitions_item_type_1 import EventDetailCompetitionsItemType1
from .event_detail_league_type_1 import EventDetailLeagueType1
from .event_detail_season_type_1 import EventDetailSeasonType1
from .event_detail_season_type_type_1 import EventDetailSeasonTypeType1
from .event_detail_venues_item_type_1 import EventDetailVenuesItemType1
from .event_detail_week_type_1 import EventDetailWeekType1
from .event_reference import EventReference
from .get_league_season_weeks_season_type import GetLeagueSeasonWeeksSeasonType
from .get_nfl_conference_standings_seasontype import GetNFLConferenceStandingsSeasontype
from .last_play_reference import LastPlayReference
from .league_enum import LeagueEnum
from .link import Link
from .logo import Logo
from .nfl_athlete_eventlog_response import NflAthleteEventlogResponse
from .nfl_athlete_eventlog_response_events import NflAthleteEventlogResponseEvents
from .nfl_athlete_eventlog_response_events_items_item import NflAthleteEventlogResponseEventsItemsItem
from .nfl_athlete_eventlog_response_teams import NflAthleteEventlogResponseTeams
from .nfl_athlete_eventlog_response_teams_additional_property import NflAthleteEventlogResponseTeamsAdditionalProperty
from .nfl_athlete_injury import NflAthleteInjury
from .nfl_athlete_injury_athlete_type_1 import NflAthleteInjuryAthleteType1
from .nfl_athlete_injury_source import NflAthleteInjurySource
from .nfl_athlete_injury_team_type_1 import NflAthleteInjuryTeamType1
from .nfl_athlete_injury_type import NflAthleteInjuryType
from .nfl_conference_standings_item import NflConferenceStandingsItem
from .nfl_conference_standings_response import NflConferenceStandingsResponse
from .nfl_draft_athlete_analysis import NflDraftAthleteAnalysis
from .nfl_draft_athlete_attribute import NflDraftAthleteAttribute
from .nfl_draft_athlete_response import NflDraftAthleteResponse
from .nfl_draft_pick import NflDraftPick
from .nfl_draft_pick_status import NflDraftPickStatus
from .nfl_draft_position import NflDraftPosition
from .nfl_draft_response import NflDraftResponse
from .nfl_draft_round import NflDraftRound
from .nfl_draft_round_detail import NflDraftRoundDetail
from .nfl_draft_round_status import NflDraftRoundStatus
from .nfl_draft_rounds_response import NflDraftRoundsResponse
from .nfl_draft_team import NflDraftTeam
from .nfl_draft_team_need import NflDraftTeamNeed
from .nfl_leader import NflLeader
from .nfl_leaders_category import NflLeadersCategory
from .nfl_leaders_response import NflLeadersResponse
from .nfl_team_depthchart_athlete import NflTeamDepthchartAthlete
from .nfl_team_depthchart_group import NflTeamDepthchartGroup
from .nfl_team_depthchart_group_positions import NflTeamDepthchartGroupPositions
from .nfl_team_depthchart_position import NflTeamDepthchartPosition
from .nfl_team_depthchart_response import NflTeamDepthchartResponse
from .paginated_reference_list_response import PaginatedReferenceListResponse
from .play import Play
from .play_clock import PlayClock
from .play_field_position import PlayFieldPosition
from .play_participant import PlayParticipant
from .play_participant_athlete_type_1 import PlayParticipantAthleteType1
from .play_participant_position_type_1 import PlayParticipantPositionType1
from .play_participant_statistics_type_1 import PlayParticipantStatisticsType1
from .play_period import PlayPeriod
from .play_probability_type_1 import PlayProbabilityType1
from .play_stat import PlayStat
from .play_type import PlayType
from .plays_list_response import PlaysListResponse
from .position import Position
from .reference import Reference
from .season import Season
from .sport_enum import SportEnum
from .statistic import Statistic
from .statistic_category import StatisticCategory
from .statistics_log_entry import StatisticsLogEntry
from .statistics_reference import StatisticsReference
from .statistics_type_entry import StatisticsTypeEntry
from .team import Team
from .team_reference import TeamReference
from .venue import Venue

__all__ = (
    "Address",
    "AlternateIDS",
    "AthleteDetailsResponse",
    "AthleteDetailsResponseAlternateIds",
    "AthleteDetailsResponseExperience",
    "AthleteReference",
    "AthleteStatisticsLogResponse",
    "AthleteStatisticsResponse",
    "AthleteStatisticsResponseSplits",
    "AthleteStatus",
    "CalendarListResponse",
    "CompetitionBroadcast",
    "CompetitionCompetitor",
    "CompetitionCompetitorLeadersType1",
    "CompetitionCompetitorLinescoresType1",
    "CompetitionCompetitorRecordType1",
    "CompetitionCompetitorRosterType1",
    "CompetitionCompetitorScoreType1",
    "CompetitionCompetitorStatisticsType1",
    "CompetitionCompetitorTeamType1",
    "CompetitionDetail",
    "CompetitionDetailNotesItem",
    "CompetitionFormat",
    "CompetitionOvertime",
    "CompetitionSituationResponse",
    "CompetitionSource",
    "CompetitionStatus",
    "CompetitionStatusType",
    "CompetitionType",
    "CoreNflSeasonTeamResponse",
    "Drive",
    "DriveClock",
    "DriveFieldPosition",
    "DrivePeriod",
    "DrivesListResponse",
    "DriveSource",
    "DriveTimeElapsed",
    "ErrorResponse",
    "ErrorResponseError",
    "EventDetail",
    "EventDetailCompetitionsItemType1",
    "EventDetailLeagueType1",
    "EventDetailSeasonType1",
    "EventDetailSeasonTypeType1",
    "EventDetailVenuesItemType1",
    "EventDetailWeekType1",
    "EventReference",
    "GetLeagueSeasonWeeksSeasonType",
    "GetNFLConferenceStandingsSeasontype",
    "LastPlayReference",
    "LeagueEnum",
    "Link",
    "Logo",
    "NflAthleteEventlogResponse",
    "NflAthleteEventlogResponseEvents",
    "NflAthleteEventlogResponseEventsItemsItem",
    "NflAthleteEventlogResponseTeams",
    "NflAthleteEventlogResponseTeamsAdditionalProperty",
    "NflAthleteInjury",
    "NflAthleteInjuryAthleteType1",
    "NflAthleteInjurySource",
    "NflAthleteInjuryTeamType1",
    "NflAthleteInjuryType",
    "NflConferenceStandingsItem",
    "NflConferenceStandingsResponse",
    "NflDraftAthleteAnalysis",
    "NflDraftAthleteAttribute",
    "NflDraftAthleteResponse",
    "NflDraftPick",
    "NflDraftPickStatus",
    "NflDraftPosition",
    "NflDraftResponse",
    "NflDraftRound",
    "NflDraftRoundDetail",
    "NflDraftRoundsResponse",
    "NflDraftRoundStatus",
    "NflDraftTeam",
    "NflDraftTeamNeed",
    "NflLeader",
    "NflLeadersCategory",
    "NflLeadersResponse",
    "NflTeamDepthchartAthlete",
    "NflTeamDepthchartGroup",
    "NflTeamDepthchartGroupPositions",
    "NflTeamDepthchartPosition",
    "NflTeamDepthchartResponse",
    "PaginatedReferenceListResponse",
    "Play",
    "PlayClock",
    "PlayFieldPosition",
    "PlayParticipant",
    "PlayParticipantAthleteType1",
    "PlayParticipantPositionType1",
    "PlayParticipantStatisticsType1",
    "PlayPeriod",
    "PlayProbabilityType1",
    "PlaysListResponse",
    "PlayStat",
    "PlayType",
    "Position",
    "Reference",
    "Season",
    "SportEnum",
    "Statistic",
    "StatisticCategory",
    "StatisticsLogEntry",
    "StatisticsReference",
    "StatisticsTypeEntry",
    "Team",
    "TeamReference",
    "Venue",
)
