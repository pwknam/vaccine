import "../App.css";
import { Routes, Route } from "react-router-dom";

import LandingPage from "./LandingPage";
import InstitutionLandingPage from "./InstitutionLandingPage";
import CreateAccount from "./CreateAccount";

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
      </Routes>
    </div>
  );
}

export default App;
