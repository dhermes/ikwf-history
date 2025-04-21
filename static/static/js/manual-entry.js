// Copyright (c) 2025 - Present. IKWF History. All rights reserved.

const wrestlerChoices = [
  { id: 1, name: "Dexton Pontnack", team: "Dakota WC" },
  { id: 2, name: "Hamza Shakeel", team: "Fit & Fight Gym WC" },
  { id: 3, name: "Joey Boggs", team: "Fighting Farmers WC" },
  { id: 4, name: "Kayden Sicka", team: "Southern Illinois Bulldogs WC" },
  { id: 5, name: "Emmett Richardson", team: "Pontiac WC" },
  { id: 6, name: "Michael Sims", team: "Wilmington WC" },
  { id: 7, name: "Jack Hermes", team: "Fox Valley WC" },
  { id: 8, name: "Darek Lee III", team: "Brawlers WC" },
  { id: 9, name: "Levi Schroeder", team: "Maine Eagles WC" },
  { id: 10, name: "Jerome Turner Jr", team: "Springs Elite WC" },
  { id: 11, name: "Eris Bybee", team: "DC WC" },
  { id: 12, name: "Bowyn Schulz", team: "El Paso Gridley Youth WC" },
  { id: 13, name: "William Kochel", team: "Lincoln-Way WC" },
  { id: 14, name: "Bobby O'Keefe", team: "Dinamo Wrestling" },
  { id: 15, name: "Aedan Perez", team: "Glenbard East Jr Rams WC" },
  { id: 16, name: "Kingston Hamilton", team: "Wildcats Wrestling Academy" },
  { id: 17, name: "Roman Oliver", team: "Olney Cubs WC" },
  { id: 18, name: "Donavan Shelby", team: "Stillman Valley WC" },
  { id: 19, name: "Hunter Voss", team: "DC WC" },
  { id: 20, name: "Max Corbell", team: "Fox Valley WC" },
  { id: 21, name: "William McConnell", team: "Team Mascoutah WC" },
  { id: 22, name: "Alexander Cid", team: "Toss Em Up Wrestling Academy" },
  { id: 23, name: "Declan Druger", team: "Dundee Highlanders WC" },
  { id: 24, name: "Ezra Lindsey", team: "Harvey Twisters WC" },
];

document.querySelectorAll(".participant-select").forEach((select) => {
  for (const option of select.options) {
    if (option.value === "") {
      continue;
    }

    const index = Number(option.value) - 1;
    const wrestler = wrestlerChoices[index];
    option.textContent = wrestler.name;
  }
});
