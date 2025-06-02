## Athletes:

https://partners.api.espn.com/v2/sports/football/nfl/athletes?limit=7000

https://sports.core.api.espn.com/v3/sports/football/nfl/athletes?page=1&limit=20000

## Events

`https://partners.api.espn.com/v2/sports/football/nfl/events?limit=1000`  
[&dates=20230101-20240101][daterange] or [&dates=20230101][singledate] or [&dates=2023][season]  

## Fantasy

`https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{{YEAR}}/players?view={{VIEW_NAME}}`  

```sh
# To get more than 50 items, run in terminal:
curl -H 'X-Fantasy-Filter: {"games":{"limit":2000}}' <URL>
```

**Views (that I know of):**

* [~~mDraftDetail~~](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=mDraftDetail)
* [mLiveScoring](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=mLiveScoring)
* [mMatchup](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=mMatchup)
* [mTeam](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=mTeam)
* [mMatchupScore](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=mMatchupScore)
* [mStandings](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=mStandings)
* [mRoster](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=mRoster)
* [mBoxscore](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=mBoxscore)
* [kona_player_info](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=kona_player_info)
* [player_wl](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=player_wl)
* [allon](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/players?view=allon)


## Stat column names

```
id   displayid  abbrev    description
---  ---------  --------  --------------------------------
0    7          PA        Each Pass Attempted
1    8          PC        Each Pass Completed
2    11         INC       Each Incomplete Pass
3    0          PY        Passing Yards
4    14         PTD       TD Pass
5    1          PY5       Every 5 passing yards
6    2          PY10      Every 10 passing yards
```

<details><summary>View more</summary>

