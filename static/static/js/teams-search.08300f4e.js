const PAGE_SIZE = 16;

const list = document.getElementById("team-list");
const search = document.getElementById("team-search");
const count = document.getElementById("team-count");
const pagination = document.getElementById("pagination");
const noResults = document.getElementById("no-results");

const allTeams = Array.from(list.querySelectorAll("li"));

const teamData = allTeams.map((team) => ({
  element: team,
  name: team.querySelector(".team-name").textContent.trim(),
  synonyms: JSON.parse(team.dataset.synonyms || "[]")
    .map((name) => name.trim())
    .filter(Boolean),
}));

let filteredTeams = allTeams;
let currentPage = 1;

function normalize(value) {
  return value
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

function render() {
  const totalPages = Math.max(1, Math.ceil(filteredTeams.length / PAGE_SIZE));

  currentPage = Math.min(currentPage, totalPages);

  const start = (currentPage - 1) * PAGE_SIZE;
  const end = start + PAGE_SIZE;

  const visibleTeams = new Set(filteredTeams.slice(start, end));

  for (const team of allTeams) {
    team.hidden = !visibleTeams.has(team);
  }

  noResults.hidden = filteredTeams.length !== 0;

  if (filteredTeams.length === 0) {
    count.textContent = "0 teams";
  } else {
    const first = start + 1;
    const last = Math.min(end, filteredTeams.length);

    count.textContent = `${first}-${last} of ${filteredTeams.length} teams`;
  }

  renderPagination(totalPages);
}

function renderPagination(totalPages) {
  pagination.innerHTML = "";

  if (totalPages <= 1) {
    return;
  }

  addPageButton("\u2190", currentPage - 1, currentPage === 1);

  const pages = getPageNumbers(totalPages);

  for (const page of pages) {
    if (page === "...") {
      const span = document.createElement("span");
      span.className = "ellipsis";
      span.textContent = "...";
      pagination.appendChild(span);
      continue;
    }

    addPageButton(page, page, false, page === currentPage);
  }

  addPageButton("\u2192", currentPage + 1, currentPage === totalPages);
}

function addPageButton(label, page, disabled = false, active = false) {
  const button = document.createElement("button");

  button.type = "button";
  button.textContent = label;
  button.disabled = disabled;

  if (active) {
    button.classList.add("active");
    button.setAttribute("aria-current", "page");
  }

  button.addEventListener("click", () => {
    currentPage = page;

    updateUrl();
    render();

    document.querySelector(".teams-browser").scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  });

  pagination.appendChild(button);
}

function getPageNumbers(totalPages) {
  if (totalPages <= 7) {
    return Array.from({ length: totalPages }, (_, i) => i + 1);
  }

  const pages = [1];

  if (currentPage > 4) {
    pages.push("...");
  }

  const start = Math.max(2, currentPage - 1);
  const end = Math.min(totalPages - 1, currentPage + 1);

  for (let page = start; page <= end; page++) {
    pages.push(page);
  }

  if (currentPage < totalPages - 3) {
    pages.push("...");
  }

  pages.push(totalPages);

  return pages;
}

function updateUrl() {
  const params = new URLSearchParams();

  const query = search.value.trim();

  if (query) {
    params.set("q", query);
  }

  if (currentPage > 1) {
    params.set("page", currentPage);
  }

  const queryString = params.toString();

  history.replaceState(
    null,
    "",
    queryString ? `?${queryString}` : location.pathname,
  );
}

function applySearch() {
  const query = normalize(search.value.trim());

  filteredTeams = query
    ? teamData
        .filter((team) => {
          const names = [team.name, ...team.synonyms];

          return names.some((name) => normalize(name).includes(query));
        })
        .map((team) => team.element)
    : allTeams;

  currentPage = 1;

  updateUrl();
  render();
}

search.addEventListener("input", applySearch);

// "/" focuses search, unless the user is already typing somewhere.
document.addEventListener("keydown", (event) => {
  if (
    event.key === "/" &&
    document.activeElement !== search &&
    !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)
  ) {
    event.preventDefault();
    search.focus();
  }
});

// Restore state from URL.
const params = new URLSearchParams(location.search);

const initialQuery = params.get("q");

if (initialQuery) {
  search.value = initialQuery;
}

const initialPage = parseInt(params.get("page"), 10);

if (Number.isFinite(initialPage) && initialPage > 0) {
  currentPage = initialPage;
}

// Initial filtering/render.
applySearch();
