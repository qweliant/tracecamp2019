import React from 'react';
import ResponsiveDrawer from './Navigate';
import {BrowserRouter as Router} from 'react-router-dom';
import { MDBJumbotron, MDBBtn, MDBContainer, MDBRow, MDBCol } from "mdbreact";
import Home from './Home';
import Navigate from './Navigate';
import Footer from './Footer'


const App =() =>{
  return (
    <div>
    
    <Navigate/>
      <Home/>
        <Footer/>

    </div>
  );
}

export default App;
