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
const PREVIOUS_MATCH_MAP = Object.freeze({
  17: { bottom: "2" },
  18: { bottom: "4" },
  19: { bottom: "6" },
  20: { bottom: "8" },
  21: { bottom: "10" },
  22: { bottom: "12" },
  23: { bottom: "14" },
  24: { bottom: "16" },
});

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

      const index = Number(option.value);
      validateIndex(index);
      const wrestler = wrestlerChoices[index];
      option.textContent = wrestler.name;
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
    nameDiv.textContent = "";

    const nameText = document.createTextNode(wrestler.name);

    const teamSpan = document.createElement("span");
    teamSpan.textContent = ` (${wrestler.team})`;

    nameDiv.appendChild(nameText);
    nameDiv.appendChild(teamSpan);
  });
}

function handleInputChange(wrestlerChoices) {
  updateWrestlerChoices(wrestlerChoices);
  updateDropdowns(wrestlerChoices);
  updateReadOnlyFields(wrestlerChoices);
}

function handleSelectChange(wrestlerChoices, event) {
  const select = event.target;
  const winnerID = select.value;

  const matchID = select.dataset.matchId;
  const position = select.dataset.position;

  const previousMatchID = PREVIOUS_MATCH_MAP[matchID]?.[position];
  if (previousMatchID === undefined) {
    throw new Error(
      `Could not determine previous match: ${matchID}, ${position}`
    );
  }

  const previousMatchDiv = document.querySelector(
    `div.match[data-match-id="${previousMatchID}"]`
  );

  const previousParticipants = previousMatchDiv.querySelectorAll(
    "div.participant[data-participant-id]"
  );

  if (previousParticipants.length !== 2) {
    throw new Error("Not (yet) implemented");
  }

  const topParticipant = previousParticipants[0];
  const bottomParticipant = previousParticipants[1];
  if (winnerID === "") {
    topParticipant.classList.remove("win");
    topParticipant.classList.remove("loss");
    topParticipant.querySelector("div.result").textContent = "";

    bottomParticipant.classList.remove("loss");
    bottomParticipant.classList.remove("win");
    bottomParticipant.querySelector("div.result").textContent = "";
  } else if (topParticipant.dataset.participantId === winnerID) {
    topParticipant.classList.add("win");
    topParticipant.classList.remove("loss");
    topParticipant.querySelector("div.result").textContent = "W";

    bottomParticipant.classList.add("loss");
    bottomParticipant.classList.remove("win");
    bottomParticipant.querySelector("div.result").textContent = "L";
  } else if (bottomParticipant.dataset.participantId === winnerID) {
    topParticipant.classList.add("loss");
    topParticipant.classList.remove("win");
    topParticipant.querySelector("div.result").textContent = "L";

    bottomParticipant.classList.add("win");
    bottomParticipant.classList.remove("loss");
    bottomParticipant.querySelector("div.result").textContent = "W";
  } else {
    throw new Error("Neither top nor bottom won the match");
  }
}

function createInputEditableSpan(span) {
  const isDivision = span.classList.contains("division");
  if (isDivision) {
    const input = document.createElement("select");
    input.classList.add("inline-edit");
    ["Senior", "Novice"].forEach((optionValue) => {
      const option = document.createElement("option");
      option.value = optionValue;
      option.textContent = optionValue;
      if (optionValue === currentValue) option.selected = true;
      input.appendChild(option);
    });
    return input;
  }

  const input = document.createElement("input");
  input.type = "number";
  input.classList.add("inline-edit");
  input.value = currentValue;
  return input;
}

function handleClickEditableSpan(span) {
  span.addEventListener("click", () => {
    const currentValue = span.dataset.value;

    const input = createInputEditableSpan(span);
    span.replaceWith(input);
    input.focus();

    const finalize = () => {
      const newValue = input.value.trim();
      const span = document.createElement("span");
      span.className = span.className;
      span.classList.add("editable");
      span.dataset.value = newValue;
      span.textContent = newValue;

      input.replaceWith(span);
      span.addEventListener("click", span.onclick); // re-attach
    };

    input.addEventListener("blur", finalize);
    input.addEventListener("keydown", (event) => {
      if (event.key === "Enter") input.blur();
      if (event.key === "Escape") {
        input.value = currentValue;
        input.blur();
      }
    });
  });
}

document
  .querySelectorAll(".cell-name input, .cell-team input")
  .forEach((input) => {
    input.addEventListener("input", () => handleInputChange(WRESTLER_CHOICES));
  });

document.querySelectorAll("select").forEach((select) => {
  select.addEventListener("change", (event) =>
    handleSelectChange(WRESTLER_CHOICES, event)
  );
});

handleInputChange(WRESTLER_CHOICES);

document.querySelectorAll("span.editable").forEach(handleClickEditableSpan);