```
id   displayid  abbrev    description
---  ---------  --------  --------------------------------
0    7          PA        Each Pass Attempted
1    8          PC        Each Pass Completed
2    11         INC       Each Incomplete Pass
3    0          PY        Passing Yards
4    14         PTD       TD Pass
5    1          PY5       Every 5 passing yards
6    2          PY10      Every 10 passing yards
7    3          PY20      Every 20 passing yards 
8    4          PY25      Every 25 passing yards 
9    5          PY50      Every 50 passing yards
10   6          PY100     Every 100 passing yards
11   9          PC5       Every 5 pass completions
12   10         PC10      Every 10 pass completions
13   12         IP5       Every 5 pass incompletions
14   13         IP10      Every 10 pass incompletions
15   15         PTD40     40+ yard TD pass bonus
16   16         PTD50     50+ yard TD pass bonus
17   20         P300      300-399 yard passing game
18   21         P400      400+ yard passing game
19   19         2PC       2pt Passing Conversion
20   18         INTT      Interceptions Thrown
21   155        CPCT      Passing Completion Pct
22   156        PYPG      Passing Yards Per Game
23   30         RA        Rushing Attempts
24   23         RY        Rushing Yards
25   33         RTD       TD Rush
26   37         2PR       2pt Rushing Conversion
27   24         RY5       Every 5 rushing yards
28   25         RY10      Every 10 rushing yards
29   26         RY20      Every 20 rushing yards
30   27         RY25      Every 25 rushing yards 
31   28         RY50      Every 50 rushing yards
32   29         R100      Every 100 rushing yards
33   31         RA5       Every 5 rush attempts
34   32         RA10      Every 10 rush attempts
35   34         RTD40     40+ yard TD rush bonus
36   35         RTD50     50+ yard TD rush bonus
37   38         RY100     100-199 yard rushing game
38   39         RY200     200+ yard rushing game
39   157        RYPA      Rushing Yards Per Attempt
40   158        RYPG      Rushing Yards Per Game
41   159        RECS      Receptions
42   40         REY       Receiving Yards
43   50         RETD      TD Reception
44   54         2PRE      2pt Receiving Conversion
45   51         RETD40    40+ yard TD rec bonus
46   52         RETD50    50+ yard TD rec bonus
47   41         REY5      Every 5 receiving yards
48   42         REY10     Every 10 receiving yards
49   43         REY20     Every 20 receiving yards
50   44         REY25     Every 25 receiving yards
51   45         REY50     Every 50 receiving yards
52   46         RE100     Every 100 receiving yards
53   47         REC       Each reception
54   48         REC5      Every 5 receptions
55   49         REC10     Every 10 receptions
56   55         REY100    100-199 yard receiving game
57   56         REY200    200+ yard receiving game
58   57         RET       Receiving Target
59   160        YAC       Receiving Yards After Catch
60   161        YPC       Receiving Yards Per Catch
61   162        REYPG     Receiving Yards Per Game
62   163        PTL       Total 2pt Conversions
63   66         FTD       Fumble Recovered for TD
64   22         SKD       Sacked
65   164        PFUM      Passing Fumbles
66   165        RFUM      Rushing Fumbles
67   166        REFUM     Receiving Fumbles
68   67         FUM       Total Fumbles
69   167        PFUML     Passing Fumbles Lost
70   168        RFUML     Rushing Fumbles Lost
71   169        REFUML    Receiving Fumbles Lost
72   68         FUML      Total Fumbles Lost
73   170        TT        Total Turnovers
74   84         FG50P     FG Made (50+ yards)
75   171        FGA50P    FG Attempted (50+ yards)
76   172        FGM50P    FG Missed (50+ yards)
77   83         FG40      FG Made (40-49 yards)
78   86         FGA40     FG Attempted (40-49 yards)
79   89         FGM40     FG Missed (40-49 yards)
80   82         FG0       FG Made (0-39 yards)
81   85         FGA0      FG Attempted (0-39 yards)
82   88         FGM0      FG Missed (0-39 yards)
83   79         FG        Total FG Made
84   80         FGA       Total FG Attempted
85   81         FGM       Total FG Missed
86   76         PAT       Each PAT Made
87   77         PATA      Each PAT Attempted
88   78         PATM      Each PAT Missed
89   136        PA0       0 points allowed
90   137        PA1       1-6 points allowed
91   138        PA7       7-13 points allowed
92   139        PA14      14-17 points allowed
93   73         BLKKRTD   Blocked Punt or FG return for TD
94   173        DEFRETTD  Fumble or INT Return for TD
95   113        INT       Each Interception
96   114        FR        Each Fumble Recovered
97   112        BLKK      Blocked Punt, PAT or FG
98   116        SF        Each Safety
99   107        SK        Each Sack
100  108        HALFSK    1/2 Sack
101  64         KRTD      Kickoff Return TD
102  65         PRTD      Punt Return TD
103  71         INTTD     Interception Return TD
104  72         FRTD      Fumble Return TD
105  174        TRTD      Total Return TD
106  115        FF        Each Fumble Forced
107  117        TKA       Assisted Tackles
108  118        TKS       Solo Tackles
109  109        TK        Total Tackles
110  110        TK3       Every 3 Total Tackles
111  111        TK5       Every 5 Total Tackles
112  119        STF       Stuffs
113  120        PD        Passes Defensed
114  58         KR        Kickoff Return Yards
115  61         PR        Punt Return Yards
116  59         KR10      Every 10 kickoff return yards
117  60         KR25      Every 25 kickoff return yards
118  62         PR10      Every 10 punt return yards
119  63         PR25      Every 25 punt return yards
120  135        PTSA      Points Allowed
121  140        PA18      18-21 points allowed
122  141        PA22      22-27 points allowed
123  142        PA28      28-34 points allowed
124  143        PA35      35-45 points allowed
125  144        PA46      46+ points allowed
126  175        PAPG      Points Allowed Per Game
127  145        YA        Yards Allowed
128  146        YA100     Less than 100 total yards allowed
129  147        YA199     100-199 total yards allowed
130  148        YA299     200-299 total yards allowed
131  149        YA349     300-349 total yards allowed
132  150        YA399     350-399 total yards allowed
133  151        YA449     400-449 total yards allowed
134  152        YA499     450-499 total yards allowed
135  153        YA549     500-549 total yards allowed
136  154        YA550     550+ total yards allowed
137  176        YAPG      Yards Allowed Per Game
138  91         PT        Net Punts
139  92         PTY       Punt Yards
140  93         PT10      Punts Inside the 10
141  94         PT20      Punts Inside the 20
142  95         PTB       Blocked Punts
143  96         PTR       Punts Returned
144  97         PTRY      Punt Return Yards
145  98         PTTB      Touchbacks
146  99         PTFC      Fair Catches
147  177        PTAVG     Punt Average
148  100        PTA44     Punt Average 44.0+
149  101        PTA42     Punt Average 42.0-43.9
150  102        PTA40     Punt Average 40.0-41.9
151  103        PTA38     Punt Average 38.0-39.9
152  104        PTA36     Punt Average 36.0-37.9
153  105        PTA34     Punt Average 34.0-35.9
154  106        PTA33     Punt Average 33.9 or less
155  69         TW        Team Win
156  70         TL        Team Loss
157  121        TIE       Team Tie
158  122        PTS       Points Scored
159  178        PPG       Points Scored Per Game
160  179        MGN       Margin of Victory
161  123        WM25      25+ point Win Margin
162  124        WM20      20-24 point Win Margin
163  125        WM15      15-19 point Win Margin
164  126        WM10      10-14 point Win Margin
165  127        WM5       5-9 point Win Margin
166  128        WM1       1-4 point Win Margin
167  129        LM1       1-4 point Loss Margin
168  130        LM5       5-9 point Loss Margin
169  131        LM10      10-14 point Loss Margin
170  132        LM15      15-19 point Loss Margin
171  133        LM20      20-24 point Loss Margin
172  134        LM25      25+ point Loss Margin
173  180        MGNPG     Margin of Victory Per Game
174  181        WINPCT    Winning Pct
175  182        PTD0      0-9 yd TD pass bonus
176  183        PTD10     10-19 yd TD pass bonus
177  184        PTD20     20-29 yd TD pass bonus
178  185        PTD30     30-39 yd TD pass bonus
179  186        RTD0      0-9 yd TD rush bonus
180  187        RTD10     10-19 yd TD rush bonus
181  188        RTD20     20-29 yd TD rush bonus
182  189        RTD30     30-39 yd TD rush bonus
183  190        RETD0     0-9 yd TD rec bonus
184  191        RETD10    10-19 yd TD rec bonus
185  192        RETD20    20-29 yd TD rec bonus
186  193        RETD30    30-39 yd TD rec bonus
187  194        DPTSA     D/ST Points Allowed
188  195        DPA0      D/ST 0 points allowed
189  196        DPA1      D/ST 1-6 points allowed
190  197        DPA7      D/ST 7-13 points allowed
191  198        DPA14     D/ST 14-17 points allowed
192  199        DPA18     D/ST 18-21 points allowed
193  200        DPA22     D/ST 22-27 points allowed
194  201        DPA28     D/ST 28-34 points allowed
195  202        DPA35     D/ST 35-45 points allowed
196  203        DPA46     D/ST 46+ points allowed
197  204        DPAPG     D/ST Points Allowed Per Game
198  205        FG50      FG Made (50-59 yards)
199  87         FGA50     FG Attempted (50-59 yards)
200  90         FGM50     FG Missed (50-59 yards)
201  206        FG60      FG Made (60+ yards)
202  207        FGA60     FG Attempted (60+ yards)
203  208        FGM60     FG Missed (60+ yards)
204  209        O2PRET    Offensive 2pt Return
205  210        D2PRET    Defensive 2pt Return
206  74         2PRET     2pt Return
207  211        O1PSF     Offensive 1pt Safety
208  212        D1PSF     Defensive 1pt Safety
209  75         1PSF      1pt Safety
210  213        GP        Games Played
211  17         PFD       Passing First Down
212  36         RFD       Rushing First Down
213  53         REFD      Receiving First Down
214  214        FGY       FG Made Yards
215  215        FGMY      FG Missed Yards
216  216        FGAY      FG Attempt Yards
217  217        FGY5      Every 5 FG Made yards
218  218        FGY10     Every 10 FG Made yards
219  219        FGY20     Every 20 FG Made yards
220  220        FGY25     Every 25 FG Made yards
221  221        FGY50     Every 50 FG Made yards
222  222        FGY100    Every 100 FG Made yards
223  223        FGMY5     Every 5 FG Missed yards
224  224        FGMY10    Every 10 FG Missed yards
225  225        FGMY20    Every 20 FG Missed yards
226  226        FGMY25    Every 25 FG Missed yards
227  227        FGMY50    Every 50 FG Missed yards
228  228        FGMY100   Every 100 FG Missed yards
229  229        FGAY5     Every 5 FG Attempt yards
230  230        FGAY10    Every 10 FG Attempt yards
231  231        FGAY20    Every 20 FG Attempt yards
232  232        FGAY25    Every 25 FG Attempt yards
233  233        FGAY50    Every 50 FG Attempt yards
234  234        FGAY100   Every 100 FG Attempt yards
```

</details>


[daterange]: https://partners.api.espn.com/v2/sports/football/nfl/events?dates=20230101-20240101&limit=1000
[singledate]: https://partners.api.espn.com/v2/sports/football/nfl/events?dates=20230101&limit=1000
[season]: https://partners.api.espn.com/v2/sports/football/nfl/events?dates=2023&limit=1000