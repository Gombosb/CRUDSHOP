let termekek = [
    {
      id: 1,
      nev: "Bögre",
      leiras: "UNCS mintás bögre",
      kep: "img/Bogre.png"
    },
    {
      id: 2,
      nev: "Egérpad",
      leiras: "UNCS mintás egérpad",
      kep: "img/Egerpad.png"
    },
    {
      id: 3,
      nev: "Matrica",
      leiras: "UNCS mintás matrica",
      kep: "img/Matrica.png"
    },
    {
      id: 4,
      nev: "Póló",
      leiras: "UNCS mintás póló",
      kep: "img/Polo1.png"
    },
    {
      id: 5,
      nev: "Sapka",
      leiras: "UNCS mintás sapka",
      kep: "img/Sapka.png"
    }
];

if (!localStorage.getItem("termekek")) {
    localStorage.setItem("termekek", JSON.stringify(termekek));
}

function termekekMegjelenitese() {
    const lista = document.getElementById("termekLista");
    lista.innerHTML = "";
  
    const taroltTermekek = JSON.parse(localStorage.getItem("termekek"));
  
    taroltTermekek.forEach(termek => {
      lista.innerHTML += `
        <div class="col-md-4">
          <div class="card h-100">
            <img src="${termek.kep}" class="card-img-top" alt="${termek.nev}">
            <div class="card-body">
              <h4 class="card-title">${termek.nev}</h4>
              <p class="card-text">${termek.leiras}</p>
              <button class="btn btn-danger btn-sm" onclick="torles(${termek.id})">
                Törlés
              </button>
              <button class="btn btn-warning btn-sm ms-2" onclick="modositas(${termek.id})">
                Módosítás
              </button>
            </div>
          </div>
        </div>
      `;
    });
}
  
function torles(id) {
    let termekek = JSON.parse(localStorage.getItem("termekek"));
    termekek = termekek.filter(t => t.id !== id);
    localStorage.setItem("termekek", JSON.stringify(termekek));
    termekekMegjelenitese();
}
  
function modositas(id) {
    let termekek = JSON.parse(localStorage.getItem("termekek"));
    let termek = termekek.find(t => t.id === id);
  
    let ujNev = prompt("Új terméknév:", termek.nev);
    let ujLeiras = prompt("Új leírás:", termek.leiras);
  
    if (ujNev && ujLeiras) {
      termek.nev = ujNev;
      termek.leiras = ujLeiras;
      localStorage.setItem("termekek", JSON.stringify(termekek));
      termekekMegjelenitese();
    }
}
  
function ujTermek() {
    let termekek = JSON.parse(localStorage.getItem("termekek"));
  
    let uj = {
      id: Date.now(),
      nev: "Új termék",
      leiras: "Új leírás",
      kep: "img/Bogre.png"
    };
  
    termekek.push(uj);
    localStorage.setItem("termekek", JSON.stringify(termekek));
    termekekMegjelenitese();
}

termekekMegjelenitese();
  