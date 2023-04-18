import "../App.css";
import { useNavigate } from "react-router-dom";
import VaccineRowIssuer from "./VaccineRowIssuer";

function ValidatorDashboard() {
  const navigate = useNavigate();
  function handleSearchPage() {
    navigate({ pathname: "/searchPage" });
  }
  return (
    <div>
      <div className="topBar">
        <h1>Patient Name</h1>
        <button onClick={handleSearchPage}>Dashboard</button>
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
    </div>
  );
}

export default ValidatorDashboard;
