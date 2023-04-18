import "../App.css";
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
  return (
    <div className="mainPage">
      <Routes>
        <Route exact path="/" element={<LandingPage />} />

        <Route
          path="/institutionLandingPage"
          element={<InstitutionLandingPage />}
        />
        <Route path="/institutionCreateAccount" element={<CreateAccount />} />
        <Route path="/institutionLogin" element={<Login />} />
        <Route
          path="/institutionDashboard"
          element={<InstitutionDashboard />}
        />
        <Route path="/newPatientForm" element={<NewPatientForm />} />
        <Route path="/patientDashboard" element={<PatientDashboard />} />
        <Route path="/searchPage" element={<SearchPage />} />
        <Route path="/validatorDashboard" element={<ValidatorDashboard />} />
      </Routes>
    </div>
  );
}

export default App;
