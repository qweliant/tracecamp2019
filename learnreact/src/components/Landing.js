import React from "react";
import bloom2 from '../images/bloom3.png';
import { MDBJumbotron, MDBBtn, MDBMask, MDBView,MDBContainer, MDBRow, MDBCol, MDBCardTitle, MDBIcon } from "mdbreact";

import Image from 'react-bootstrap/Image'
import 'bootstrap/dist/css/bootstrap.min.css';

var sectionStyle = {
    backgroundImage: `url(${bloom2} )`,
    height: "600px",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover",
    backgroundPosition: "center",
  };

  const Landing = () => {
    return (
      
      
    
    <Image src={bloom2} fluid />
    
    );
}

export default Landing;