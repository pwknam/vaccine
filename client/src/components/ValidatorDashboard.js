import "../App.css";
import { useNavigate } from "react-router-dom";
import VaccineRowIssuer from "./VaccineRowIssuer";
import React, { useEffect, useState } from "react";
import VaccineCard from "../images/VaccineCard.svg";

function ValidatorDashboard({ dl, user }) {
  const navigate = useNavigate();
  const [patientData, setPatientData] = useState({});
  const [vaccinations, setVaccinations] = useState([]);
  function handleSearchPage() {
    navigate({ pathname: "/searchPage" });
  }

  useEffect(() => {
    fetch(`/patients/${dl}`)
      .then((r) => {
        if (!r.ok) {
          throw new Error("Patient not found");
        } else {
          return r.json();
        }
      })
      .then((data) => {
        setPatientData(data);
        setVaccinations(data.vaccinations);
      });
    // .catch((error) => alert(error.message));
  }, [dl, user]);

  const renderVaccines = vaccinations
    ? vaccinations.map((vaccination) => {
        return (
          <VaccineRowIssuer
            key={vaccination.expiration_date}
            vaccineData={vaccination}
          />
        );
      })
    : null;

  return (
    <div className="institutionDashboardPage">
      <div className="topBar">
        <h1>{patientData.name}</h1>
        <img src={VaccineCard} alt="vaccineCard" className="image99" />
        <button
          onClick={handleSearchPage}
          className="button-47"
          style={{ marginBottom: "20px" }}
        >
          Back to Search
        </button>
      </div>
      <div className="tableContainer">
        <table className="table">
          <tbody>
            <tr>
              <th className="tableHeader">
                <h3>Vaccine Name</h3>
              </th>
              <th className="tableHeader">
                <h3>Name of Issuer</h3>
              </th>
              <th className="tableHeader">
                <h3>Valid Through</h3>
              </th>
            </tr>
            {renderVaccines}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default ValidatorDashboard;
