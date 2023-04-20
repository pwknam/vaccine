import "../App.css";
import { useNavigate } from "react-router-dom";
import VaccineRowIssuer from "./VaccineRowIssuer";
import React, { useEffect, useState } from "react";

function ValidatorDashboard({ dl, user }) {
  const navigate = useNavigate();
  const [patientData, setPatientData] = useState({});
  const [vaccinations, setVaccinations] = useState([]);
  function handleSearchPage() {
    navigate({ pathname: "/searchPage" });
  }

  useEffect(() => {
    console.log(dl, user.role);
    fetch(`http://127.0.0.1:8000/patients/${dl}/${user.role}`)
      .then((r) => r.json())
      .then((data) => {
        console.log(data);
        setPatientData(data);
        setVaccinations(data.vaccinations);
      });
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
    <div>
      <div className="topBar">
        <h1>{patientData.name}</h1>
        <button onClick={handleSearchPage} className="button-47">
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
