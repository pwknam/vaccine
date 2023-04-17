import './App.css';
import Home from './Home/Home'
import { useState } from 'react';

function App() {


  // const handleImageChange = (event) => {
  //   const file = event.target.files[0];
  //   const reader = new FileReader();
  //   reader.onload = () => {
  //     setImage(reader.result);
  //   };
  //   reader.readAsDataURL(file);
  // };


  return (
    <div>
      <h1>Vaccine Verification</h1>
      <h1>Michelle, Ian, and Kyushik</h1>

      <Home/>
    </div>
  );
}

export default App;




// import './App.css';
// import Home from './Home/Home'
// // import { Butler } from 'butler-sdk';
// import {useState} from 'react';
// // import fs from 'fs';



// function App() {
//   const [image, setImage] = useState('')
//   return (
    
//     <div>
//       <h1>Vaccine Verification</h1>
//       <h1>Michelle, Ian, and Kyushik</h1>
//       <Home image = image/>
//     </div>
       
//   );
// }

// export default App;
