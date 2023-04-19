import React from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import VaccineRowIssuer from "./VaccineRowIssuer";

function PatientDashboard({ DL }) {
  console.log(DL);
  const navigate = useNavigate();

  function handleDashboardNavigate() {
    navigate({ pathname: "/institutionDashboard" });
  }

  return (
    <div>
      <div className="topBar">
        <h1>Patient Name</h1>
        <button onClick={handleDashboardNavigate}>Dashboard</button>
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
            <VaccineRowIssuer />
            <VaccineRowIssuer />
            <VaccineRowIssuer />
          </tbody>
        </table>
      </div>
      <div>
        <h2>Add New Vaccine</h2>
        <form className="createAccountForm">
          <div className="formDiv">
            <label className="formLabel">Vaccine Name</label>
            <input type="text" className="formInput"></input>
          </div>
          <div className="formDiv">
            <label className="formLabel">Expiration Date</label>
            <input type="text" className="formInput"></input>
          </div>

          <button className="createAccountButton">Add Vaccine</button>
        </form>
      </div>
    </div>
  );
}

export default PatientDashboard;
