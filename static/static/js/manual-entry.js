// Copyright (c) 2025 - Present. IKWF History. All rights reserved.

const WRESTLER_CHOICES = [
  { name: "Wrestler 1", team: "Team 1" },
  { name: "Wrestler 2", team: "Team 2" },
  { name: "Wrestler 3", team: "Team 3" },
  { name: "Wrestler 4", team: "Team 4" },
  { name: "Wrestler 5", team: "Team 5" },
  { name: "Wrestler 6", team: "Team 6" },
  { name: "Wrestler 7", team: "Team 7" },
  { name: "Wrestler 8", team: "Team 8" },
  { name: "Wrestler 9", team: "Team 9" },
  { name: "Wrestler 10", team: "Team 10" },
  { name: "Wrestler 11", team: "Team 11" },
  { name: "Wrestler 12", team: "Team 12" },
  { name: "Wrestler 13", team: "Team 13" },
  { name: "Wrestler 14", team: "Team 14" },
  { name: "Wrestler 15", team: "Team 15" },
  { name: "Wrestler 16", team: "Team 16" },
  { name: "Wrestler 17", team: "Team 17" },
  { name: "Wrestler 18", team: "Team 18" },
  { name: "Wrestler 19", team: "Team 19" },
  { name: "Wrestler 20", team: "Team 20" },
  { name: "Wrestler 21", team: "Team 21" },
  { name: "Wrestler 22", team: "Team 22" },
  { name: "Wrestler 23", team: "Team 23" },
  { name: "Wrestler 24", team: "Team 24" },
];

function validateIndex(index) {
  if (!Number.isInteger(index) || index < 0 || index > 23) {
    throw new Error(`Invalid index: ${index}`);
  }
}

function updateWrestlerChoices(wrestlerChoices) {
  document.querySelectorAll("tr.input-row").forEach((row) => {
    const participantID = Number(row.dataset.participantId);
    validateIndex(participantID);

    const name =
      row.querySelector(".input-name")?.value || `Wrestler ${participantID}`;
    const team =
      row.querySelector(".input-team")?.value || `Team ${participantID}`;

    wrestlerChoices[participantID] = { name, team };
  });

  return wrestlerChoices;
}

function updateDropdowns(wrestlerChoices) {
  document.querySelectorAll(".participant-select").forEach((select) => {
    for (const option of select.options) {
      if (option.value === "") {
        continue;
      }

      const index = Number(option.value) - 1;
      const wrestler = wrestlerChoices[index];
      if (wrestler === null) {
        option.textContent = "<unset>";
      } else {
        option.textContent = wrestler.name;
      }
    }
  });
}

function updateReadOnlyFields(wrestlerChoices) {
  const participants = document.querySelectorAll(
    "div.participant[data-participant-id]"
  );

  participants.forEach((div) => {
    const participantID = Number(div.dataset.participantId);
    validateIndex(participantID);

    const nameDiv = div.querySelector("div.name");
    if (!nameDiv) {
      return;
    }

    const wrestler = wrestlerChoices[participantID];
    nameDiv.textContent = ""; // Clear existing

    const nameText = document.createTextNode(wrestler.name);

    const teamSpan = document.createElement("span");
    teamSpan.textContent = ` (${wrestler.team})`;

    nameDiv.appendChild(nameText);
    nameDiv.appendChild(teamSpan);
  });
}

updateWrestlerChoices(WRESTLER_CHOICES);
updateDropdowns(WRESTLER_CHOICES);
updateReadOnlyFields(WRESTLER_CHOICES);
