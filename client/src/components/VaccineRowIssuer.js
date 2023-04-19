import React from "react";
import "../App.css";

function VaccineRowIssuer({ vaccineData }) {
  console.log(vaccineData.name);
  return (
    <tr>
      <td>{vaccineData.name}</td>
      <td>{vaccineData.issuer_name}</td>
      <td>{vaccineData.expiration_date}</td>
    </tr>
  );
}

export default VaccineRowIssuer;
