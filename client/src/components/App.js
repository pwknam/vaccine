import "../App.css";
import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";

import LandingPage from "./LandingPage";
import InstitutionLandingPage from "./InstitutionLandingPage";
import CreateAccount from "./CreateAccount";
import Login from "./Login";
import InstitutionDashboard from "./InstitutionDashboard";
import NewPatientForm from "./NewPatientForm";
import PatientDashboard from "./PatientDashboard";
import SearchPage from "./SearchPage";
import ValidatorDashboard from "./ValidatorDashboard";

function App() {
  const [user, setUser] = useState({});
  const [patientDL, setPatientDL] = useState({});
  const [patient, setPatient] = useState({});
  const [patients, setPatients] = useState([]);

  function setNewUser(user) {
    setUser(user);
    setPatients(user.patients);
  }

  function setNewPatient(patient) {
    setPatients([...patients, patient]);
  }
  return (
    <div className="mainPage">
      <Routes>
        <Route exact path="/" element={<LandingPage />} />

        <Route
          path="/institutionLandingPage"
          element={<InstitutionLandingPage />}
        />
        <Route
          path="/institutionCreateAccount"
          element={<CreateAccount setNewUser={setNewUser} />}
        />
        <Route
          path="/institutionLogin"
          element={<Login setNewUser={setNewUser} />}
        />
        <Route
          path="/institutionDashboard"
          element={
            <InstitutionDashboard
              userInfo={user}
              DL={setPatientDL}
              setPatient={setPatient}
              patients={patients}
            />
          }
        />
        <Route
          path="/newPatientForm"
          element={<NewPatientForm setNewPatient={setNewPatient} />}
        />
        <Route
          path="/patientDashboard"
          element={
            <PatientDashboard DL={patientDL} user={user} patient={patient} />
          }
        />
        <Route path="/searchPage" element={<SearchPage />} />
        <Route path="/validatorDashboard" element={<ValidatorDashboard />} />
      </Routes>
    </div>
  );
}

export default App;
