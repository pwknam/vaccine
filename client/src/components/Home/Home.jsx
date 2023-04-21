import React, { useState } from 'react'
import { WebcamCapture} from '../Webcam/Webcam'
import { useNavigate } from "react-router-dom";
import "./homeStyles.css"


const Home = ({setSearch}) => {
    const [image, setImage] = useState('');
    const[driverslicense, setDriverslicense] = useState('');
    const navigate = useNavigate();


    const handleSubmit= (e) => {
        // alert("Form submitted");
        e.preventDefault()
        fetch('/upload', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image })
          })
          .then(res => {
            if (!res.ok) {
              throw new Error('Network response was not ok');
            }
            return res.json();
          })
          .then(data => {        
            console.log(data);
            setSearch(data.license)
            navigate({ pathname: "/validatorDashboard" });
          })
          .catch(error => {
            console.log(error);
          });
    }



    return (
       
                    <form className="form">
                        <WebcamCapture image={image} handleSubmit={handleSubmit} setImage = {setImage} />
                        <button type="submit" className='button-47' onClick={(e) => handleSubmit(e)}>Submit</button>
                        {driverslicense && <h1>{driverslicense}</h1>}    

                    </form>

    )
}
export default Home