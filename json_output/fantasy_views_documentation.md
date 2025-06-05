# ESPN Fantasy Football Player Views Characteristics

## allon

**Description**: All available player data combined

**Use Case**: Comprehensive analysis, data export

**Data Fields**:
- ✓ Basic player information (name, ID)
- ✓ Statistical data
- ✓ Ownership percentages
- ✓ Draft rankings
- ✓ Injury status
- ✓ Position eligibility
- ✓ Additional fields: activationInfo, draftedSeasonId, historicalInjuryStatus, dateUniverseChanged, laterality

---

## kona_player_info

**Description**: General player information with ownership and draft data

**Use Case**: Player research, draft preparation, waiver wire decisions

**Data Fields**:
- ✓ Basic player information (name, ID)
- ✓ Statistical data
- ✓ Ownership percentages
- ✓ Draft rankings
- ✓ Injury status
- ✓ Position eligibility

---

## mBoxscore

**Description**: Detailed statistical boxscore

**Use Case**: Post-game analysis, statistical breakdown

**Data Fields**:
- ✓ Basic player information (name, ID)
- ✓ Statistical data
- ✓ Injury status
- ✓ Additional fields: universeId

---

## mDraftDetail

**Description**: Draft-specific player details

**Use Case**: Draft preparation, ADP analysis

**Note**: This view returns empty player objects without specific filters or league context.

---

## mLiveScoring

**Description**: Live scoring and real-time stats

**Use Case**: In-game tracking, live fantasy scoring

**Data Fields**:
- ✓ Basic player information (name, ID)
- ✓ Statistical data
- ✓ Injury status

---

## mMatchup

**Description**: Matchup-specific player information

**Use Case**: Head-to-head matchup analysis

**Data Fields**:
- ✓ Basic player information (name, ID)
- ✓ Injury status
- ✓ Position eligibility
- ✓ Additional fields: universeId

---

## mMatchupScore

**Description**: Matchup scoring details

**Use Case**: Scoring breakdown for matchups

**Note**: This view returns empty player objects without specific filters or league context.

---

## mRoster

**Description**: Complete roster information

**Use Case**: Full roster management, lineup decisions

**Data Fields**:
- ✓ Basic player information (name, ID)
- ✓ Statistical data
- ✓ Ownership percentages
- ✓ Draft rankings
- ✓ Injury status
- ✓ Position eligibility
- ✓ Additional fields: universeId

---

## mStandings

**Description**: Standings-related player data

**Use Case**: League standings context

**Note**: This view returns empty player objects without specific filters or league context.

---

## mTeam

**Description**: Team-oriented player data

**Use Case**: Team roster management

**Note**: This view returns empty player objects without specific filters or league context.

---

## players_wl

**Description**: Waiver wire and free agent focused data

**Use Case**: Waiver wire decisions, free agent pickups

**Data Fields**:
- ✓ Basic player information (name, ID)
- ✓ Ownership percentages
- ✓ Injury status
- ✓ Position eligibility
- ✓ Additional fields: universeId

---

