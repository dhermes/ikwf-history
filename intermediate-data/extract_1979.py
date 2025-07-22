# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
Produce `extracted.1979.json` brackets.

The full names / teams / weights were provided in the 1979 program:

| Team                      | Name               | Weight |
| ------------------------- | ------------------ | ------ |
| Alton W.C.                | Kip Kristoff       | 75     |
|                           | Charlie Sherertz   | 100    |
|                           | Jeff Nichols       | 125    |
| Antioch Upper Grade       | Jeff Hieze         | 80     |
|                           | Tad DeRousse       | 90     |
|                           | Steve Case         | 95     |
|                           | Tim Curtis         | 100    |
|                           | John Oelkees       | 105    |
|                           | Andy Lehn          | 125    |
|                           | George Bessette    | 135    |
|                           | Pibor Jung         | 145    |
|                           | Bill Carney        | 155    |
| Apollo Jr. High           | Dave Sherran       | 90     |
|                           | Angelo Campanella  | 125    |
| Belleville                | Ed Cantrell        | 60     |
|                           | John Churchill     | 60     |
|                           | Tim Allgire        | 65     |
|                           | Bob Calhoun        | 70     |
|                           | Mike Neiner        | 80     |
| Belvidere                 | Dave Doulghenbauch | 75     |
|                           | Kerry Flynn        | 90     |
|                           | Jody Flynn         | 95     |
|                           | Dave Loos          | 125    |
| Big Hollow W.C.           | Rich Ilmberger     | 170    |
| Bismarck                  | Mike Hoover        | 70     |
|                           | Dan Smalley        | 100    |
| Bloomington Jr. High      | Brad Johnson       | 70     |
|                           | Carlos Ortiz       | 111    |
|                           | Randy Evans        | 118    |
|                           | Charles Robb       | 125    |
|                           | Gill Crutcher      | 275    |
| Indian Trail / Addison    | Rodriguez          | 111    |
|                           | Lullo              | 118    |
| Indian Trail / Plainfield | John Walter        | 60     |
|                           | Ed Moholick        | 65     |
|                           | Mike Witkowski     | 65     |
|                           | Chuck McCann       | 75     |
|                           | Dave Dupree        | 75     |
|                           | Nick Quas          | 85     |
|                           | John Rajich        | 95     |
|                           | Darren Herbst      | 111    |
|                           | Rich Henderson     | 118    |
|                           | Guy Pennington     | 155    |
|                           | Eric Greenup       | 185    |
| Jack London               | Jeff Brannan       | 60     |
|                           | Steve Petersen     | 85     |
|                           | Mark Nowak         | 111    |
|                           | Mike Wilson        | 185    |
|                           | Marcelino Garcia   | 275    |
| Jane Adams                | Mike Oshiro        | 111    |
|                           | Jeff Goodwin       | 135    |
|                           | Lou Rinaldi        | 185    |
| Joliet YMCA               | Tim Meagher        | 70     |
|                           | Chris Scott        | 80     |
|                           | Vincent Criscione  | 90     |
|                           | Sean Mann          | 95     |
|                           | Todd Conroy        | 100    |
|                           | Keith Rumchuck     | 118    |
| Jordon Jr. High           | Mike Patting       | 95     |
|                           | John Doak          | 111    |
|                           | John Wetderell     | 118    |
| King Upper Grade          | Rodger Mayer       | 118    |
| Lake Villa                | Carl Hildinger     | 85     |
|                           | Todd Jenkins       | 90     |
|                           | Bob Ratajczyk      | 118    |
| Blue Island W.C.          | Kevin Goudeau      | 275    |
| Bower                     | Randy Crow         | 170    |
| Calumet Pk. Dist.         | Mark Antonietti    | 170    |
| Carbondale                | Eric Walker        | 65     |
|                           | Scott Grammer      | 90     |
|                           | Matt Lemming       | 100    |
|                           | Tim Brown          | 111    |
|                           | Adam Phavorachit   | 118    |
| Champaign W.C.            | Eric Mueller       | 75     |
|                           | Dennis Stabl       | 185    |
|                           | Dana Anastasia     | 135    |
| Chicago Ridge             | Dan Evensen        | 60     |
|                           | Mike O'Brien       | 65     |
|                           | Greg Flores        | 90     |
|                           | Pat Nolan          | 95     |
|                           | Tony Evenson       | 105    |
|                           | Tim Cocco          | 125    |
| Bobcats                   | Nino Chiapetta     | 60     |
|                           | Joe Chiapetta      | 75     |
|                           | Gennevali          | 170    |
| Coal City                 | Dan Residori       | 95     |
|                           | Mike Friddle       | 105    |
| Cooper                    | Tony Rivoppo       | 100    |
|                           | Bob Bruno          | 185    |
| Decatur                   | Jeff Scott         | 60     |
|                           | Walter Scott       | 65     |
|                           | Scoh Mitchell      | 85     |
|                           | Tom Velek          | 118    |
| Lake Zurich W.C.          | Kollin Stagnito    | 65     |
|                           | Jeff Pahlos        | 70     |
|                           | Dave Berg          | 75     |
|                           | Korry Stagnito     | 95     |
|                           | Mike Meinhart      | 275    |
| Lil Reaper W.C.           | Dan Goldsmith      | 170    |
|                           | Rich Spears        | 185    |
|                           | Dave Browning      | 275    |
| Lincoln Jr. High          | Joe Landis         | 90     |
|                           | Daron Smith        | 145    |
| Lincoln Cicero            | Spacone            | 65     |
|                           | Dorich             | 70     |
|                           | Flanagan           | 80     |
| Lisle                     | Winze              | 275    |
| Lockport Wrestlers        | Mitchell           | 185    |
| Lombard Jr. Rams          | Zezuiak            | 185    |
| Lundahl Jr. High          | Steve Schrey       | 111    |
|                           | Chuck Sherman      | 155    |
|                           | Joe Fortin         | 170    |
| Mahomet Seymour           | Robbie Porter      | 65     |
|                           | Greg Durst         | 75     |
|                           | Gary Campbell      | 80     |
|                           | Steve Zehr         | 85     |
| Mat Burns                 | Terry Higgins      | 80     |
|                           | Fernado Malablhar  | 111    |
|                           | Tony Cortese       | 118    |
|                           | Mike Burke         | 118    |
|                           | Eric Koeller       | 170    |
|                           | Lou Rodriguez      | 275    |
| Deerpath                  | Todd Stanton       | 80     |
| Dolton                    | Jim Throw          | 60     |
|                           | John Bulf          | 95     |
|                           | Bill Anderson      | 155    |
| Dundee Highlanders        | Roger Shelton      | 75     |
|                           | Dave Alborn        | 135    |
| East Moline               | Bam Bam Pustelnik  | 60     |
|                           | Chris Tiemeier     | 70     |
|                           | Shawn Harris       | 135    |
|                           | Dale Johnson       | 185    |
| Edwardsville              | Steve Schmidt      | 90     |
|                           | Greg Mihalich      | 125    |
|                           | Eric Brown         | 135    |
|                           | Tracy Bradford     | 170    |
|                           | Eric Wildgrube     | 185    |
| Eisenhower                | Johnson            | 65     |
|                           | Denning            | 80     |
|                           | Knez               | 100    |
|                           | Kallas             | 135    |
|                           | Little             | 145    |
|                           | Miller             | 155    |
| Franklin Pk Raiders       | Kevin Powers       | 70     |
|                           | Peter Tarzygnat    | 80     |
|                           | Scott Fitzgibbons  | 95     |
|                           | Dave Vohaska       | 155    |
| Glenview                  | Mike Redden        | 135    |
| Glenwood                  | Lance Pero         | 65     |
|                           | Jeff Adams         | 170    |
| Mattoon W.C.              | Terry Thomason     | 105    |
|                           | Greg Winchester    | 111    |
| McDonough County YMCA     | Troy Protsman      | 65     |
| Mokena                    | Dwane Maue         | 70     |
|                           | Bryant Capodice    | 100    |
|                           | Rick Pedigo        | 111    |
| Mount Greenwood           | Bob Clancy         | 155    |
|                           | Mike Eperjesi      | 275    |
| Naperville                | Phil Gray          | 60     |
|                           | Reid Diehl         | 80     |
|                           | Ralf Diehl         | 85     |
|                           | Bob Davies         | 125    |
|                           | Connor McCarthy    | 145    |
|                           | Larry Parece       | 155    |
| Normal                    | Jammie Abbott      | 170    |
| Oak Forest                | Craig DeBevec      | 70     |
|                           | Mike Muilli        | 80     |
|                           | Brian Porter       | 105    |
|                           | Kevin Jarchow      | 118    |
|                           | Dale Schmidt       | 145    |
| Oak Park                  | Rich Ryser         | 75     |
|                           | Jeff Sorensen      | 155    |
|                           | James Holman       | 170    |
|                           | Craig Drummond     | 185    |
|                           | John Phelan        | 275    |
| Orland Park               | Mike LaMonica      | 60     |
|                           | Mike Urwin         | 60     |
|                           | Mark Olsen         | 90     |
|                           | Tom Hoch           | 105    |
| Gompers Jr. High          | Reed               | 135    |
|                           | Sefcik             | 185    |
| Gower                     | Pat Kohl           | 90     |
|                           | Kevin Craggs       | 100    |
| Grigsby                   | Mike Bellipanni    | 85     |
|                           | Kent Patterson     | 105    |
|                           | Bob Unger          | 111    |
|                           | Mike Kessler       | 135    |
|                           | Frank Edwards      | 145    |
|                           | John Morris        | 170    |
| Harvard W.C.              | Dan Muehl          | 65     |
|                           | Tim Linhart        | 145    |
| Hickory Hills             | Joe Zaccone        | 85     |
|                           | Bill Collins       | 105    |
|                           | Steve Myers        | 111    |
|                           | Mike Flannery      | 125    |
|                           | Tim Johnson        | 145    |
|                           | Scott Scelfo       | 170    |
| Holmes Jr. High           | Alegoz Satlimis    | 135    |
|                           | Derek Grandt       | 145    |
| Hoopeston E. Lynn         | Doug Dennison      | 95     |
|                           | Darrin Pierce      | 100    |
| Hufford                   | Craig Sterr        | 70     |
|                           | Jim Henderson      | 100    |
| Huntley Middle School     | Brad Larson        | 80     |
|                           | Jeff Meier         | 85     |
|                           | Bill Herrmann      | 90     |
|                           | Paul Hemmett       | 105    |
|                           | Ken Taylor         | 275    |
| Huth Jr. High             | Dean Rodgers       | 118    |
|                           | Mike Webster       | 275    |
| Palatine P.D.             | Jim Rosman         | 118    |
| Palos South               | Joe White          | 75     |
|                           | Dave Elkin         | 80     |
|                           | Scott Barczi       | 111    |
|                           | John Connel        | 135    |
| Panther W.C.              | Mark Becker        | 60     |
|                           | Joe Bochenski      | 70     |
|                           | Jon Popp           | 75     |
|                           | Ken Sroka          | 85     |
|                           | Jim Schultz        | 90     |
|                           | Keith Healy        | 90     |
|                           | Jerry Blaney       | 95     |
|                           | Jim Popp           | 111    |
|                           | Gary Enquita       | 135    |
| Park Ridge                | Bill Lamanna       | 60     |
|                           | John Loos          | 65     |
|                           | Ralph Milito       | 85     |
| Pekin B.C.                | Chuck Reed         | 60     |
|                           | Todd Spraggs       | 105    |
|                           | Kip Flairty        | 155    |
| Peter Claver              | Fredrick Ferguson  | 75     |
| Pontiac                   | Joe Lind           | 70     |
|                           | Richard Weaver     | 275    |
| Prather                   | Collin Davis       | 70     |
|                           | Bruce Widel        | 95     |
|                           | Mark Gowdy         | 105    |
|                           | John Frangovils    | 118    |
|                           | Bill Zimmer        | 155    |
|                           | Eric Gunderson     | 185    |
|                           | Bob Allen          | 275    |
| Quincy                    | Randy Womack       | 85     |
| Rantoul                   | Jim Scherbering    | 185    |
| Rich Township             | Dean Souder        | 65     |
|                           | Scott Zayner       | 80     |
|                           | Mike Terrell       | 85     |
|                           | Todd Kunz          | 95     |
|                           | John Terrell       | 125    |
|                           | James Cotton       | 135    |
|                           | Charles VanGamert  | 145    |
|                           | Ed Lusting         | 275    |
| Riverdale                 | Shawn Wildermuth   | 145    |
| River Trails              | Robert Watters     | 100    |
|                           | Ronald Renaud      | 185    |
| Rock Falls                | Darren Brown       | 60     |
|                           | Danny Bushaw       | 155    |
|                           | Gilbert Almanza    | 155    |
| Rosemont Cobras           | Mike Chicoski      | 60     |
|                           | Kirk Jurinek       | 65     |
|                           | Phillip Chihoski   | 70     |
|                           | Marvin Robackowski | 75     |
|                           | Tom Klescyk        | 100    |
| Rosette Middle School     | Scott Sisler       | 80     |
|                           | Tim Weeks          | 85     |
|                           | Don Butler         | 100    |
|                           | Joe Hoiness        | 125    |
|                           | Scott Herbert      | 145    |
| Roxana Jr. High           | Rob Millazzo       | 75     |
|                           | Chris Paynic       | 80     |
|                           | Rob Mauser         | 95     |
| Shady Lane W.C.           | Scott Sutton       | 60     |
|                           | Jeff Jensen        | 70     |
|                           | John Corrigan      | 105    |
|                           | Mike Rowden        | 125    |
| Springfield S.E.          | Kane Robertson     | 125    |
|                           | Jerry Ware         | 170    |
| Springfield W.C.          | John Suter         | 80     |
|                           | Dick McCormick     | 135    |
|                           | John Rodlands      | 145    |
| St. Barnabas              | Tom Carroll        | 70     |
|                           | Hal Olofsson       | 85     |
|                           | Mah Fassan         | 100    |
|                           | Ed Cineda          | 145    |
| St. Phillips              | Laparker Evereh    | 75     |
|                           | Rod Martin         | 170    |
| St. Tarcissus             | John Egan          | 125    |
| Summit Hill               | Don Miller         | 155    |
| Sycamore                  | Steve Glawe        | 75     |
|                           | Bill Schepler      | 100    |
|                           | Jerry Dobson       | 111    |
|                           | Ric Petruchius     | 118    |
|                           | Paul Klink         | 170    |
| Tinley Park               | Mike Pfingston     | 65     |
|                           | Ted Howlett        | 85     |
|                           | Dave Arndt         | 90     |
|                           | Dion Stewart       | 125    |
| Trimpe                    | Dave Miller        | 155    |
| Troy                      | Phil Daniels       | 80     |
|                           | Jamie Litchfield   | 90     |
|                           | Rene Robles        | 105    |
|                           | Bob Atkinson       | 118    |
|                           | Frank Ostir        | 135    |
|                           | Jim Taylor         | 170    |
| Urbana                    | Mike Arnold        | 90     |
|                           | Mark Mannen        | 95     |
| Vittum Vikings            | Schilling          | 100    |
| Ward Middle School        | Ken Johnson        | 145    |
|                           | Ray Tyree          | 275    |
| Washington Jr. High       | Navel Woods        | 75     |
|                           | Houston            | 155    |
| West Chicago              | Carlson            | 95     |
|                           | Cothron            | 105    |
|                           | Hernandez          | 125    |
|                           | Jaskowke           | 155    |
|                           | Shemshedini        | 170    |
|                           | King               | 185    |
| West Leyden               | Mike Hruska        | 85     |
|                           | Bob Gonnella       | 90     |
|                           | Danny Marcinac     | 95     |
|                           | Wayne Bohenek      | 105    |
|                           | Dave Paske         | 105    |
|                           | Bob Guerrieri      | 111    |
| Westview Hills            | Martin             | 145    |
|                           | Schrock            | 275    |
| Wheaton Pk Dist.          | Pierre             | 85     |
| Dixon W.C.                | Joe Williams       | 70     |
| Stephens Middle School    | Chris Greham       | 125    |
| Murphysboro               | Chett McAdams      | 145    |
"""

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Phil Gray", team="Naperville"),
    65: bracket_utils.Placer(name="Mike O'Brien", team="Chicago Ridge"),
    70: bracket_utils.Placer(name="Tim Meagher", team="Joliet YMCA"),
    75: bracket_utils.Placer(name="Rob Milazzo", team="Roxana"),
    80: bracket_utils.Placer(name="Chris Scott", team="Joliet YMCA"),
    85: bracket_utils.Placer(name="Nick Quaz", team="Plainfield"),
    90: bracket_utils.Placer(name="Keith Healy", team="Burbank"),
    95: bracket_utils.Placer(name="Jerry Blaney", team="Burbank"),
    100: bracket_utils.Placer(name="Brian Capodice", team="Mokena"),
    105: bracket_utils.Placer(name="Tony Evensen", team="Chicago Ridge"),
    111: bracket_utils.Placer(name="Bob Guirriero", team="West Leyden"),
    118: bracket_utils.Placer(name="Rich Henderson", team="Plainfield Indian Tr"),
    125: bracket_utils.Placer(name="Tim Cocco", team="Chicago Ridge"),
    135: bracket_utils.Placer(name="George Bessette", team="Antioch"),
    145: bracket_utils.Placer(name="Dale Schmidt", team="Oak Forest Warriors"),
    155: bracket_utils.Placer(name="Dave Vohaska", team="Franklin Park"),
    170: bracket_utils.Placer(name="Rod Martin", team="St. Philip Neri"),
    185: bracket_utils.Placer(name="Dennis Stabl", team="Champaign"),
    275: bracket_utils.Placer(name="Ray Tyree", team="Bolingbrook Ward"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "PLAINFIELD": 146.0,
    "JOLIET YMCA": 119.0,
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1979.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
