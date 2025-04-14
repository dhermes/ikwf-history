# Raw bracket data

## Missing data

We have **some** but not **all** data for some years.

- Novice 2000: **MISSING** Team Scores (as of 2025-03-18)
- Senior 2000: **MISSING** Team Scores (as of 2025-03-18)

## Team acronyms

We attempt to determine team acronyms by doing (approximate) team scoring and
comparing to the team scores for a given tournament.

For one year (2001), there were `team.pdf`, `team-2.pdf`, etc. files found
on the Wayback Machine. (Original source needed.) The IKWF used to print
this acronym key in the state tournament booklets but these didn't really
make it onto the internet.

## Trackwrestling

For 2007-2025, brackets are on Trackwrestling. Unfortunately there is no API,
however we can capture brackets via Selenium (a webdriver). We capture 4
primary data sources:

- `brackets.selenium.json`: Championship brackets; this is purely to determine
  which athletes are top / bottom in initial rounds
- `deductions.selenium.json`: Team point deductions by going to the team score
  detail for every single team
- `rounds.selenium.json`: "Round Results" for every weight, across each
  round
- `team_scores.selenium.json`: Team scores by division

## Team scoring

As of 2025 bylaws (`bylaws_2024-25.pdf`), team scoring at the state tournament
is as follows (`22.8.3`):

- 16 points for 1st place
- 12 points for 2nd place
- 9 points for 3rd place
- 7 points for 4th place
- 5 points for 5th place
- 3 points for 6th place
- 2 points for 7th place
- 1 point for 8th place.

and advancement points (`22.8.4.1`):

- 2 advancement points will be credited to a team's total for
  each match won in the championship bracket
- 1 advancement point in the consolation bracket
- Except the first, third, fifth, and seventh place bouts

and bonus points (`22.8.4.2`, `22.8.4.3`, `22.8.4.4`):

- 2 additional points will be awarded for a win by fall, default,
  disqualification, or forfeit
- 1.5 additional points shall be awarded for each win by technical fall
- 1 additional point shall be awarded for each win by major decision

and handling byes (`22.8.4.5`):

- If a wrestler receives a bye in the preliminary round of competition, he/she
  shall be awarded 2 advancement points for that round if he/she wins his/her
  next match. Bonus points shall be duplicated as well. If one match is wrestled
  in a round, all other wrestlers in that bracket shall receive byes for that
  round. In consolation brackets, the same rule applies. In both cases, no
  points shall be awarded for the bye if the wrestler loses his/her next match
  after the bye.

## Notable changes over time

### 1993

- Split from a single age division into Novice / Senior

### 2001

- Increase from 6 to 8 medalists

### 2002

- Senior new weight classes (19): 70, 74, 79, 84, 89, 95, 101, 108, 115, 122, 130,
  138, 147, 156, 166, 177, 189, 215, 275

### 2004

- First walkover (`P-Dec`) appeared; not sure when these were allowed (as of
  2025-03-19)

### 2006

- Other walkover (`P-Dec`) appeared; not sure when these were allowed (as of
  2025-03-19)

### 2008

- Novice new weight classes (17): 62, 66, 70, 74, 79, 84, 89, 95, 101, 108, 115,
  122, 130, 138, 156, 177, 215
- Senior new weight classes (18): 74, 79, 84, 89, 95, 101, 108, 115, 122, 130,
  138, 147, 156, 166, 177, 189, 215, 275

### 2020

- Novice new weight classes (15): 60, 64, 69, 74, 80, 86, 93, 100, 108, 116,
  125, 134, 154, 178, 215
- Senior new weight classes (18): 70, 74, 79, 84, 90, 96, 103, 110, 118, 126,
  135, 144, 154, 164, 176, 188, 215, 275

### 2022

- Guaranteed full wrestlebacks for all R32 wrestlers (previously, if
  wrestler **B** beat wrestler **C** in R32, then wrestler **B** lost to the
  sectional champ wrestler **A** in R16, then wrestler **C** did not get to
  wrestle back; this was a follow-the-leader after R16 format, IHSA did
  something similiar with follow-the-leader after R8)

### 2023

- Senior new weight classes (17): 74, 79, 84, 90, 96, 103, 110, 118, 126, 135,
  144, 154, 164, 176, 188, 215, 275

### 2024

- First ever Bantam and Intermediate state championship
- First time girls are included in state tournament(s)
- Bantam new weight classes (13): 43, 46, 49, 52, 55, 58, 62, 66, 70, 76, 84,
  95, 120
- Intermediate new weight classes (13): 55, 59, 64, 69, 74, 79, 84, 90, 98, 108,
  122, 148, 177
- Girls Bantam new weight classes (8): 43, 46, 50, 55, 62, 68, 74, 85
- Girls Intermediate new weight classes (9): 53, 57, 62, 67, 73, 80, 90, 113,
  135
- Girls Novice new weight classes (12): 59, 64, 69, 75, 81, 87, 94, 102, 112,
  126, 140, 180
- Girls Senior new weight classes (13): 71, 84, 90, 93, 97, 102, 108, 115, 121,
  127, 143, 183, 240

### 2025

- Girls Bantam new weight classes (9): 45, 50, 55, 61, 67, 74, 85, 95, 115
- Girls Intermediate new weight classes (11): 53, 57, 62, 67, 72, 77, 82, 88,
  95, 115, 135
- Girls Novice new weight classes (13): 63, 68, 74, 80, 85, 90, 96, 102, 108,
  115, 125, 140, 185
- Girls Senior new weight classes (16): 75, 80, 85, 90, 95, 100, 105, 110, 115,
  120, 125, 130, 135, 145, 185, 240

## IWF

There was a "schism" in Illinois kids wrestling in the late 90s and early
00s. From `iwfusaw.org` results in the Wayback Machine, it appears that there
were four tournaments held by the IWF:

- 1998
- 1999
- 2000
- 2001

By 2002-06-03, the website was redirecting to
`http://www.shopfaq.com/Sports/wwspwr.html`, so likely the organization
ceased to exist. This is corroborated by a banner on the IKWF website just
at the start of the 2001-2002 season:

> On October 30, 2001 Judge Jacobius entered his Memorandum Opinion and Order
> in the case Illinois Kids Wrestling Federation vs. Ronald Reichert, Illinois
> Wrestling Federation, et al., Case No. 97 CH 6241. In the Memorandum Opinion
> and Order, Judge Jacobius entered a judgment in favor of the Illinois Kids
> Wrestling Federation ("IKWF") and against Ronald Reichert ("Reichert") and
> the Illinois Wrestling Federation ("Federation") in the amount of $103,000,
> as compensatory damages, and $50,000 as punitive damages. Judge Jacobius
> denied all Counterclaims of the Federation and Reichert. As such, Judge
> Jacobius ruled completely in favor of the IKWF on all counts, and completely
> against Reichert and the Federation on all counts. As the IKWF claimed, Judge
> Jacobius found after the lengthy trial, that Reichert and the Federation had
> acted dishonestly as part of a scheme to injure the IKWF. The Memorandum
> Opinion and Order will be posted in full on the IKWF's website in the next
> few days. In the meantime, if you require any information, please contact
> Mike Urwin at (708) 478-4593.
