import React from 'react';
import Navigation from '../Navigation/Navigation'
import SideNav from '../SideNav/SideNav'
import bloom from '../../images/bloom.jpg'

const background ={
    backgroundImage: `url(${bloom})`,
    height: "100vh",
    backgroundSize: " contain",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "center",
    backgroundColor: "#abb4fe",


}

const homePage = () => {
    return (
        <div style={background}>
            <Navigation/>
            <SideNav/>
        </div> 
    );
}

export default homePage