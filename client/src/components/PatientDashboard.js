import React, { useEffect, useState } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import VaccineRowIssuer from "./VaccineRowIssuer";
import vaccineImage from "../images/CV.svg";

function PatientDashboard({ DL, user, patient }) {
  const [patientData, setPatientData] = useState({});
  const [vaccinations, setVaccinations] = useState([]);
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [date, setDate] = useState("");
  console.log(patient);

  function handleDashboardNavigate() {
    navigate({ pathname: "/institutionDashboard" });
  }

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/patients/${DL}/${user.role}`)
      .then((r) => r.json())
      .then((data) => {
        setPatientData(data);
        setVaccinations(data.vaccinations);
      });
  }, [DL, user]);

  console.log(user.id);

  const renderVaccines = vaccinations
    ? vaccinations.map((vaccination) => {
        return (
          <VaccineRowIssuer key={vaccination.name} vaccineData={vaccination} />
        );
      })
    : null;
  function handleNewVaccine(e) {
    console.log(user.issuer_id);
    e.preventDefault();
    fetch(`http://127.0.0.1:8000/vaccinations`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        expiration_date: date,
        issuer_id: user.issuer_id,
        patient_id: patient.id,
      }),
    })
      .then((r) => r.json())
      .then((data) => {
        setVaccinations([...vaccinations, data]);
      });
  }

  return (
    <div>
      <div className="topBar">
        <h1>{patientData.name}</h1>
        <button onClick={handleDashboardNavigate} className="button-47">
          Dashboard
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
      <div className="container">
        <div className="left">
          <div className="landingPageImage">
            <img
              src={vaccineImage}
              alt="Coronavirus Vaccine"
              style={{ width: 600, height: 600 }}
            />
          </div>
        </div>
        <div className="right">
          <div className="addNewContainer1">
            <h2>Add New Vaccine</h2>
            <form className="createAccountForm1" onSubmit={handleNewVaccine}>
              <div className="formDiv1">
                <label className="formLabel1">Vaccine Name</label>
                <input
                  type="text"
                  className="formInput1"
                  onChange={(e) => {
                    setName(e.target.value);
                  }}
                  value={name}
                ></input>
              </div>
              <div className="formDiv1">
                <label className="formLabel1">Expiration Date</label>
                <input
                  type="text"
                  className="formInput1"
                  onChange={(e) => setDate(e.target.value)}
                  value={date}
                ></input>
              </div>

              <button className="button-47">Add Vaccine</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PatientDashboard;
