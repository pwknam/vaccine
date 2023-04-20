import "../App.css";
import React, { useState } from "react";
import { Routes, Route, useNavigate } from "react-router-dom";

import LandingPage from "./LandingPage";
import InstitutionLandingPage from "./InstitutionLandingPage";
import CreateAccount from "./CreateAccount";
import Login from "./Login";
import InstitutionDashboard from "./InstitutionDashboard";
import NewPatientForm from "./NewPatientForm";
import PatientDashboard from "./PatientDashboard";
import SearchPage from "./SearchPage";
import ValidatorDashboard from "./ValidatorDashboard";
import PatientLandingPage from "./PatientLandingPage";
import ActivateAccount from "./ActivateAccount";
import PatientVaccineSummary from "./PatientVaccineSummary";
import { useEffect } from "react";

function App() {
  const [user, setUser] = useState({});
  const [patientDL, setPatientDL] = useState({});
  const [patient, setPatient] = useState({});
  const [patients, setPatients] = useState([]);
  const [validatorDL, setValidatorDL] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    fetch('/check_session')
    .then(r => {
      if (r.ok) {
        r.json().then(data => data.patients ? setNewUser(data) : setUser(data))
      } else {
        navigate('/')
      }
    })
  }, [])

  function setNewUser(user) {
    setUser(user);
    setPatients(user.patients);
  }

  function setNewPatient(patient) {
    setPatients([...patients, patient]);
  }

  function goHome() {
    navigate({ pathname: "/" });
  }

  function setSearch(val) {
    setValidatorDL(val);
  }
  return (
    <div className="mainPage">
      <button onClick={goHome}>Go Home</button>
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
        <Route path="/patientLandingPage" element={<PatientLandingPage />} />
        <Route path="/activateAccount" element={<ActivateAccount setUser={setUser}/>} />
        <Route
          path="/patientVaccineSummary"
          element={<PatientVaccineSummary user={user}/>}
        />
        <Route
          path="/searchPage"
          element={<SearchPage setSearch={setSearch} dl={validatorDL} />}
        />
        <Route
          path="/validatorDashboard"
          element={<ValidatorDashboard dl={validatorDL} user={user} />}
        />
      </Routes>
    </div>
  );
}

export default App;
